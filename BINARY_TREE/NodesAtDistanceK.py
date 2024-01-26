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


    def nodesAtDisK(self, root,target,k):
        def getParents(dic,root,target,source,vis):
            q = [root]

            while q:

                root = q.pop(0)
                vis[root] = False
                if root.data == target:
                    source  = root
                if root.left:
                    dic[root.left] = root
                    q.append(root.left)
                
                if root.right:
                    dic[root.right]  = root
                    q.append(root.right)
                

            return source


        dic ={}
        source = None
        vis = {}
        source = getParents(dic,root,target,source ,vis)
        ans =[]
        q =[[source,k]]

        while q:
            root = q.pop(0)
            node = root[0]
            dist = root[1]
            if node:
                vis[node] = True
                if dist == 0:
                    ans.append(node.data)
                    continue
                if node.left and not vis[node.left]:
                    q.append([node.left,dist-1])
                
                if node.right and not vis[node.right]:
                    q.append([node.right , dist-1])
                
                if node in dic and not vis[dic[node]]:
                    q.append([dic[node] , dist-1])


        return ans
    
    def height(self,root):
        if not root:
            return 0

        count = 0


        left = self.height(root.left)
        right = self.height(root.right)

        count+= max(left , right) +1 

        return count


root = Node()
roots = [2,3,1,3,1,None,1]
# target = 5
# k = 2

ob = BT()

ob.createTree(root,roots)
ans = ob.level_order_traversal(root)
print(ans)
# print(ob.level_order_traversal(root))

# print(ob.nodesAtDisK(root,target,k))
# print(ob.height(root))