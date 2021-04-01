function [tree] = ID3()

% ������Ϣ��
labelCounts = {};
% �����п��ܷ��ഴ���ֵ�
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
    Ent = Ent - p * math.log(p, 2);  % ��2Ϊ�������
end
return;
