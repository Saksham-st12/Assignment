#convert a singly linked list into a circular linked list


class Node:
    def __init__(self,data):
        self.data=data
        self.nextptr=None
class Linked_List:
    def __init__(self):
        self.head = None
        
    def circular_list(self):
        temp = self.head
        while(temp.nextptr):
            temp= temp.nextptr

        temp.nextptr = self.head
               

    def print_list(self,count=5):
        current = self.head
        printed_nodes = 0

        while current and printed_nodes<count:
            print(current.data, end=" -> ")
            current = current.nextptr
            printed_nodes += 1
        print("... (circular)")


ll=Linked_List()
ll.head =Node(1)
ll.head.nextptr =Node(2)
ll.head.nextptr.nextptr =Node(3)
ll.head.nextptr.nextptr.nextptr =Node(4)
ll.head.nextptr.nextptr.nextptr.nextptr =Node(5)
ll.print_list()
ll.circular_list()
ll.print_list(count = 5)
