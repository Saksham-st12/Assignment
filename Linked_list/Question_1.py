# Given a single singly linked list give the reversal of that ex: 1->2->3->4->5
class Node:
    def __init__(self,data):
        self.data=data
        self.nextptr=None
class Linked_List:
    def __init__(self):
        self.head = None
    def reversal(self):
        prev = None
        nextptr= None
        current = ll.head
        while current:
            nextptr = current.nextptr
            current.nextptr= prev
            prev = current
            current =nextptr
        ll.head = prev
        return ll
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.nextptr
        print("None")



ll=Linked_List
ll.head =Node(1)
ll.head.nextptr =Node(2)
ll.head.nextptr.nextptr =Node(3)
ll.head.nextptr.nextptr.nextptr =Node(4)
ll.head.nextptr.nextptr.nextptr.nextptr =Node(5)
ll.print_list()
ll.reversal()
ll.print_list()