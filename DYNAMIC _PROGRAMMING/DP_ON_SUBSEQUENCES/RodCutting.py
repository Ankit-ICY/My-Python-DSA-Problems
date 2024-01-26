def solve(nums,n,ind,dp,cut):
    if ind==n:
        return 0
    
    if (ind) in dp:
        return dp[(ind)]

    sum = 0
    ans = 0
    length = 0
    for i in range(ind,n):
        sum=nums[length]
        length +=1
        ans = max(ans , sum +solve(nums,n,i+1,dp,cut) )
        dp[(ind)] = ans

    dp[(ind)] = ans
    return ans


nums = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
ind = 0
dp = {}
cut = 0
print(solve(nums,n,ind,dp,cut ))