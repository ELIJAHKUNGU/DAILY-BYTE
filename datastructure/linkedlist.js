//  A linked list is a linear collection of data elements, in which linear order is not given by their physical placement in memory.
//  Instead, each element points to the next. It is a data structure consisting of a group of nodes which together represent a sequence. 
//  Under the simplest form, each node is composed of data and a reference (in other words, a link) to the next node in the sequence. 
//  This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. 
//  More complex variants add additional links, allowing efficient insertion or removal from arbitrary element references.
//  A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible.
//   Arrays have better cache locality as compared to linked lists.

// PSEUDOCODE OPERATIONS
// 1. Insertion
// 2. Deletion
// 3. Traversal
// 4. Searching
// 5. Sorting
// 6. Merging


class Node {
    constructor (element) {
        this.element = element;
        this.next = null;


    }
}

class LinkedList {
    constructor () {
        this.head = null;
        this.size = 0;
    }


    // Insertion
    addELement (element) {
        var node = new Node (element)

        var current

        if (this.head == null) {
            this.head = node
            
        }else {
            current = this.head
            while (current.next){
                current = current.next
            }
        }
        this.size ++ ;

    
    }

    // Insert At 
    insertAtCertainIndex (element, index) {

        if (index > this.size || index < 0) {
            return console.log('Enter a valid index');
            
        }

        var node = new Node(element)

        var current, previous

        current = this.head

        if(index = 0){
            node.next = this.head
            this.head = node
        }

        current = this.head
        var it = 0
        while (it < index) {
            it ++
            previous = current
            current = current.next
        }

        node.next = current
        previous.next = node

        this.size ++;

    }
}

