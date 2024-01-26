def merge(nums,i,mid,j):
    left = i
    right = mid+1
    ans = []
    count = 0
    for k in range(i , mid+1):
        while x<=j and nums[k]> 2 * nums[x]:
            x+=1
        count += 1


    while left <=mid and right<=j:
        if nums[left] < nums[right]:
            # for x in range(right , j +1):
            #     if nums[left] > 2 * nums[x]:
            #         count += (j - x + 1)
            #         break
            ans.append(nums[left])
            
            left+=1
        else:
            if nums[left] > 2 * nums[right]:
                count += (j - right + 1)
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


nums =[2,4,3,5,1]


i = 0
j = len(nums)-1



i = 0

print(mergeSort(nums,i,j))

