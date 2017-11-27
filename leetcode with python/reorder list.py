# -*- coding:utf-8 -*-
class Solution(object):
     def reverse(self, head):
         newHead = None
         while head != None:
             temp = head.next
             head.next = newHead
             newHead = head
             head = temp
         return newHead

     def merge(self, head1, head2):
         index = 0
         dummy = ListNode(0)
         while head1 != None and head2 != None:
             if index % 2 == 0:
                 dummy.next = head1
                 head1 = head1.next
             else:
                 dummy.next = head2
                 head2 = head2.next
             dummy = dummy.next
             index += 1
         if head1 != None: dummy.next = head1
         else: dummy.next = head2

     def findMiddle(self, head):
         slow, fast = head, head.next
         while fast != None and fast.next != None:
             fast = fast.next.next
             slow = slow.next
         return slow

     def reorderList(self, head):
         if head == None or head.next == None:
             return
         mid = self.findMiddle(head)
         tail = self.reverse(mid.next)
         mid.next = None
         self.merge(head, tail)





    # def reorderList(self, head):
    #     def reverse(root):
    #         pre = None
    #         cur = root
    #         while cur:
    #             next = cur.next
    #             cur.next = pre
    #             pre = cur
    #             cur = next
    #         return pre
    #
    #     if not head or not head.next:
    #         return
    #     slow = fast = head
    #     pre = None
    #     while fast and fast.next:
    #         pre = slow
    #         slow = slow.next
    #         fast = fast.next.next
    #     if pre:
    #         pre.next = None
    #     newHead = reverse(slow)
    #     ret = dummy = ListNode(-1)
    #     p1 = head
    #     p2 = newHead
    #     while p1 and p2:
    #         dummy.next = p1
    #         p1 = p1.next
    #         dummy = dummy.next
    #         dummy.next = p2
    #         p2 = p2.next
    #         dummy = dummy.next
    #
    #     if p2:
    #         dummy.next = p2
    #     head.next = ret.next.next