def read_dataset(fileName):
    """
    ge[0:59]代表不同位置的碱基对，分别为A，C，G，T
    A-->1 0 0;C-->0 1 0;G-->0 0 1;T-->0 0 0
    分类结果：ei-->1;ie-->2;n -->3

    :param fileName: The Location of the dataset file
    :return:
        dataset: The dataset which has been translated
        labels: The label of the dataset
    """

    fr = open(fileName, 'r')
    all_lines = fr.readlines()  # list形式,每行为1个str
    # 从文件中读取原始数据，存入list
    data = []
    for line in all_lines[0:]:
        line = line.strip(';\n').split(' ')  # 以逗号为分割符拆分列表
        data.append(line)
    fr.close

    # 生成标签
    labels = []
    for ge in range(int(len(data[0]) / 3)):
        labels.append('ge' + str(ge))
    labels.append('r')

    # 对读取的原始数据进行翻译
    dict = {'100': 'A', '010': 'C', '001': 'G', '000': 'T', '1': 'ei', '2': 'ie', '3': 'n'}
    dataset = []
    for i in range(len(data)):
        dataset.append([])
        j = 0
        for j in range(int(len(data[0]) / 3)):
            try:
                dataset[i].append(dict.get(str(data[i][j * 3]) + str(data[i][j * 3 + 1]) + str(data[i][j * 3 + 2])))
            except:
                print("处理第data[%d][%d]条数据出错！" % (i, j))
        dataset[i].append(dict.get(data[i][len(data[0]) - 1]))
    return dataset, labels


if __name__ == '__main__':
    filename = '..\data\dna.data'
    read_dataset(filename)
