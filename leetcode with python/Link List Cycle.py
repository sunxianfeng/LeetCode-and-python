# -*- coding:utf-8 -*-
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = finder = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while finder != slow:
                    finder = finder.next
                    slow = slow.next
                return finder
        return None
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         fast = slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if slow == fast:
#                 return True
#         return False
