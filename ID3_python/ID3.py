import Decision_Tree
import GetData

def ID3_chooseBestFeatureToSplit(dataset):
    numFeatures = len(dataset[0]) - 1
    baseEnt = cal_entropy(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历所有特征
        # for example in dataset:
        # featList=example[i]
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)  # 将特征列表创建成为set集合，元素不可重复。创建唯一的分类标签列表
        newEnt = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subdataset = splitdataset(dataset, i, value)
            p = len(subdataset) / float(len(dataset))
            newEnt += p * cal_entropy(subdataset)
        infoGain = baseEnt - newEnt
        print(u"ID3中第%d个特征的信息增益为：%.3f" % (i, infoGain))
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain  # 计算最好的信息增益
            bestFeature = i
    return bestFeature

# 利用ID3算法创建决策树
def ID3_createTree(dataset, labels, test_dataset):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataset[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = ID3_chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    print(u"此时最优索引为：" + (bestFeatLabel))

    ID3Tree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)

    if pre_pruning:
        ans = []
        for index in range(len(test_dataset)):
            ans.append(test_dataset[index][-1])
        result_counter = Counter()
        for vec in dataset:
            result_counter[vec[-1]] += 1
        leaf_output = result_counter.most_common(1)[0][0]
        root_acc = cal_acc(test_output=[leaf_output] * len(test_dataset), label=ans)
        outputs = []
        ans = []
        for value in uniqueVals:
            cut_testset = splitdataset(test_dataset, bestFeat, value)
            cut_dataset = splitdataset(dataset, bestFeat, value)
            for vec in cut_testset:
                ans.append(vec[-1])
            result_counter = Counter()
            for vec in cut_dataset:
                result_counter[vec[-1]] += 1
            leaf_output = result_counter.most_common(1)[0][0]
            outputs += [leaf_output] * len(cut_testset)
        cut_acc = cal_acc(test_output=outputs, label=ans)

        if cut_acc <= root_acc:
            return leaf_output

    for value in uniqueVals:
        subLabels = labels[:]
        ID3Tree[bestFeatLabel][value] = ID3_createTree(
            splitdataset(dataset, bestFeat, value),
            subLabels,
            splitdataset(test_dataset, bestFeat, value))

    if post_pruning:
        tree_output = classifytest(ID3Tree,
                                   featLabels=['年龄段', '有工作', '有自己的房子', '信贷情况'],
                                   testDataSet=test_dataset)
        ans = []
        for vec in test_dataset:
            ans.append(vec[-1])
        root_acc = cal_acc(tree_output, ans)
        result_counter = Counter()
        for vec in dataset:
            result_counter[vec[-1]] += 1
        leaf_output = result_counter.most_common(1)[0][0]
        cut_acc = cal_acc([leaf_output] * len(test_dataset), ans)

        if cut_acc >= root_acc:
            return leaf_output

    return ID3Tree