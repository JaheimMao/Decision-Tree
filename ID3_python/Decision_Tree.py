import GetData
import ID3
import TreePlotter

def classify(inputTree, featLabels, testVec):
    """
    输入：决策树，分类标签，测试数据
    输出：决策结果
    描述：跑决策树
    """
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    # 初始化标签，如果没有在决策树中找到结果，则返回的值为默认的'n'
    classLabel = 'n'
    # 遍历树，secondDict.keys()获取所有的键
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            # 判断键是否为字典，键名和其值就组成了一个字典，如果是字典则通过递归继续遍历，寻找叶子节点
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


def classifytest(inputTree, featLabels, testDataSet):
    """
    输入：决策树，分类标签，测试数据集
    输出：决策结果
    描述：跑决策树
    """
    classLabelAll = []
    for testVec in testDataSet:
        classLabelAll.append(classify(inputTree, featLabels, testVec))
    return classLabelAll


if __name__ == '__main__':
    filename = 'data\dna.data'
    testfile = 'data\dna.test'

    dataset, labels = GetData.read_dataset(filename)

    print('dataset', dataset)
    print("---------------------------------------------")
    print("数据集长度", len(dataset))
    print("Ent(D):", ID3.cal_entropy(dataset))
    print("---------------------------------------------")

    print("下面开始创建相应的决策树-------")

    labels_tmp = labels[:]  # 拷贝，createTree会改变labels
    ID3desicionTree = ID3.ID3_createTree(dataset, labels_tmp)
    print('ID3desicionTree:\n', ID3desicionTree)

    # TreePlotter.ID3_Tree(ID3desicionTree)
    TreePlotter.createPlot(ID3desicionTree)
    testSet = GetData.read_dataset(testfile)[0]
    print("下面为测试数据集结果：")
    print('ID3_TestSet_classifyResult:')
    result = classifytest(ID3desicionTree, labels, testSet)
    print(result)
    correct = 0
    for cal_accuracy in range(len(testSet)):
        if result[cal_accuracy] == testSet[cal_accuracy][len(testSet[0])-1]:
            correct = correct + 1
    accuracy = correct / len(testSet)
    print("correct=%d,len(testSet)=%d"%(correct,len(testSet)))
    print("正确率为：", accuracy)
    print("---------------------------------------------")
