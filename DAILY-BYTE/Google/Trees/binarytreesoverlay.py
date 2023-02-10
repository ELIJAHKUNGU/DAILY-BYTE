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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def overlay(a, b):
    if not a and not b:
        return None
    elif not a:
        return b
    elif not b:
        return a
    else:
        a.val += b.val
        a.left = overlay(a.left, b.left)
        a.right = overlay(a.right, b.right)
        return a


if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    b = TreeNode(4)
    b.left = TreeNode(5)
    b.right = TreeNode(6)
    result = overlay(a, b)




        