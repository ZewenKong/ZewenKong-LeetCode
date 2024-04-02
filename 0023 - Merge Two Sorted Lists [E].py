# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # val 默认为 0
        # next 默认为 None
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    
    head = ListNode()  # 创建 ListNode 对象 object with default value 0 (next is None)
    current = head  # value = 0

    while l1 and l2:  # l1 and l2 是 head node
        if l1.val < l2.val:
            current.next = l1  # 下一个节点设置为 l1 头节点的值, 链接 l1 到链表内 [Pointer to list]
            l1 = l1.next  # 设置头节点为 l1 的下一个节点 (node) [Advance list and current]
        else:
            current.next = l2  # [Pointer to list]
            l2 = l2.next  # [Advance list and current]

        current = current.next  # 设置 current pointer/node 为刚刚链接的节点

    current.next = l1 or l2  # attach the remaining part of one of the lists to the merged list
    return head.next
    # return to starting node (获得链表开头就可以访问整个链表)
    # "返回链表"实际上意味着返回对头节点的引用。一旦得到头节点，就可以通过连续访问`next`指针来访问链表中的每个后续节点


# https://www.youtube.com/watch?v=E5XXiY6QnAs&ab_channel=AlgoEngine





