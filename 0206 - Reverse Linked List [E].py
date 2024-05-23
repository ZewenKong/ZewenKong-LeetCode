# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr,prev = head,None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        
        return prev