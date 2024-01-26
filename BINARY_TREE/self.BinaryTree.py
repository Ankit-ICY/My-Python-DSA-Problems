class Node :
    def __init__(self,data) -> None:

        self.data= data
        self.left = None
        self.right = None



class Solution:

    def Create_Tree(self,data):
        root = Node(data)

        return root
    
    def preOrder_Traversal(self,root):
        elements = []

        elements.append(root.data)
        if root.left:
            elements+=self.preOrder_Traversal(root.left)


        if root.right:
            elements+=self.preOrder_Traversal(root.right)

        return elements
    

    def build_From_level_order_Traversal(self,root):
        if root.data:
            q  = [root]
        else:
            print("ENTER THE ROOT NODE\n")
            data = int(input())
            # root = Node(data) 
            root.data =data 
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

        
    def level_order_traversal(self,root):
        queue = [root]
        level = []
        next_queue = []
        result = []
        while queue!=[]:
            for root in queue:
                if root:
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
    

    def height(self,root):
        if not root :
            return 0
        left = 0
        right= 0
        ans = 0
        if root.left:
            left = 1 + self.height(root.left)

        if root.right:
            right = 1 + self.height(root.right)

        ans = max(left,right)

        return ans
         

    def isBalanced(self,root):
        if not root:
            return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        diff = abs(self.heights(root.left) - self.heights(root.right))<=1

        if left and right and diff :
            return 1

        else:
            return 0

    def isSumTree(self,root):
        # Code here
        if not  root:
            return True
        
        if not root.left and not root.right:
            return True
        left= self.isSumTree(root.left)
        right = self.isSumTree(root.right)
        
        leftSum = 0
        rightSum = 0

     
        leftSum = self.Sum(root.left) 
        
        rightSum =  self.Sum(root.right)

        comp  =  leftSum + rightSum== root.data
        
        if comp  and left and right:
            return True
            
        else:
            return False
        

    def Sum(self,root):
        sum = 0
            
        if not root:
            return 0
        
        
        sum = root.data + self.Sum(root.left)
        sum +=  self.Sum(root.right)
        
        
        return sum
    
    def zigzagLevelOrder(self, root) :
        q = [root]
        next = []
        level  = []
        result = []
        leftToRight = True
        while q != []:
            
            for root in q:
                if root:
                    level.append(root.data)
                    if root.left :
                        next.append(root.left)
                    if root.right:
                        next.append(root.right)
    
            q = next
            next = []
            if level and not leftToRight :
                level.reverse()
            if level:
                result.append(level)
            level = []
            leftToRight = not leftToRight
        return result                


    def BoundaryTraversal(self, root,ans):
        ans.append(root.data)
        self.leftNodes(root.left,ans)
        self.leafNodes(root.left,ans)
        self.leafNodes(root.right,ans)
        self.rightNodes(root.right,ans)

        return ans

    def leftNodes(self,root,ans):
        if not root:
            return  ans

        if (not root.left and not root.right) :
            return ans

    
        ans.append(root.data)
        if root.left:
            self.leftNodes(root.left,ans)

        else:
            self.leftNodes(root.right,ans)
        

    def rightNodes(self,root,ans):
        if not root:
            return

        if not root.left and not root.right :
            return
        
        if root.right:
            self.rightNodes(root.right,ans)
        else:
            self.rightNodes(root.left,ans)

        ans.append(root.data)


    
    def leafNodes(self,root,ans):
        if not root:
            return ans

        if not root.left and not root.right:
            ans.append(root.data)
            return ans

        if root.left:
            self.leafNodes(root.left,ans)

        if root.right:
            self.leafNodes(root.right,ans)

    

      

    def Top_View(self,root):
        map  = {}

        q = [[root, 0]]
        ans = []
        while q!=[]:
            temp = q[0]
            q.pop(0)

            fnode = temp[0]
            hd = temp[1]

            if hd not in map:
                map[hd] = fnode.data

            if fnode.left:
                q.append([fnode.left , hd-1])
            if fnode.right:
                q.append([fnode.right , hd+1])

        from collections import OrderedDict

        map = OrderedDict(sorted(map.items()))
        for i in map:
            ans.append(map[i])

        return ans
    
    def verticalTraversal(self, root) :
        q =[[root, 0,0]]
        map = {}
        ans =[]
    
        while(q!=[]):
            
            temp = q.pop(0)
            fnode= temp[0]
            hd  = temp[1]
            level = temp[2]
            if fnode.left:
                q.append([fnode.left,hd-1,level+1])

            if fnode.right:
                q.append([fnode.right, hd+1,level+1])

            if hd not in map:
                map[hd] = [[level,fnode.val]]

            else:
                map[hd].append([level,fnode.val])


        for i in sorted(map):
            temp=map[i]
            temp.sort()
            t=[]
            for j in temp:
                t.append(j[1])
            ans.append(t)

        return ans


    def bottom_view(self,root):
        map = {}
        
        q = [[root, 0]]
        while q!=[]:
            temp = q.pop(0)

            fnode = temp[0]
            hd = temp[1]

            if fnode.left:
                q.append([fnode.left,hd-1])

            if fnode.right:
                q.append([fnode.right,hd+1])

            if hd in map:
                map[hd] = fnode.data
            else:
                map[hd] = fnode.data


        from collections import OrderedDict
        ans = []
        map = OrderedDict(sorted(map.items()))
        for i in map:
            ans.append(map[i])

        return ans

    


    def rightSideView(self) :
        

    
        def rightView(ans,root,level):
            if  not root:
                return 


            if level == len(ans):
                ans.append(root.val)


            rightView(ans,root.right,level+1)
            rightView(ans,root.left,level+1)

            return ans
        ans =[]
        return rightView(ans,root,0)



    def sumOfLongRootToLeafPath(self,root):
            #code here
            sum = 0
            len = 0
            ans =[0,0]
            self.solve(sum, ans,len,root)
            return ans[0]
            
        
    def solve(self,sum, ans,len,root):
        if not root:
            if len>ans[1]:
                ans[1]=len
                ans[0] = sum
                
            elif len==ans[1]:
                ans[0] = max(sum, ans[0])
                
            return ans
 
        
        sum +=root.data
        self.solve(sum, ans,len+1,root.left)
        self.solve(sum, ans,len+1,root.right)
            
        return ans
    
    def Tree_Build(self,root,elements):
        root.data = elements[0]
        elements.pop(0)
        q = [root]
        next  = []

        while(elements!=[]):
            for root in q:
                if elements:
                    temp1 = elements.pop(0)
                if elements:
                    temp2 = elements.pop(0)

                if temp1:
                    root.left=  Node(temp1)
                    next.append(root.left)

                if temp2:
                    root.right = Node(temp2)
                    next.append(root.right)

                temp1, temp2 = 0,0
            

            q = next
            next = []
            temp1, temp2 = 0,0

        root = None
        return root

        
    def MaxSum_Non_Adjacent(self,root):
        def solve(root ):
            if not root:
                return [0,0]
            


            left = solve(root.left)
            right = solve(root.right)
            map = [0,0]
            map[0] = root.data  + left[1]+right[1]
            map[1] = max(left[0],left[1] )  + max(right[0] ,right[1])
            # map[1] = left[0] + right[0]

            return map

        return max(solve(root ))
         

    def ConstructTree_From_IN_PRE_ORder(self, inorder , preorder): 
        indi= 0
        def construct_tree(inorder , preorder,ind, i, j, n):
            nonlocal indi
            if indi>=n or i>j:
                return

            data = preorder[indi]
            indi+=1
            root = Node(data)
            pos = inorder.index(data)

            root.left = construct_tree(inorder , preorder,ind, i, pos-1, n)
            root.right = construct_tree(inorder , preorder,ind, pos+1, j, n)

            return root

        i = 0
        j = len(inorder)-1
        n = len(inorder)        

        return construct_tree(inorder , preorder,0, i, j, n)

    def findBottomLeftValue(self, root) :

        q =[root]
        level =[]
        ans = 0
        next = []
        while q!=[]:

            for root in q:
                if root:
                    level.append(root.data)
                    if root.left:
                        next.append(root.left)
                    if root.right:
                        next.append(root.right)

            if level:
                ans=level[0]
            level = []
            q = next
            next = []
        return ans
    

    def maxPathSum(self, root) :
        sum = 0

        def maxSum(root):
            nonlocal sum
            if not root:
                return float("-inf")

            left= max(maxSum(root.left),0)
            right= max(maxSum(root.right),0)

            sum = max(sum , root.val + left + right )

            return root.val + max(left , right)

        maxSum(root)
        return sum
    
    def serialize(self, root):
        ans = []
        
        def solve(root):
            if not root:
                ans.append('#')
                return 
            
            ans.append(str(root.data))
            solve(root.left)
            solve(root.right)



        solve(root)
        return ','.join(ans)
        

    def deserialize(self, data):
        datalist = data.split(',')
        
        def solve2():
            if datalist:
                value = datalist.pop()
                if value == "#":
                    return None
                else:
                    root = Node(int(value))
                    root.left = solve2()
                    root.right  = solve2()

                return root
    

        ans = solve2()
        return ans




root = Node(None)
ob = Solution()



ele = [1,2,3,None,None,4,5]
ob.Tree_Build(root,ele)
print(ob.level_order_traversal(root))

