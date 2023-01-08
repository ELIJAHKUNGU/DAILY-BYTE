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
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertBeginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    # def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list

        # Now insert data_to_insert after data_after node

    # def remove_by_value(self, data):
    #     # Remove first node that contains data
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next



        
        
       


           
      



if __name__ == '__main__':
    ll = LinkedList()
    # ll.insertBeginning(5)
    # ll.insertBeginning(56)
    # ll.insert_values(["banana", "mango", "grapes", "orange"])
    # ll.print()
    # ll.insert_at(1, "blueberry")
    # ll.print()
    # ll.remove_at(2)
    # ll.print()
    # ll.insertAtEnd(4)
    # ll.insertAtEnd(5)
    # ll.insertAtEnd(6)
    # ll.insertAtEnd(7)

    # ll.insertAtEnd(9)
    # ll.insertAtEnd(16)

    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    print("After inserting apple after mango")
    ll.print()
