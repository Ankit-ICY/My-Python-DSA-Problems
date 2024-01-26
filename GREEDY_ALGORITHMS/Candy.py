nums = [1,3,4,5,2]


n = len(nums)
candy= [1]*n


for i in range(1,n):
    if nums[i]>nums[i-1] and (candy[i]<=candy[i-1]):
        candy[i] = candy[i-1]+1
    else:
        continue


for i in range(n-2 , -1,-1) :
    if nums[i] >nums[i+1] and (candy[i]<=candy[i+1]):
        candy[i] = candy[i+1]+1

    else:
        continue

print(candy)

