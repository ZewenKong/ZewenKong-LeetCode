root = [1, 3, 2]
def inorderTraversal(root):
    result = []

    def inorder(root, result):
        if root != None:
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

    inorder(root, result)
    return result

# Node	Operation	        Result
# 1	    Left	            []
# 1	    Visit 1	            [1]
# 1	    Right	            [1] (Reaches Node 2)
# 2	    Left	            [1] (Reaches Node 3)
# 3	    Visit	            [1,3]
# 2	    Return & Visit 2	[1, 3, 2]
