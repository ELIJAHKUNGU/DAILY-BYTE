class Node:
    def __init__(self, data=None, next=None):
        self.data = data,
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is emptu")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + "----->"
            itr = itr.next
        print(llstr)
    def insertAtEnd(self, data):
        if self.head is None:
            self.head  = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insertBeginning(5)
    # ll.insertBeginning(56)
    ll.insertAtEnd(5)
    ll.insertAtEnd(9)
    ll.insertAtEnd(16)
    
    ll.print()
