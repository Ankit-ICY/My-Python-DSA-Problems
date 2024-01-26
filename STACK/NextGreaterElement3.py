n = 2147483486

n = str(n)
nums =[]
for i in range(len(n)):
    nums.append(int(n[i]))

tempo = nums
ind = -1
ans = []
for i in range(len(nums)-2,-1,-1):
    if nums[i]<nums[i+1]:
        ind = i
        break

if ind==-1:
    for i in range(len(nums)):
        nums[i] = tempo[i]
    print(-1)
else:
    for i in range(len(nums)-1,ind,-1):
        if nums[i]>nums[ind]:
        
            temp = nums[ind]
            nums[ind] = nums[i]
            nums[i] = temp
            break

    ans = (nums[ind+1:])
    ans.reverse()
    x = 0
    for i in range(ind+1,len(nums)):
        nums[i] = ans[x]
        x+=1
 
    string = ""
    for i in range(len(nums)):
        string+=str(nums[i])

    string = int(string)
    n = int(n)
    print(string)