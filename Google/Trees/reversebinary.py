# Given a binary tree, invert it and return the resulting tree.

# Ex: Given the following binary tree…

#         1
#        /  \
#       2    3, return...
#          1
#         /  \
#        3    2
# Ex: Given the following binary tree…

#         1
#        /  \
#       2     3
#      / \   /  \
#     4   5 6    7, return...
#          1
#         /  \
#        3     2
#      /   \  /  \
#     7    6 5    4 \



class TreeNode:
    def __init__(self, left=None, right= None, val=0):
     self.left = left
     self.right = right
     self.val = val


def invertTree(root:TreeNode) ->TreeNode:
    if not  root:
        return None  
    root.left, root.right = root.right , root.left
    invertTree(root.left)
    invertTree(root.right)

    return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(invertTree.val)

    print(invertTree.root.left.val) 
    print(invertTree.root.right.val)
    