# TREES
Trees are a type of data structure that represent hierarchical relationships between elements. Each element in a tree is called a node and can have zero or more child nodes. There is a root node that has no parent, and leaf nodes that have no children. The nodes in a tree can also have a parent-child relationship, with a parent having one or more child nodes. Trees can be used to represent many different types of data structures, including binary trees, n-ary trees, and decision trees. They are often used in algorithms to efficiently search and traverse complex data structures, as well as in computer science and information technology for representation of data and storage.

### INVERT A TREE
To invert a binary tree, one approach is to perform a `depth-first traversal` of the tree, swapping the left and right child of each node. This can be done recursively or iteratively. Here's one possible implementation in Python using a recursive approach:
        ``
            class TreeNode:
                def __init__(self, left = None, right = None, val = 0):
                    self.left = left
                    self.right = right
                    self.val = val
            def invertTree(root):
                if not root:
                    return None
                else:
                    root.left, root.right = root.right, root.left
                    invertTree(root.left)
                    invertTree(root.right)

                return root

            def printTree(root):
                if  root:
                    print(root.left)
                    print(root.right)

       ``

## PRE-ORDER Operations
One approach to get the preorder traversal of an N-ary tree is to perform a depth-first traversal of the tree and add the current node's value to the output list before visiting its children. Here's one possible implementation in Python:


### METHOD 1

    ``class Node:
        def __init__(self, val, children=None):
            self.val = val
            self.children = children
    
    def preorderMethodOne(root):
        result = [root.val]
        if not root:
            return result
        for child in root.children:
            result += preorderMethodOne(child)
        return result
    ``
### METHOD 2
    ``class Node:
        def __init__(self, val, children[]):
            self.val = val
            self.children = children

    def preorderMethodTwo(root):
        result = []
        if not root:
            return result.append(root.val)
        for child in root.children:
            result.extend(preorderMethodTwo(child))
    ``
### METHOD 3
    ``
    class Node:
        def __init__(self, val, children=None):
            self.val = val
            self.children = children

        def preorderMethodThree(root):
            if not root
                return []
            res = []
            stack = []

            while stack:
                node = stack.pop()
                res.append(node.val)

                stack.extend(node.children[::-1])
            return res



### Test
``
root = Node(1, [Node(2), Node(3, [Node(4), Node(7), Node(9)])])
result1 = preorderMethodOne(root)
result12 = preorderMethodTwo(root)


print(result1)
print(result2)

```
    


            
