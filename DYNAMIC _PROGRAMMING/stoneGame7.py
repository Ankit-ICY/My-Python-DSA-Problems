
def solve(i,j,dp,nums , chance):
    if i>=j:
        return 0
    total = 0
    for k in range(i , j+1):
        total +=nums[k]
    x0 = 0
    x3 = 0

    x1 = total-nums[j] - solve(i,j-1,dp,nums , 0)
    x2 = total - nums[i] - solve(i+1,j,dp,nums , 0)
    x = max(x1,x2)

    return x

nums = [7,90,5,1,100,10,10,2]
i = 0
j = len(nums)-1
dp ={}  
chance = 1
print(solve(i,j,dp,nums , chance))