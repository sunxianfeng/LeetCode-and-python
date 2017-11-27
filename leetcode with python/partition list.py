# -*- coding:utf-8 -*-
def partition(self, head, x):
    if head is None:
        return None
    dummy = ListNode(-1)
    dummy.next = head
    sHead = sDummy = ListNode(-1)
    p = dummy
    while p and p.next:
        if p.next.val < x:
            sDummy.next = p.next
            p.next = p.next.next
            sDummy = sDummy.next
        else:
            p = p.next
            # if you change p.next then make sure you wouldn't change p in next run
    sDummy.next = dummy.next
return sHead.next


'''def partitionList(head,x):
    if head is None: return None
    dummy1 = ListNode(0)
    dummy2 = ListNode(0)
    cur1,cur2 = dummy1,dummy2
    while head != None:
        if head.val < x:
            cur1.next = head
            cur1 = cur1.next
        else:
            cur2.next = head
            cur2 = cur2.next
        head = head.next
    cur2.next = None
    cur1.next = dummy2.next
    return dummy1.next
'''