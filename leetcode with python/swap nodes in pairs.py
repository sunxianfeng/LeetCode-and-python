def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    pre, curr = dummy, head
    while curr and curr.next:       # curr =1, curr.next =2
        pre.next = curr.next         # 0 --> 2
        curr.next = pre.next.next    # 1 --> 3  # curr.next.next
        pre.next.next = curr         # 2 --> 1
        pre, curr = curr, curr.next  # pre = 1, curr= 3
    return dummy.next