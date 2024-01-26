class Graph:

    global dic
    dic = {}

    def addEdge(self, u , v, direction):
        
        if u not in dic:
            dic[u] = [v]

        else:
            dic[u].append(v)


    def printAdjList(self):

        for i in dic.keys():
            print(i , '-->', end=' ')
            for j in dic[i]:
                print(j , ',', end= "")

            print("\n")
                




g = Graph()

# n = int(input("ENTER THE NUMBER OF EDGES : "))
# u= 0 
# v=  0
# print("ENTER THE EDGES")
# for i in range(n):
#     u, v = input().split()

#     g.addEdge(u,v,0)

edge = [[1,2], [2,3], [1,4], [3,5], [2,4]]

for i  in range(len(edge)):
    g.addEdge(edge[i][0],edge[i][1],0)




g.printAdjList()


