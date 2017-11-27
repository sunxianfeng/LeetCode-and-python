# -*- coding:utf-8 -*-
import heapq as p
import random

class MyHeap(object):
    def __init__(self, array):
        self.n = len(array)
        self.list = array

    def build_heap(self):
        n_hat = self.n
        for i in range(n_hat // 2 - 1, -1, -1):                    # 遍历所有的非叶子节点进行heapify
            self.heapify(i)
        return self.list

    def heapify(self, i):                                           # 最大堆

        j = i * 2 + 1                                                # 存储堆的数组以0开始，j为i的左孩子
        while j < self.n:
            if j + 1 < self.n and self.list[j] < self.list[j + 1]:   # j+1<n 为右孩子存在
                j += 1
            if self.list[i] > self.list[j]:
                break
            else:
                self.list[i], self.list[j] = self.list[j], self.list[i]
            i = j
            j = i * 2 + 1

    def heap_sort(self):
        res = []
        self.build_heap()
        # 交换堆顶与最后一个结点,再调整堆
        for i in xrange(self.n):
            p.heapify(self.list)
            res.append(p.heappop(self.list))
        # for i in range(self.n - 1, 0, -1):
        #     res.append(self.list[0])
        #     self.list[0], self.list[i] = self.list[i], self.list[0]
        #     self.heapify(0)
        return res
if __name__ == '__main__':

    a1=[13,14,2,7,3,10,6,9]
    print a1
    myheap=MyHeap(a1)
    heap = myheap.build_heap()
    sorted_heap = myheap.heap_sort()
    print heap,sorted_heap
