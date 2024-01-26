nums1 = [2 ,3 ,6 ,7, 9]
nums2 = [1 ,4 ,8 ,10]
k = 4
m = len(nums1)
n = len(nums2)

nums = []
i = 0
j = 0
while(i<m and j < n):
    if nums1[i]<nums2[j]:
        nums.append(nums1[i])
        i+=1
    else:
        nums.append(nums2[j])
        j+=1

while i<m:
    nums.append(nums1[i])
    i+=1
    
while j<n:
    nums.append(nums2[j])
    j+=1

print(nums)


def  upperBound(ele):
    s = 0
    e = len(nums)-1
    ans = 0
    while s<=e:
        mid = s + (e-s)//2

        if nums[mid]>ele :
            ans = mid
            e= mid-1

        else:
            s = mid+1
    
    return ans

# def countCheck(up):


print(upperBound(9))

# s = nums[0]
# e = nums[-1]

# while s<=e:
#     mid = s + (e-s)//2

#     up = upperBound(mid)
    
#     cnt = countCheck(up)