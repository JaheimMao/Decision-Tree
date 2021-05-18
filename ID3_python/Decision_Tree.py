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
    classLabel = '0'
    for key in secondDict.keys():
        if testVec[featIndex] == key:
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


def cal_acc(test_output, label):
    """
    :param test_output: the output of testset
    :param label: the answer
    :return: the acc of
    """
    assert len(test_output) == len(label)
    count = 0
    for index in range(len(test_output)):
        if test_output[index] == label[index]:
            count += 1

    return float(count / len(test_output))


if __name__ == '__main__':
    filename = 'data\dna.data'
    testfile = 'data\dna.test'

    dataset, labels = GetData.read_dataset(filename)

    print('dataset', dataset)
    print("---------------------------------------------")
    print("数据集长度", len(dataset))
    print("Ent(D):", ID3.cal_entropy(dataset))
    print("---------------------------------------------")

    print("以下为首次寻找最优索引:\n")
    print("ID3算法的最优特征索引为:" + str(ID3.ID3_chooseBestFeatureToSplit(dataset)))
    print("首次寻找最优索引结束！")
    print("---------------------------------------------")

    print("下面开始创建相应的决策树-------")

    labels_tmp = labels[:]  # 拷贝，createTree会改变labels
    ID3desicionTree = ID3.ID3_createTree(dataset, labels_tmp, test_dataset=GetData.read_dataset(testfile))
    print('ID3desicionTree:\n', ID3desicionTree)

    TreePlotter.ID3_Tree(ID3desicionTree)
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
    print("正确率为：", accuracy)
    print("---------------------------------------------")
