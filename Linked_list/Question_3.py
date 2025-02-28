class Node:
    def __init__(self,data):
        self.data=data
        self.nextptr=None
class Linked_List:
    def __init__(self):
        self.head = None

    def is_palindrome(self):
        if not self.head or not self.head.nextptr:
            return True
        slow,fast = self.head,self.head
        while fast and fast.nextptr:
            slow=slow.nextptr
            fast = fast.nextptr.nextptr
        second_half = self.reversal(slow)
        first_half = self.head

        while second_half:
            if(first_half.data!=second_half.data):
                return False
            first_half= first_half.nextptr
            second_half=second_half.nextptr

        return True


    def reversal(self,head):
        prev = None
        nextptr= None
        current = head
        while current:
            nextptr = current.nextptr
            current.nextptr= prev
            prev = current
            current =nextptr
        return prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.nextptr
        print("None")



ll=Linked_List()
ll.head =Node(1)
ll.head.nextptr =Node(2)
ll.head.nextptr.nextptr =Node(3)
ll.head.nextptr.nextptr.nextptr =Node(2)
ll.head.nextptr.nextptr.nextptr.nextptr =Node(1)
ll.print_list()
if ll.is_palindrome():
    print("\nYes, it's a palindrome! ")
else:
    print("\nNo, it's not a palindrome. ")