def deleteNearn(nums,ind,dp,value):
    if ind==len(nums):
        return 0

    if (ind,value) in dp:
        return dp[(ind,value)]    

    earn = nums[ind]
    if  value==-1 or earn!= value+1:
        x1 = earn + deleteNearn(nums,ind+1,dp,earn)
        x2 = deleteNearn(nums,ind+1,dp,value)
        dp[(ind,value)] =max(x1,x2)

    else:
        dp[(ind,value)] = deleteNearn(nums,ind+1,dp,value)
        
    return dp[(ind,value)]

nums = [3,4,2]
nums.sort()
ind = 0
dp ={}
value = -1
print(deleteNearn(nums,ind,dp,value))




