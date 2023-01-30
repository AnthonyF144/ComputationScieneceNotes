import numpy as np

def my_connectivity_mat_2_dict(C, names):
    # write your function code here
    temp = 0
    count = 0
    tempArray = np.array[C[0]]
    for i in range(tempArray):
        tempArray = [C[i]]
        for j in sizeOfList:
            if (C[i] == 1):
                count += 1
            temp += 1
            node.append(names[i], C[i]*count)
    return node

C = [[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0]]
names = ['Los Angeles', 'New York', 'Miami', 'Dallas']

# Output: node['Los Angeles'] = [2, 4]
#         node['New York'] = [1, 4]
#         node['Miami'] = [4]
#         node['Dallas'] = [1, 2, 3]

node = my_connectivity_mat_2_dict(C, names)