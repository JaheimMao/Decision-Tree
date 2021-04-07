function [data] = GetData(fname)

% GetData  Get the data from the txt and translate the 1s and 0s into value. 
%       A -> 1 0 0      C -> 0 1 0
%       G -> 0 0 1      T -> 0 0 0
% The class values are 
%       ei -> 1     ie -> 2
%       n  -> 3
% args:
%   fname  - The location of the file
% return:
%   data   - The data in file

%fname = 'dna.data';
fid = fopen(fname, 'rt');
dataInput = textscan(fid, '%s');
dataLen = length(dataInput{1})/181;
fclose(fid);
attributes = cell(1,181);
attributes_mat = zeros(dataLen,181);

for i=1:dataLen
    for j=1:181;
    attributes{j} = dataInput{1}{(i-1)*181+j};
    end
    attributes_mat(i,:) = str2num(char(attributes))';
end

data = cell(dataLen,61);

for i=1:dataLen
    for j=1:60
        if(attributes_mat(i,(j-1)*3+1) == 1)
            data{i,j} = 'A';
        elseif(attributes_mat(i,(j-1)*3+2) == 1)
            data{i,j} = 'C';
        elseif(attributes_mat(i,(j-1)*3+3) == 1)
            data{i,j} = 'G';
        else
            data{i,j} = 'T';
        end
    end
    if(attributes_mat(i,181) == 1)
        data{i,61} = 'ei';
    elseif(attributes_mat(i,181) == 2)
        data{i,61} = 'ie';
    elseif(attributes_mat(i,181) == 3)
        data{i,61} = 'n';
    end
end
return
