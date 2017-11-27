# -*- coding:utf-8 -*-
def removeNthFromEnd(pHead, n):
    if pHead == None or pHead.next == None:
        return None
    new_head = ListNode(-1)
    new_head.next = pHead
    fast = new_head
    for i in range(0, n):
        if fast.next != None:
            fast = fast.next
        else:
            return pHead
    slow = new_head
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return new_head.next