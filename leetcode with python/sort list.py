# -*- coding:utf-8 -*-
class Solution(object):
    def findMiddle(self,head):
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1 != None: tail.next = head1
        else: tail.next = head2
        return dummy.next

    def sortList(self, head):
        if head == None or head.next == None:
            return head
        mid = self.findMiddle(head)

        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.merge(left,right)

