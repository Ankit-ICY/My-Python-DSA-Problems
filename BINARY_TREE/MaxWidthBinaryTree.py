class Tree:
    def __init__(self,data) -> None:

        self.data= data
        self.left = None
        self.right = None

class Solution:

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
                    root.left=  Tree(temp1)
                    next.append(root.left)

                if temp2:
                    root.right = Tree(temp2)
                    next.append(root.right)

                temp1, temp2 = 0,0
                

            q = next
            next = []
            temp1, temp2 = 0,0

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


    def maxWidthBT(self,root):

        q = [[root,0]]
        next_q = []
        level = []
        result = []
        ans = 0
        maxi = 0
        while q:
            for r in q:
                root = r[0]
                ind = r[1]
                level.append([root.data , ind])
                if root:
                    if root.left:
                        next_q.append([root.left , 2*ind + 1])
                    if root.right:
                        next_q.append([root.right , 2*ind + 2])
            

            

            if level:
                diff = level[-1][-1] - level[0][1] + 1
                ans = max(ans, diff)
                result.append(level.copy())
            level =[]
            q = next_q
            next_q =[]

        return ans

    def pathSum(self, root, target: int) :
        ans = []
        res =[]
        def solve(root,target) : 
            
            if target == 0:
                res.append(ans.copy())
                return ans
        
            if not root:
                return 


            ans.append(root.data)
            if root.data <= target:
                
                solve(root.left,target-root.data)
                ans.pop()
                solve(root.right,target - root.data)
                
            return res

        
        return solve(root,target)
    
    def hasPathSum(self, root, target: int) -> bool:
        if not root:
            return False
        if root:
            q = [[root,root.data]]
        else:
            q = [[root , 0]]

        while q:
            node = q.pop(0)
            root = node[0]
            sum = node[1]

            if sum == target and not root.left and not root.right:
                return True

            if root.left:
                q.append([root.left, sum + root.data])

            if root.right:
                q.append([root.right , sum +root.data])

        
        return False

                




root  = Tree(None)


elements= [1,2 ,None]
ob = Solution()

ob.Tree_Build(root,elements)
target = 2
print(ob.pathSum(root,target))