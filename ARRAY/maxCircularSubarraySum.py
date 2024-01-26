nums = [20 ,28 ,2, 6, 18 ,12 ,-28 ,3 ,-3 ,-26 ,1 ,6 ,6 ,-27 ,-6 ,-7 ,28 ,-26 ,13 ,30 ,-5 ,-6]

    
maxi = nums[0]
mini = nums[0]
ans = 1e9
for i in range(1,len(nums)):
    el = nums[i]
    x1= el
    x2 = el + maxi
    x3 =  el +mini
    maxi = max(x1,x2,x3)
    mini = min(x1,x2,x3)
    ans = min(ans,mini)

total = sum(nums)

print(total-ans)

# temp = ans
# for i in range(len(nums)):
#     nums[i]= -nums[i]


    
# maxi = nums[0]
# mini = nums[0]
# ans = nums[0]
# for i in range(1,len(nums)):
#     el = nums[i]
#     x1= el
#     x2 = el + maxi
#     x3 =  el +mini
#     maxi = max(x1,x2,x3)
#     mini = min(x1,x2,x3)
#     ans = max(ans,maxi)

# temp2 = total + ans

# print(max(temp, temp2))
