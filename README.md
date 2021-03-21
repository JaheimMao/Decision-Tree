# Decision Tree

## 决策树结构

&ensp;决策树是一个树形结构，其中每个非叶子节点表示一个属性，叶子节点表示一个类。决策树可以看成一个嵌套的if-then结构。决策树构建的关键就是选择分裂属性。ID3算法是最优化选择分裂属性的算法。

## 信息熵

## 使用MATLAB进行编程

### MATLAB读取数据
&ensp;使用MATLAB读取数据的第一步是根据路径打开文件，使用```textscan()```获取其中的数据，并关闭文件。从文件中获取的数据为cell格式。