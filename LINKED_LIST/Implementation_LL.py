class Node:
    def __init__(self , data,next) :
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) :
        self.top = None


    def insert_at_Begin(self, data,head):
        # node = Node(data, head)
        # head = node

        # self.top = node

        temp = Node(data,head)
        # temp.next = head
        head = temp
        self.top  = temp
        return head



    def insert_at_End(self,data):
        if self.head==None:
            self.head = Node(data,None)
            return
        else:
            itr = self.head
            while(itr.next!= None):
                itr = itr.next

            itr.next = Node(data, None)

    def insert_at_Index(self, data, index):
        if index<0 and index>= self.get_length():
            raise Exception("INVALID INDEX")

        if index==0:
            self.insert_at_Begin(self, data)
            return
        
        else:
            count = 0

            temp = self.head

            while(temp):
                count+=1
                if count==index:
                    node = Node(data, temp.next)
                    temp.next = node
                    break

            return


    def get_length(self):
        if self.head== None:
            return 0
        count =0
        temp = self.head

        while(temp):
            count+=1
            temp= temp.next

        return count

    def remove_node(self, node):
        if self.head == None:
            return 

        itr = self.head

        while itr.next and itr.next.data!= node:
            itr = itr.next

        if itr.next.next!=None:
            itr.next  = itr.next.next
        else:
            itr.next = None
        

    # def print(self,head):
        # if head == None:
        #     print("LINKED LIST IS EMPTY")
        #     return
        # else:
        #     temp= head
        #     store = ""

        #     while temp :
        #         store += str(temp.data) +  '-->'
        #         temp = temp.next
                
            
        #     print(store)
            

    
    def print(self,head):
        if not self.top:
            print("LINKED LIST IS EMPTY")
            return
        else:
            store = ""
            x = self.top
            while x:
                store += str(x.data) +  '-->'
                x= x.next

            print(store)

      

    def CreateLL(self, data,head):
        if head.data == None:
            head.data = data
            self.top = head
        else:
            while head.next:
                head= head.next

            head.next = Node(data ,None)


    def reverse(self,head):
        ans = []
        if not head:
            return

        if head.next:
            ans+= self.reverse(head.next)
        
        ans.append(head.data)

        return ans

    def revereseLinkedList(self,curr,prev,head):
        if not curr:
            self.top = prev
            # head = prev
            return 
        forward = curr.next 
        self.revereseLinkedList(  forward, curr, head)
        curr.next= prev

        return 

    
    def reverseNodesByK(self,head,k):
        if k==1:
            return head
        
        curr= head
        prev = None
        cnt = 0
        while curr and cnt<k:
            if curr:
                forward = curr.next
                curr.next = prev
                prev =curr
                curr = forward
            cnt +=1
            
        head = prev
            
        cnt = 0
        temp = head
        
        last = None
        while curr:
            while temp.next:
                temp = temp.next
            cnt = 0
            last = None
            new = curr
            while curr and cnt<k:
                forward = curr.next
                curr.next = last
                last =curr
                curr = forward
                cnt+=1
            
            if cnt !=k:
                while new:
                    temp.next = new
                    new = new.next
                    temp = temp.next
                curr = None
            else:
                temp.next = last

        return head
                


        # if not head or head.next == None:
        #     return 
        
    
        # prev = None
        # curr= head

        # while curr!= None:
        #     forward = curr.next
        #     curr.next = prev    
        #     prev= curr
        #     curr = forward

        # self.top  = prev


    def middleLL(self,head):
        def getLen(head):
            count = 0
            if not head:
                return 1

            count += getLen(head.next)
        
            return count
        
        n =  getLen(head)
        
        ans = n//2

        cnt =0 
        temp = head
        while cnt<ans:
            temp = temp.next


        return temp
    
    def detectCycle(self,head):
        temp = head
        ind = 0
        map = []
        while temp:
            if temp not in map:
                map.append(temp)
                temp = temp.next
            else:
                return temp


        return -1
        
    def makecycle(self,head):

        temp = head
        top = head

        while temp.next:
            temp = temp.next

        temp.next = top





    def AddTwoNumb(self,head1,head2 ):
        
        def add(first, second):
            carry = 0
            temp = Node(-1, None)
            curr = temp
            while first or second:
                if first:
                    value1 = first.data
                    first = first.next
                else:
                    value1 = 0
                
                if second:
                    value2 =second.data
                    second = second.next
                else:
                    value2 = 0

                sum = value1 + value2 + carry
                carry = sum//10
                curr.next  = Node(sum%10 , None)
                curr = curr.next
                

            return temp.next

        def reverse(head):

            curr = head
            prev = None
            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward   

            return prev
        # STEP 1

        first = reverse(head1)
        second = reverse(head2)


        #STEP 2 
        ans = add(first, second)

        #STEP 3

        return reverse(ans)
    
    def reverseByK(self,head,k):
        curr= head
        prev = None
        while curr and cnt<k:
            if curr:
                forward = curr.next
                curr.next = prev
                prev =curr
                curr = forward
            cnt +=1

    def intersection(self, head1 , head2):
        def reverse(head):

            curr = head
            prev = None

            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward

            return prev

        first = reverse(head1)
        second = reverse(head2)
        last = None
        while first.data == second.data:
            last = first
            first = first.next
            second = second.next

        return last.data
    
    
    def addOne(self, head):
        def reverse(head):

            curr =head
            prev = None
            while curr:
                forward = curr.next
                curr.next =prev
                prev = curr
                curr=  forward
            return prev
            
        heads = reverse(head)


        carry = 1
        temp = heads
        res = Node(-1 , None)
        ans = res
        while temp:
            value = temp.data

            sum = value + carry
            ans.next = Node(sum%10 , None)
            ans = ans.next
            carry = sum//2
            temp = temp.next

        return reverse(res.next)

    
    def reverseNodesByK(self,head,k):
        if k==1:
            return head
        
        curr= head
        prev = None
        cnt = 0
        while curr and cnt<k:
            if curr:
                forward = curr.next
                curr.next = prev
                prev =curr
                curr = forward
            cnt +=1
            
        head = prev
            
        cnt = 0
        temp = head
        
        last = None
        while curr:
            while temp.next:
                temp = temp.next
            cnt = 0
            last = None
            new = curr
            while curr and cnt<k:
                forward = curr.next
                curr.next = last
                last =curr
                curr = forward
                cnt+=1
            
            if cnt !=k:
                while new:
                    temp.next = new
                    new = new.next
                    temp = temp.next
                curr = None
            else:
                temp.next = last

        return head
            


ob = LinkedList()


head = Node(None, None)


e1 = [1,2,3,4,5]
for i in range(len(e1)):
    ob.CreateLL(e1[i] , head)


head = ob.reverseNodesByK(head, 3)
# head = ob.addOne(head)

ob.print(head)