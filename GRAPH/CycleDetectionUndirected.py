# def isCyclicBFS(node , visited,adj):
#     parent = {}
#     parent[node] = -1

#     q = [node]
#     visited[node] = True
#     while(q):
#         Fnode = q.pop(0)
#         for i in adj[Fnode]:
#             if not visited[i] :
#                 visited[i]  = True
#                 parent[i] = Fnode
#                 q.append(i)

#             elif visited[i] and parent[Fnode] != i:
#                 return True
#     return False

    
# adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 
# # adj = [[], [2], [1, 3], [2]]
# v = 5
# e = 5

# visited = {}
# for i in range(v):
#     visited[i] = False

# for i in range(v):
#     if not visited[i]:
#         if  isCyclicBFS(i , visited,adj):
#             print(True)
#             break



# DFS
def isCyclicDFS(node , parent, visited,adj):

    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            if isCyclicDFS(i , node, visited,adj):
                return True
        elif i != parent:
            return True


    return False


    
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 
v = 5
e = 5

visited = {}
for i in range(v):
    visited[i] = False

for i in range(v):
    if not visited[i]:
        if  isCyclicDFS(i , -1, visited,adj):
            print(True)
            break 

