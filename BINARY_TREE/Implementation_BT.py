


class Node:

    def __init__(self , data) -> None:
        self.data = data
        self.left = None
        self.right = None




    def add_child(self,data):
        if data == self.data or data<0:
            return 
        
        if data < self.data:
            
            if self.left:
                self.left.add_child(data)

            else:
                self.left = Node(data)
        

        else:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = Node(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
 

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

    def search(self,val):
        if self.data == val:
            return True


        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False



    def find_min(self):
        if self.left:
            return self.left.find_min()

        else:
            return self.data


    def find_max(self):
        if self.right:
            return self.right.find_max()

        else:
            return self.data

    

    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum =self.data +   self.left.calculate_sum() 
   
        if self.right:
            sum = sum + self.right.calculate_sum()  

        return sum


    def level_order_traversal(self):
        queue = [num_tree]
        level = []
        next_queue = []
        result = []
        while queue!=[]:
            for root in queue:
                level.append(root.data)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)

            result.append(level.copy())
            level = []
            queue = next_queue
            next_queue = []
        return result
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()

        if self.right:
            elements+=self.right.pre_order_traversal()


        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements+=self.left. post_order_traversal()

        if self.right:
            elements+=self.right. post_order_traversal()

        elements.append(self.data)

        return elements


def build_From_level_order_Traversal():
    print("ENTER THE ROOT NODE\n")
    data = int(input())
    root = Node(data) 
    q = [root]

    while(q!=[]):
        temp = q[0]
        q.pop(0)

        print("ENTER THE LEFT CHILD FOR " , temp.data)
        leftData = int(input())

        if leftData != -1:
            temp.left =  Node(leftData)
            q.append(temp.left)

        

        print("ENTER THE Right CHILD FOR " , temp.data)
        rightData = int(input())

        if rightData !=-1:
            temp.right = Node(rightData)
            q.append(temp.right)

    


def build_tree(elements):
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


root = Node(None)

nums =  [2,3,1,3,1,None,1]
num_tree= build_tree(nums)

tree = build_From_level_order_Traversal()
print(tree)
# level_order_traversal()


