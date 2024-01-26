# <---------BRUTE FORCE---------->
# nums =[1,1,1]
# k = 2
# ans= []

# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         ans.append(abs(nums[j]-nums[i]))

# ans.sort()
# print(ans[k-1])


# <---------------BINARY SEARCH + SLIDING WINDOW ----------------->
def slidingWind(mid , nums, n):
    count = 0
    j  = 0
    for i in range(1,n):
        while nums[i] - nums[j]>mid:
            j+=1
        
        count+=(i-j)
    
    return count

nums = [1,6,1]
k = 3
nums.sort()
low = 1e9
high = nums[-1] - nums[0]
n = len(nums)

for i in range(1,n):
    if nums[i]-nums[i-1]<low:
        low = nums[i] - nums[i-1]

while(low<high):
    mid = (low+high)//2

    if slidingWind(mid , nums, n)< k:
        low = mid+1
    else:
        high = mid

print(low)
    

