# -*- coding:utf-8 -*-
def sortColors(A):
    len_A = len(A)
    if len(A) == 1:
        return
    left = 0
    right = len_A - 1
    i = 0
    while i <= right:
        if A[i] == 0:
            if left == i:
                i += 1
            else:
                A[left], A[i] = A[i], A[left]
            left += 1
        elif A[i] == 1:
            i += 1
        else:
            if right == i:
                i += 1
            else:
                A[right], A[i] = A[i], A[right]
            right -= 1

a = [1,2,0,0,0,2,1,0,1,2,0,0,2,2]
sortColors(a)
print a