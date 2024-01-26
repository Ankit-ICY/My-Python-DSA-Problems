def BoolCheck(nums,mid,m ,n):
    count = 1  
    total =0 
    
    for i in range(n):
        if total+nums[i]<=mid:
            total+=nums[i]
        else:
            count+=1
            total = nums[i]

    if count >m:
        return False

    return True

nums = [1 ,2 ,4 ,8, 9]
m =3
n = 5
sum = 0
maxi = 0
for i in range(n):
    sum+=nums[i]
    if maxi <nums[i]:
        maxi = nums[i]

s = maxi
e = sum
mid = s + (e-s)//2

while(s<=e):
    if BoolCheck(nums,mid,m ,n):
        e = mid-1
    else:
        s = mid+1

    mid = s + (e-s)//2

print(s)