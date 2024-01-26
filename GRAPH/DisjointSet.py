class Disjoint:

    def __init__(self , n) -> None:
        
        self.rank  = [0]*(n+1)
        self.parent = [0]*(n+1)
        for i in range(n+1):
            self.parent[i] = i

        self.size = [1]*(n+1)

    def UnionByRank(self,u, v):
        ul_u = self.FindUparent(u)
        ul_v = self.FindUparent(v)
        if ul_u == ul_v :
            return 
        
        if self.rank[ul_u] > self.rank[ul_v]:
            self.parent[ul_v] = ul_u
        
        elif self.rank[ul_v] > self.rank[ul_u]:
            self.parent[ul_u] = ul_v

        else:
            self.parent[ul_u] = ul_v
            self.rank[ul_v] +=1
        


    def FindUparent(self, node):

        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.FindUparent(self.parent[node])
            return self.parent[node]

    
    def UnionBySize(self, u , v):
        ul_u = self.FindUparent(u)
        ul_v = self.FindUparent(v)
        if ul_u == ul_v :
            return 
        
        if self.size[ul_u] > self.size[ul_v]:
            self.parent[ul_v] = ul_u
            self.size[ul_u] += self.size[ul_v]

        elif self.size[ul_v] > self.size[ul_u]:
            self.parent[ul_u] = ul_v
            self.size[ul_v] += self.size[ul_u]

        else:
            self.parent[ul_u] = ul_v
            self.size[ul_v]+= self.size[ul_u]





graph = Disjoint(7)

graph.UnionBySize(1,2)
graph.UnionBySize(2,3)
graph.UnionBySize(4,5)
graph.UnionBySize(6,7)
graph.UnionBySize(5,6)

graph.UnionBySize(3,7)


# if graph.FindUparent(3) == graph.FindUparent(7):
#     print("SAME")
# else:
#     print("NOT SAME")

print(graph.size)