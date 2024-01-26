class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.left = None
        self.right  = None

class BT:
    def createTree(self,root,elements):
        n = elements.pop(0)
        root.data = n
        
        q= [root]
        while elements:
            while q:
                root = q.pop(0)
                if elements:
                    node = elements.pop(0)

                if elements:
                    node2 = elements.pop(0)

                if node!=None:
                    root.left = Node(node)
                    q.append(root.left)
     
                if node2!=None:
                    root.right = Node(node2)
                    q.append(root.right)

                node=  None
                node2 = None     
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
        
    def pseudoPalindromicPaths (self, root) :
        ans = 0
        def solve(root,dic):
            nonlocal ans
            if not root:
                return 

            if root.data in dic:
                dic[root.data]+=1

            else:
                dic[root.data] = 1

            
            if not root.left and not root.right:
                flag =0
                count = 0
                for i , j in dic.items():
                    if j & 1 :
                        count+=1
                    if count>1:
                        flag = 1
                        break
                if flag==0:
                    ans+=1
                dic[root.data]-=1
                if dic[root.data] == 0:
                    del dic[root.data]
                return 


            left  = solve(root.left,dic)   
            right = solve(root.right,dic) 
            dic[root.data]-=1
            if dic[root.data] == 0:
                del dic[root.data] 
            return            
        dic = {}
        solve(root,dic)
        return ans
root = Node()
roots = [2,3,1,3,1,None,1]
ob = BT()
ob.createTree(root,roots)
ans = ob.pseudoPalindromicPaths(root)
print(ans)