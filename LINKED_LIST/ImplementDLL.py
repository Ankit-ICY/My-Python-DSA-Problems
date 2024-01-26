class Node:

    def __init__(self,data , prev) -> None:
        self.data = data
        self.prev = prev
        self.next = None


class D_LinkedList :

    def __init__(self) -> None:
        self.head = None


    def Create_DLL(self, num):
        if self.head == None:
            self.head = Node(num,None)
        
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = Node(num,curr)

    

    def printDLL(self):

        store =""
        curr = self.head
        while curr:
            store += str(curr.data) + "-->"
            curr = curr.next
        
        print(store)



top = D_LinkedList()

nums =[ 4,2,5,1]

for i in range(len(nums)):
    top.Create_DLL(nums[i])


top.printDLL()