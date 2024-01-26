def BoolCheck(mid,n,nums,k):
    count = 1
    lasPos = nums[0]
    for i in range(1,n):
        if nums[i] - lasPos>mid:
            count+=1
            lasPos = nums[i]

        if count==k:
            return True
        
    return False    
        

nums = [10 ,1 ,2 ,7 ,5]
nums.sort()
k =3 
n = 5

s  = 0
e = max(nums)-min(nums)

mid = s + (e-s)//2

while(s<=e):
    if BoolCheck(mid,n,nums,k):
        s = mid+1

    else:
        e= mid-1

    
    mid = s + (e-s)//2

print(s)