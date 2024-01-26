from heapq import heappop , heappush , heapify
def solve(heights, distance,i , j ,n , m):
    heap = []  
    heappush(heap, [0 , [i,j]])
    heapify(heap)
    dr = [-1 , 0, 1, 0]
    dc = [0 , 1, 0, -1]

    while(heap):
        node = heappop(heap)
        effort = node[0]
        row = node[1][0]
        col = node[1][1]
        if row == n-1 and col == m-1:
            return distance[row][col]

        for i in range(4):
            newR = row + dr[i]
            newc = col + dc[i]
            if newR >=0  and newc>=0 and newR<n and newc<m:
                newEffort = max(effort ,  abs(heights[row][col] - heights[newR][newc]) )
                if newEffort <distance[newR][newc]:
                    distance[newR][newc] = newEffort
                    heappush(heap, [newEffort , [newR, newc] ])


heights = [[1,10,6,7,9,10,4,9]]

n = len(heights)
m = len(heights[0])

distance = [[1e9]*m for i in range(n)]
i = 0 
j = 0

distance[i][j] = 0
print(solve(heights, distance,i , j , n , m) )