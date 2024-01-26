def merge(nums,i , mid , j):
    count = 0
    ans = []
    ind1 = i 
    ind2 =mid+1

    

    while(ind1<=mid and ind2<=j):
        if nums[ind1]<nums[ind2]:
            ans.append(nums[ind1])
            ind1+=1

        else:
            ans.append(nums[ind2])
            ind2+=1


    while(ind1<=mid):
        ans.append(nums[ind1])
        ind1+=1

    while(ind2<=j):
        ans.append(nums[ind2])
        ind2+=1

    for x in range(len(ans)):
        nums[i] = ans[x]
        i+=1

def mergeSort(nums, i ,j):
    if i>=j:
        return 
    
    mid = i + (j-i)//2
    mergeSort( nums , i , mid)
    mergeSort( nums , mid+1 , j)
    merge(nums,i , mid , j)

    
nums = [2, 4, 1, 3, 5]
n = 5
i = 0

mergeSort(nums, i,n-1)

print(nums)