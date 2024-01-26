mat = [[1,2,3],[4,5,6],[7,8,9]]

right = 1
left = 0

m = len(mat)
n = len(mat[0])

i = 0
j = 0


ans = []
while i < m and j<n:
    if right == 1:
        while i>= 0 and j < n:
            ans.append(mat[i][j]) 
            i-=1
            j+=1

        if j == n:
            i+=2
            j-=1
        else:
            i = 0
        right = 0

    else:
        
        while i< m and j>=0:
            ans.append(mat[i][j])
            j-=1
            i+=1

        if i==m:
            j+=2
            i-=1
        else:
            j = 0

        right = 1
        

print(ans)