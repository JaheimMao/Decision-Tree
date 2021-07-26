<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

# Decision Tree

## 1 相关背景知识

### 1.1 熵、信息熵、熵增益

&emsp;&emsp;根据维基百科的介绍，熵是一个科学概念，也是一个可测量的物理量，和混乱度、随机性、不确定性类似。熵最初是一个热力学的概念，用于描述物理内分子的混乱程度。熵在很多的领域都会被用到。信息是一个很抽象的概念，很难用进行量化评价。直到香农提出了“信息熵”的概念，才解决了对信息的量化度量问题。信息熵这个词是香农从热力学中借鉴过来的。香农用信息熵的概念来描述信源的不确定度。假定当前样本集合$D$中第$k$类样本所占的比例为$p_k(k=1,2,3,\ldots,\vert y\vert)$，则$D$的信息熵定义为  
$$
Ent(D)=-\sum_{k=1}^{\vert y\vert}p_k\log_2p_k \tag{1-1}
$$  
$Ent(D)$的值越小，则$D$的纯度越高。  
&emsp;&emsp;假定离散属性a有V个可能的取值$\{a^1,a^2,\ldots,a^V\}$，若使用$a$来对样本集$D$进行划分，则会产生$V$个分支节点，其中第$v$个分支节点包括了$D$中所有在属性$a$上取值为$a^v$的样本，记为$D^v$，我们可以根据式(1-1)计算出$D^v$的信息熵，再考虑到不同分支节点所包含的样本数不同，给分支节点赋予权重$\vert D^v\vert/\vert D\vert$，即样本数越多的分支节点的影响越大，于是可计算出用属性$a$对样本集$D$进行划分所获得的“信息增益”(information gain)  
$$
Gain(D,a)=Ent(D)-\sum_{v=1}^V\frac{\vert D^v\vert}{\vert D\vert}Ent(D^v)\tag{1-2}
$$  
&emsp;&emsp;一般而言，信息增益越大，则意味着使用属性$a$来进行划分所获得的“纯度提升”越大。因此，我们可用信息增益来进行决策树的划分属性选择。
## 1.2 决策树结构

&emsp;&emsp;决策树是一个树形结构(可以是二叉树或者非二叉树)，其中每个非叶子节点表示一个属性，叶子节点表示一个类。决策树可以看成一个嵌套的if-then结构。决策树构建的关键就是选择分裂属性。ID3算法是最优化选择分裂属性的算法。

## 2 使用MATLAB进行编程

### 2.1 MATLAB读取数据
&emsp;&emsp;使用MATLAB读取数据的第一步是根据路径打开文件，使用```textscan()```获取其中的数据，并关闭文件。从文件中获取的数据为cell格式。

## 3 使用Python进行编程

### 3.1 Python读取数据

## 参考文献

[深入浅出理解决策树算法（一）-核心思想](https://zhuanlan.zhihu.com/p/26703300)
