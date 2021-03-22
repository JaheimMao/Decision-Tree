import GetData
import ID3
from GetData import read_dataset

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
    filename = 'dataset.txt'
    testfile = 'testset.txt'
    dataset, labels = read_dataset(filename)
    # dataset,features=createDataSet()
    print('dataset', dataset)
    print("---------------------------------------------")
    print(u"数据集长度", len(dataset))
    print("Ent(D):", cal_entropy(dataset))
    print("---------------------------------------------")

    print(u"以下为首次寻找最优索引:\n")
    print(u"ID3算法的最优特征索引为:" + str(ID3_chooseBestFeatureToSplit(dataset)))
    print(u"首次寻找最优索引结束！")
    print("---------------------------------------------")

    print(u"下面开始创建相应的决策树-------")

    while True:
        dec_tree = '1'
        # ID3决策树
        if dec_tree == '1':
            labels_tmp = labels[:]  # 拷贝，createTree会改变labels
            ID3desicionTree = ID3_createTree(dataset, labels_tmp, test_dataset=read_testset(testfile))
            print('ID3desicionTree:\n', ID3desicionTree)
            # treePlotter.createPlot(ID3desicionTree)
            treePlotter.ID3_Tree(ID3desicionTree)
            testSet = read_testset(testfile)
            print("下面为测试数据集结果：")
            print('ID3_TestSet_classifyResult:\n', classifytest(ID3desicionTree, labels, testSet))
            print("---------------------------------------------")
        break