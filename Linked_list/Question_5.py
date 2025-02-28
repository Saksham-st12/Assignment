class ListNode:
    def __init__(self,data):
        self.data=data
        self.nextptr=None
class Solution:
    def __init__(self):
        self.head = None

    def detectLoop(self):

        slow,fast = self.head,self.head
        while fast and fast.nextptr:
            slow=slow.nextptr
            fast = fast.nextptr.nextptr
            if slow== fast:
                print("Loop detected in the linked list!")
                return True
        print("No loop found in the linked list.")
        return False


    def print_list(self, n=20):
        current = self.head
        count = 0
        while current and count < n:
            print(current.val, end=" -> ")
            current = current.nextptr
            count += 1
        print("None")

#test case

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


node1.nextptr = node2
node2.nextptr = node3
node3.nextptr = node4
node4.nextptr = node5


node5.nextptr = node3

sol = Solution()
sol.head = node1


sol.detectLoop()

