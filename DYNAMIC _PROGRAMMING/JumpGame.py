def koodKaKhel(nums,ind,dp):

    if ind==len(nums)-1:
        return True

    if ind>len(nums)-1:
        return False

    for i in range(1, nums[ind]+1):
        if koodKaKhel(nums,ind+i,dp):
            return True

    return False

nums = [3,2,1,0,4]
ind = 0
dp ={}
print(koodKaKhel(nums,ind,dp))