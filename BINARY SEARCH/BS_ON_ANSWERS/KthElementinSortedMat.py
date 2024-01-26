def CountElements(mid,n):
    cnt = 0
    for i in range(n):
        if mat[i][n-1]<=mid:
            cnt +=n
            continue
        for j in range(n):
            if mat[i][j] < mid:
                cnt+=1
            else:
                break


    return cnt



mat = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
n = len(mat)
s = mat[0][0]

e = mat[n-1][n-1]
ans = 0

while s<=e :
    mid = s+ (e-s)//2

    count = CountElements(mid,n)
    # if count == mid:
    #     ans = mid
    #     break

    if count<k:
        s = mid+1

    else:
        e = mid


print(s)

