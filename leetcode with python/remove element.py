# -*- coding:utf-8 -*-
def removeElement(alist,elem):
    n = len(alist)
    index = 0
    for i in range(0,n):
        if alist[i] != elem:
            alist[index] = alist[i]
            index += 1
    return index




# def removeElement(A, elem):
#     if None == A:
#         return A
#     len_A = len(A)
#     m = 0
#     n = len_A - 1
#     while m <= n:
#         if elem == A[m]:
#             if elem != A[n]:
#                 A[m], A[n] = A[n], A[m]
#                 m += 1
#                 n -= 1
#             else:
#                 n -= 1
#         else:
#             m += 1
#     return n + 1
a = [1,2,6,9,12,2,4,2]
length = removeElement(a,2)
print length