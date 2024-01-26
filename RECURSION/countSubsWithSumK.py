# def CountSub(nums,target,ind ,n , ans , res):
#     if sum(ans) == target:
#         res.append(ans.copy())
#         return ans

#     for i in range(ind,n):
#         ans.append(nums[i])
#         CountSub(nums,target,i+1 ,n , ans , res)
#         ans.pop()

#     return res



# nums = [1,0]
# target= 1
# n = 2
# res= []
# ind = 0
# ans= []
# print(CountSub(nums,target,ind , n ,ans , res))

def countSubs(nums,target,ind,dp, total):
    # if target==0:
    #     return 1


    if ind==n:
        if target==0:
            return 1

        return 0
    x1 = 0
    x2 = 0
    if nums[ind]<=target:
        x1 =  countSubs(nums,target-nums[ind],ind+1,dp, total) 
        x2 = countSubs(nums,target,ind+1,dp, total)
    else:
        x = countSubs(nums,target,ind+1,dp, total)

    x = x1 + x2
    return x


nums = [2, 3, 5, 6, 8, 10]
target= 10
n = 6
print(countSubs(nums,target,0,{}, []))