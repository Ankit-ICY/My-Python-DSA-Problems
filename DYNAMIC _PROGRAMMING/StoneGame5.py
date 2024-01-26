
def solve(i , j, dp , nums ):
    if i==j:
        return 0
    total= 0
    for x in range(i,j+1):
        total+=nums[x]


    leftSum = 0
    ans = -1e9
    for  k in range(i,j):

        leftSum += nums[k]
        rightSum = total - leftSum

        if rightSum > leftSum:
            throwRight = leftSum + solve(i , k, dp , nums )
            ans = max(ans, throwRight)

        elif leftSum> rightSum:
            throwLeft = rightSum +  solve(k+1 , j, dp , nums )
            ans = max(ans,throwLeft)

        else:
            throwRight = leftSum  +  solve(i , k, dp , nums )
            throwLeft = rightSum +  solve(k+1 , j, dp , nums )

            ans = max(ans , max(throwLeft , throwRight))

    return ans

nums = [6,2,3,4,5,5]
dp = {}
j = len(nums)-1


i = 0
print(solve(i , j, dp , nums))
