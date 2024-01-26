



# def jump(arr, dp,d , n ,ind , prev ):

#     if d<0:
#         return 0

#     if (ind) in dp:
#         return dp[(ind)]

#     ans = 1

#     if ind+1<n and arr[prev]>arr[ind+1]  :
#         x1 = 1 + jump(arr, dp,d , n ,ind+1,ind+1 )
#         x2 =  jump(arr, dp,d-1 , n ,ind+1 ,prev)
#         ans = max(x1,x2)
#         dp[(ind)]= ans

#     if ind-1>=0 and arr[prev]>arr[ind-1]:
#         x1 = 1 + jump(arr, dp,d , n ,ind-1 ,ind-1)
#         x2 =  jump(arr, dp,d-1 , n ,ind-1,prev )
#         ans = max(x1,x2)
#         dp[(ind)]= ans


#     return ans

# arr = [3,3,3,3,3]
# d = 3
# dp = {}
# n = len(arr)
# maxi = -1e9
# prev = -1
# for i in range(n):
#     maxi = max(maxi, jump(arr, dp,d , n ,i ,i))

# print(maxi)




def jump(arr, dp,d , n ,ind ):

    if (ind) in dp:
        return dp[(ind)]

    ans = 1
    # FORWARD
    for i in range(ind+1, min(ind+d+1 , n) ):
        if arr[ind]>arr[i]:
            ans = max(ans,  1 + jump(arr, dp,d , n ,i ))
            dp[(ind)]= ans
        else:
            break
    # BACKWARD
    for i in range(ind-1, max((ind-d)-1 , -1) , -1):
        if  arr[ind]>arr[i]:
            ans = max(ans, 1 +  jump(arr, dp,d , n ,i ))
            dp[(ind)]= ans

        else:
            break


    return ans

arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
dp = {}
n = len(arr)
maxi = -1e9
for i in range(n):
    maxi = max(maxi, jump(arr, dp,d , n ,i ))

print(maxi)

