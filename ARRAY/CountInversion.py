def merge(nums,i,mid,j):
    left = i
    right = mid+1
    ans = []
    count = 0
    while left <=mid and right<=j:
        if nums[left] > nums[right]:
            
            count += (j - right + 1)
            ans.append(nums[left])
            
            left+=1
        else:
            ans.append(nums[right])
            right+=1


    while left<mid+1:
        ans.append(nums[left])
        left+=1

    while right<=j:
        ans.append(nums[right]) 
        right+=1

    
    for x in range(len(ans)):
        nums[i] = ans[x]
        i+=1
        

    return count



def mergeSort(nums,i,j):
    count = 0
    if i>=j:
        return count
    
    mid = i + (j-i)//2
    
    count += mergeSort(nums,i,mid)
    count += mergeSort(nums,mid+1,j)
    count += merge(nums,i,mid,j)
    
    return count


nums = [2, 4, 1, 3, 5]


i = 0
j = len(nums)-1


for i in range(len(nums)):
    nums[i] = nums[i]

i = 0

print(mergeSort(nums,i,j))
