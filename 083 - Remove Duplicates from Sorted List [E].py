# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        temp = head

        while (temp and temp.next):
            if (temp.next.val == temp.val):
                temp.next = temp.next.next
                continue
            temp = temp.next  # 设置 temp pointer/node 为下一个节点

        return head