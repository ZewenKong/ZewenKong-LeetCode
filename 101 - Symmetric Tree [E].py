# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def aSymmetric(self, right, left):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and self.aSymmetric(left.left, right.right) and self.aSymmetric(left.right, right.left)
        # left.val == right.val
        # if equal, return true, else return false

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.aSymmetric(root.left, root.right)