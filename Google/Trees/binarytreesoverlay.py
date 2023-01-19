# Given the root of two binary trees, a and b, return the resulting tree when you overlay a on top of b.
# Note: For any nodes that overlap a is placed on top of b, the resulting tree’s node should contain their sum.

# Ex: Given the following a and b…

# a = 1     b = 4
#    / \       / \
#   2   3     5   6, return the resulting tree...
#            5 (1 + 4)
#          /   \
# (2 + 5) 7     9 (3 + 6)
# Ex: Given the following a and b…

# a = 7     b = 9
#    / \       /
#   2   1     5, return the resulting tree...
#          16
#         /  \
#        7    1

class TreeNode:
    def __init__(self, left=None, right=None, val= 0):
        self.left = left
        self.right = right
        self.val = val

    
def overlay_method(root:TreeNode) -> TreeNode:
    if root not None:
        return None
        

        