nums =[5, 8, 40, 11, 15]
m = 2
n = 5


nums.sort()



i = 0
j =len(nums)-1
mini = 0
maxi = 0
while m:
    maxi +=nums[j]
    mini += nums[i]
    i+=1
    j-=1
    m-=1


print(maxi-mini)
    