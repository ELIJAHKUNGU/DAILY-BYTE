# Tree

A tree is a hierarchical data structure that consists of nodes and edges. Each node in a tree represents an object or a piece of data, and each edge represents a relationship between the two connected nodes. The top node in a tree is called the `root`, and the nodes that do not have any children are called l`eaf nodes`. Trees can be used to represent various types of data and relationships, such as` file systems`, `decision trees`, and `parse trees`. The tree data structure is widely used in computer science and is a fundamental concept in algorithms and data structures.
## Other Defnitions
A Tree is a non-linear data structure and a hierarchy consisting of a collection of nodes such that each node of the tree stores a value and a list of references to other nodes (the “children”).
<a href="https://www.geeksforgeeks.org/introduction-to-tree-data-structure-and-algorithm-tutorials/" >Trees</a>

### Why Tree is considered a non-linear data structure?
The data in a tree are not stored in a sequential manner i.e, they are not stored linearly. Instead, they are arranged on multiple levels or we can say it is a hierarchical structure. For this reason, the tree is considered to be a non-linear data structure.

<img src="https://github.com/ELIJAHKUNGU/DAILY-BYTE/blob/facebook/Datastructure/Trees/Treedatastructure.png" alt="loading" />

### Basic Terminologies In Tree Data Structure:
1. Parent Node: The node which is a predecessor of a node is called the parent node of that node. {B} is the parent node of {D, E}.
2. Child Node: The node which is the immediate successor of a node is called the child node of that node. Examples: {D, E} are the child nodes of {B}.
3. Root Node: The topmost node of a tree or the node which does not have any parent node is called the root node. {A} is the root node of the tree. A non-empty tree must contain exactly one root node and exactly one path from the root to all other nodes of the tree.
4. Leaf Node or External Node: The nodes which do not have any child nodes are called leaf nodes. {K, L, M, N, O, P} are the leaf nodes of the tree.
5. Descendant: Any successor node on the path from the leaf node to that node. {E,I} are the descendants of the node {B}.
6. Sibling: Children of the same parent node are called siblings. {D,E} are called siblings.
7. Level of a node: The count of edges on the path from the root node to that node. The root node has level 0.
8. Internal node: A node with at least one child is called Internal Node.
9. Neighbour of a Node: Parent or child nodes of that node are called neighbors of that node.
10 .Subtree: Any node of the tree along with its descendant.
11. Ancestor of a Node: Any predecessor nodes on the path of the root to that node are called Ancestors of that node. {A,B} are the ancestor nodes of the node {E}
## Properties of a Tree:
1. Number of edges: An edge can be defined as the connection between two nodes. If a tree has N nodes then it will have (N-1) edges. There is only one path from each node to any other node of the tree.
2. Depth of a node: The depth of a node is defined as the length of the path from the root to that node. Each edge adds 1 unit of length to the path. So, it can also be defined as the number of edges in the path from the root of the tree to the node.
3. Height of a node: The height of a node can be defined as the length of the longest path from the node to a leaf node of the tree.
Height of the Tree: The height of a tree is the length of the longest path from the root of the tree to a leaf node of the tree.
4. Degree of a Node: The total count of subtrees attached to that node is called the degree of the node. The degree of a leaf node must be 0. The degree of a tree is the maximum degree of a node among all the nodes in the tree.
#### Some more properties are:

Traversing in a tree is done by depth first search and breadth first search algorithm.
1. It has no loop and no circuit
2. It has no self-loop 
3. Its hierarchical model.

## Types of Tree data structures
The different types of tree data structures are as follows:

1. General tree

A general tree data structure has no restriction on the number of nodes. It means that a parent node can have any number of child nodes.  

2. Binary tree  

A node of a binary tree can have a maximum of two child nodes. In the given tree diagram, node B, D, and F are left children, while E, C, and G are the right children.  

3. Balanced tree

If the height of the left sub-tree and the right sub-tree is equal or differs at most by 1, the tree is known as a balanced tree.

4. Binary search tree

As the name implies, binary search trees are used for various searching and sorting algorithms. The examples include AVL tree and red-black tree. It is a non-linear data structure. It shows that the value of the left node is less than its parent, while the value of the right node is greater than its parent.

Applications of Tree data structure:
The applications of tree data structures are as follows:

1. Spanning trees: It is the shortest path tree used in the routers to direct the packets to the destination.  

2. Binary Search Tree: It is a type of tree data structure that helps in maintaining a sorted stream of data.  

Full Binary tree
Complete Binary tree
Skewed Binary tree
Strictly Binary tree
Extended Binary tree
3. Storing hierarchical data: Tree data structures are used to store the hierarchical data, which means data is arranged in the form of order.  

4. Syntax tree: The syntax tree represents the structure of the program’s source code, which is used in compilers.  

5. Trie: It is a fast and efficient way for dynamic spell checking. It is also used for locating specific keys from within a set.  

6. Heap: It is also a tree data structure that can be represented in a form of an array. It is used to implement priority queues.  



### Why to use Tree Data Structure? 
1. One reason to use trees might be because you want to store information that naturally forms a hierarchy.
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on the number of nodes as nodes are linked using pointers.

# Binary Trees
#### What is a Binary Tree?
A binary tree is a tree data structure composed of nodes, each of which has at most, two children, referred to as left and right nodes and the tree begins from root node.

```
# A Python class that represents
# an individual node in a Binary Tree

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

```
### Basic Operations On Binary Tree:
1. Inserting an element.
2. Removing an element.
3. Searching for an element.
4. Deletion for an element.
5. Traversing an element. There are four (mainly three) types of traversals in a binary tree which will be discussed ahead.

### Tree Traversal algorithms can be classified broadly into two categories:

1. Depth-First Search (DFS) Algorithms
2. Breadth-First Search (BFS) Algorithms
#### Tree Traversal using Depth-First Search (DFS) algorithm can be further classified into three categories:

Preorder Traversal (current-left-right: It means that the root node is traversed first then its left child and finally the right child.
Inorder Traversal (left-current-right): . Here, the traversal is left child – root – right child.  It means that the left child is traversed first then its root node and finally the right child.
Postorder Traversal (left-right-current):  Here, the traversal is left child – right child – root.  It means that the left child has traversed first then the right child and finally its root node

<img src="https://github.com/ELIJAHKUNGU/DAILY-BYTE/blob/facebook/Datastructure/Trees/level.png" alt="loading">

Pre-order Traversal of the above tree: 1-2-4-5-3-6-7 Root-Left-Right

In-order Traversal of the above tree: 4-2-5-1-6-3-7 Left - Root - Right

Post-order Traversal of the above tree: 4-5-2-6-7-3-1 Left - Right- Node 

Level-order Traversal of the above tree: 1-2-3-4-5-6-7 Root -left- right - left -right

### Tree Traversal using Breadth-First Search (BFS) algorithm can be further classified into one category:
Level Order Traversal:It means that the most left child has traversed first and then the other children of the same level from left to right have traversed. 
```
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


if __name__ == "__main__":
    # Create root
    root = Node(1)
    ''' following is the tree after above statement
    1
    / \
    None None'''
    root.left = Node(2)
    root.right = Node(3)
 
    ''' 2 and 3 become left and right children of 1
    1
    / \
    2 3
    / \ / \
    None None None None'''
    
    root.left.left = Node(4)
    '''4 becomes left child of 2
    1
    / \
    2 3
    / \ / \
    4 None None None
    / \
    None None'''
        
```

