# Given an N-ary tree, return a list containing the preorder traversal of its elements.
# Note: You may assume that each node in the tree has a 
# children attribute to access all of its N child nodes.

# Ex: Given the following N-ary tree


#     1
#      / | \
#     2  3  4, return [1, 2, 3, 4].
# Ex: Given the following N-ary tree…

#        1
#      /   \
#     2     3 
#         / | \
#        4  7  9, return [1, 2, 3, 4, 7, 9].

class TreeNode:

    def __init__(self, val, children=[]) :
        self.val = val
        self.children = children
       


def preorder_function(root):
    # preOrder = root -> left -> right
    result = [root.val]
    if not root:
        return []
    for child in root.children:
        result += preorder_function(child)
    
    return result




if __name__ == "__main__":
    root = TreeNode(1, TreeNode[2],TreeNode[3],TreeNode[4],TreeNode[5],TreeNode[6],TreeNode[7])
    res = preorder_function(root)
    print(res)
    


'''
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        
def preorder(root):
    result = []
    if root:
        result.append(root.val)
        for child in root.children:
            result.extend(preorder(child))
    return result



class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children

def preorder(root):
    if root is None:
        return []
    result = [root.val]
    for child in root.children:
        result += preorder(child)
    return result




'''