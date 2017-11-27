# -*- coding:utf-8 -*-
def setZeroes(matrix):
    if matrix == None or matrix == [] or matrix[0] == None or matrix[0] == []:
        return
    firstrow_clear = False
    firstcol_clear = False
    len_x = len(matrix)
    len_y = len(matrix[0])
    for i in range(0, len_x):
        for j in range(0, len_y):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                if i == 0:
                    firstrow_clear = True
                if j == 0:
                    firstcol_clear = True
    for i in range(1, len_x):
        if matrix[i][0] == 0:
            for j in range(0, len_y):
                matrix[i][j] = 0
    for j in range(1, len_y):
        if matrix[0][j] == 0:
            for i in range(0, len_x):
                matrix[i][j] = 0
    if firstcol_clear:
        for i in range(1, len_x):
            matrix[i][0] = 0
    if firstrow_clear:
        for j in range(1, len_y):
            matrix[0][j] = 0
        # def setZeroes(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     if m == 0 or n == 0: return
#     hasZeros = 0
#     for i in range(m):  # 第i行
#         if matrix[i][0] == 0:  # 第零列
#             hasZeros = 1
#         for j in range(1, n):  # 第i行的第j列
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0
#     for i in range(m - 1, -1, -1):  # i = 2,1,0
#         for j in range(n - 1, 0, -1):  # j = 2,1
#             if matrix[i][0] == 0 or matrix[0][j] == 0:# 第零列的第i行，或第零行的第i列任一个为零，则将第i行第j列的元素置为零
#                 matrix[i][j] = 0
#         if hasZeros == 1:
#             matrix[i][0] = 0
#     return



matrix = [[1, 0, 2],
          [0, 1, 3],
          [2, 1, 1]]
setZeroes(matrix)
print matrix