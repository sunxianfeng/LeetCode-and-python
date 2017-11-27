# -*- coding:utf-8 -*-

def build_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n)
def heapify(array, i, n):                            #从第i节点开始，n为结束节点
    j = i * 2 + 1                                     #存储堆的数组以0开始，j为i的左孩子
    while j < n:
        if j + 1 < n and array[j] < array[j + 1]:     #j+1<n 为右孩子存在
            j += 1
        if array[i] > array[j]:
            break
        else: array[i], array[j] = array[j], array[i]
        i = j
        j = i * 2 + 1
res = []
def heap_sort(array):
    n = len(array)
    build_heap(array)
    # 交换堆顶与最后一个结点,再调整堆
    for i in range(n - 1, 0, -1):
        res.append(array[0])
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)


a = [13,14,2,7,3,10,6,9]
print a
build_heap(a)
print a
heap_sort(a)
print res