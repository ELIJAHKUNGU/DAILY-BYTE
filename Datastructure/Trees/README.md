# Tree

A tree is a hierarchical data structure that consists of nodes and edges. Each node in a tree represents an object or a piece of data, and each edge represents a relationship between the two connected nodes. The top node in a tree is called the `root`, and the nodes that do not have any children are called l`eaf nodes`. Trees can be used to represent various types of data and relationships, such as` file systems`, `decision trees`, and `parse trees`. The tree data structure is widely used in computer science and is a fundamental concept in algorithms and data structures.
## Other Defnitions
A Tree is a non-linear data structure and a hierarchy consisting of a collection of nodes such that each node of the tree stores a value and a list of references to other nodes (the “children”).
<a href="https://www.geeksforgeeks.org/introduction-to-tree-data-structure-and-algorithm-tutorials/" >Trees</>

### Why Tree is considered a non-linear data structure?
The data in a tree are not stored in a sequential manner i.e, they are not stored linearly. Instead, they are arranged on multiple levels or we can say it is a hierarchical structure. For this reason, the tree is considered to be a non-linear data structure.

### Basic Terminologies In Tree Data Structure:
1. Parent Node: The node which is a predecessor of a node is called the parent node of that node. {B} is the parent node of {D, E}.
2. Child Node: The node which is the immediate successor of a node is called the child node of that node. Examples: {D, E} are the child nodes of {B}.
3. Root Node: The topmost node of a tree or the node which does not have any parent node is called the root node. {A} is the root node of the tree. A non-empty tree must contain exactly one root node and exactly one path from the root to all other nodes of the tree.
4. Leaf Node or External Node: The nodes which do not have any child nodes are called leaf nodes. {K, L, M, N, O, P} are the leaf nodes of the tree.
Ancestor of a Node: Any predecessor nodes on the path of the root to that node are called Ancestors of that node. {A,B} are the ancestor nodes of the node {E}
5. Descendant: Any successor node on the path from the leaf node to that node. {E,I} are the descendants of the node {B}.
Sibling: Children of the same parent node are called siblings. {D,E} are called siblings.
6. Level of a node: The count of edges on the path from the root node to that node. The root node has level 0.
7. Internal node: A node with at least one child is called Internal Node.
Neighbour of a Node: Parent or child nodes of that node are called neighbors of that node.
Subtree: Any node of the tree along with its descendant.
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