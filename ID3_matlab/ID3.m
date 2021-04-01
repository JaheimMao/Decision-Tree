function [tree] = ID3()

% 计算信息熵
labelCounts = {};
% 给所有可能分类创建字典
for featVec in dataset:
    currentlabel = featVec[-1];
    if currentlabel not in labelCounts.keys():
        labelCounts[currentlabel] = 0;
    end
    labelCounts[currentlabel] += 1;
end
Ent = 0.0;
for key in labelCounts:
    p = float(labelCounts[key]) / numEntries;
    Ent = Ent - p * math.log(p, 2);  % 以2为底求对数
end
return;
