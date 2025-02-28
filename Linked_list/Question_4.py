# Remove the nth node from end

class Node:
    def __init__(self, data):
        self.data = data
        self.nextptr = None

class Linked_List:
    def __init__(self):
        self.head = None

    def del_n_element(self, n):
        first = self.head
        second = self.head
        
        for i in range(n):
            if first is None:
                print("Position out of range")
                return
            first = first.nextptr
        if first is None:
            self.head = self.head.nextptr
            return
        while first.nextptr:
            first = first.nextptr
            second = second.nextptr
        second.nextptr = second.nextptr.nextptr
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.nextptr
        print("None")

ll = Linked_List()
ll.head = Node(1)
ll.head.nextptr = Node(2)
ll.head.nextptr.nextptr = Node(3)
ll.head.nextptr.nextptr.nextptr = Node(4)
ll.head.nextptr.nextptr.nextptr.nextptr = Node(5)
print("Original Linked List:")
ll.print_list()
ll.del_n_element(2)
print("\nLinked List after removing 2nd node from the end:")
ll.print_list()
