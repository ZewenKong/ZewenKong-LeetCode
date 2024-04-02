# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    ldepth = self.maxDepth(root.left)
    rdepth = self.maxDepth(root.right)
    return max(ldepth, rdepth) + 1

# not complete