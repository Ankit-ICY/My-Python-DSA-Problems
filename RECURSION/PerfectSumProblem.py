def perfectSum(nums,n,sum,ind , dp):
    


    if ind==n and sum>0:
        return 0

    elif ind <n :
        if sum==0:
            if nums[ind]==0:
                return 2
            else:
                return 1

            
        # else:
        #     if nums[ind]==sum:
        #         return 1
        #     else:
        #         return 0

    elif  sum==0:
        return 1


    score = 0
    a = 0
    # if (ind,sum) in dp:
    #     return dp[(ind,sum)]
    for i in range(ind,len(nums)):
        if nums[i]<=sum:
            a +=perfectSum(nums,n,sum -nums[i],i+1,dp)
            score = max(a, score )  

 
    return score

nums = [1,0]
n = 2
sum = 1

ind = 0
dp  = {}
print(perfectSum(nums,n,sum,ind,dp))
# def perfectSum(nums,n,sum,ans,res,ind , dp):

#     if sum == 0:
#         res.append(ans.copy())
#         return ans

#     if (ind,sum) in dp:
#         return dp[(ind,sum)]


#     for i in range(ind, n):
#         if nums[i]<=sum:
#             ans.append(nums[i])
#             dp[(ind,sum)] = perfectSum(nums,n,sum -nums[i],ans,res,i+1,dp)
#             ans.pop()

#     return res

# nums = [1,0]
# n = 2
# sum = 1
# ans = []
# res = []
# ind = 0
# dp  = {}
# print(perfectSum(nums,n,sum,ans,res,ind,dp))