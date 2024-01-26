def merge(nums,i,mid,j):
    left = i
    right = mid+1
    ans = []
    while left <=mid and right<=j:
        if nums[left][0] >= nums[right][0]:
            ans.append(nums[left])
          
            dic[nums[left][1]]+= (j-right + 1)
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
        




def mergeSort(nums,i,j):

    if i>=j:
        return
    
    mid = i + (j-i)//2
    
    mergeSort(nums,i,mid)
    mergeSort(nums,mid+1,j)
    merge(nums,i,mid,j)
    


nums = [1,9,7,8,5]


cop = nums.copy()
i = 0
j = len(nums)-1


for i in range(len(nums)):
    nums[i] = [nums[i] , i]

i = 0
dic = [0] * (j+1)
mergeSort(nums,i,j)


print(dic)