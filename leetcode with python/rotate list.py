# -*- coding:utf-8 -*-
def rotateRight(head, k):
    if head == None or head.next == None or k == 0:
        return head
    count = 0
    p = head
    while (p):
        count += 1
        p = p.next

    k = k % count  # 真实旋转值k
    if k == 0: return head
    p = head
    while (k > 0):  # 执行完p为链表第k+1个结点
        k -= 1
        p = p.next
    slow = head  # slow为头结点
    fast = p  # fast为当前p
    while fast.next:  # 将fast移到链表尾结点的同时，slow也向尾结点方向移
        slow = slow.next  # fast移到尾结点的同时，slow指向旋转后的尾结点
        fast = fast.next
    new_head = slow.next  # 旋转后的尾结点的下一个结点即为新链表的头结点
    fast.next = head  # 原链表的尾结点指向原头结点
    slow.next = None  # 旋转后的尾结点指向None
    return new_head