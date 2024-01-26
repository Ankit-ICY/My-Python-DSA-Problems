# def solve(nums1,nums2,ind,prev,dp):

  
#     if ind==len(nums1):
#         return 0

#     if (ind,prev) in dp:
#         return dp[(ind,prev)]
    
#     x1= 0
#     if prev == -1 or nums1[ind] > prev:
#         x1 = 1 + solve(nums1,nums2,ind+1,nums1[ind],dp)


#     x2= 0
#     if prev ==-1 or nums2[ind] > prev:
#         x2 = 1 + solve(nums1,nums2,ind+1,nums2[ind],dp)


#     x3 = solve(nums1,nums2,ind+1,prev,dp)
#     dp[(ind,prev)]= max(x1,x2,x3)


#     return dp[(ind,prev)]


# nums1 = [3,19,13,19]
# nums2 = [20,18,7,14]
# prev = -1
# dp = {}
# ind = 0
# print(solve(nums1,nums2,ind,prev,dp))



nums1 = [1,8]
nums2 = [10,1]

dp1 = [1] *len(nums1)
dp2 = [1] * len(nums2)
n= len(nums1)


for i in range(1,n):
    for j in range(i-1,i):
        if nums1[i] >= nums1[j] :
            dp1[i] = max(dp1[j] +1 ,dp1[i])

        if nums1[i] >= nums2[j]  :
            dp1[i] = max(dp2[j] + 1,dp1[i])

        if nums2[i] >= nums1[j] :
            dp2[i] = max(dp1[j] +1 ,dp2[i])

        if nums2[i] >= nums2[j]  :
            dp2[i] = max(dp2[j] + 1, dp2[i])


print(dp1)
print(dp2)



# for i in range(1,n):

#     for j in range(0,i):

#         if (nums1[i]>=nums1[j] or nums1[i]>=nums2[j] )and dp[i] < 1 + dp[j]:
#             dp[i] = 1 + dp[j]

#         elif (nums2[i]>=nums2[j]  or  nums2[i]>=nums1[j] ) and dp[i] < 1 + dp[j]:
#             dp[i] = 1 + dp[j]

#         else:
#             dp[i] = 0


