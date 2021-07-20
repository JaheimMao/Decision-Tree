import math
import operator

def cal_entropy(dataset):
    """
    Calculate the entropy of the dataset

    :param dataset: The dataset which need to calculate the entropy
    :return:
        Ent: The entropy of the dataset
    """

    numEntries = len(dataset)
    labelCounts = {}
    # 给所有可能分类创建字典
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    Ent = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / numEntries
        Ent = Ent - p * math.log(p, 2)  # 以2为底求对数
    return Ent


# 划分数据集
def splitdataset(dataset, axis, value):
    retdataset = []  # 创建返回的数据集列表
    for featVec in dataset:  # 抽取符合划分特征的值
        if featVec[axis] == value:
            reducedfeatVec = featVec[:axis]  # 去掉axis特征
            reducedfeatVec.extend(featVec[axis + 1:])  # 将符合条件的特征添加到返回的数据集列表
            retdataset.append(reducedfeatVec)
    return retdataset


# 根据计算得到的信息熵，选择属性
def ID3_chooseBestFeatureToSplit(dataset):
    numFeatures = len(dataset[0]) - 1
    baseEnt = cal_entropy(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历所有特征
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)  # 将特征列表创建成为set集合，元素不可重复。创建唯一的分类标签列表
        newEnt = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subdataset = splitdataset(dataset, i, value)
            p = len(subdataset) / float(len(dataset))
            newEnt += p * cal_entropy(subdataset)
        infoGain = baseEnt - newEnt
        # print("ID3中第%d个特征的信息增益为：%.3f" % (i, infoGain))
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain  # 计算最好的信息增益
            bestFeature = i
    return bestFeature


# 利用ID3算法创建决策树
def ID3_createTree(dataset, labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    bestFeat = ID3_chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    print("此时最优索引为：" + (bestFeatLabel))

    ID3Tree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)

    for value in uniqueVals:
        subLabels = labels[:]
        ID3Tree[bestFeatLabel][value] = ID3_createTree(
            splitdataset(dataset, bestFeat, value),
            subLabels)

    return ID3Tree
