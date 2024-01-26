def merge(nums,i,mid,j):
    x = 13
    y = 82
    left = i
    right = mid+1
    ans = []
    count = 0
    q = mid+1
    for p in range(i , mid+1):
        for q in range(mid+1, j+1):
            if x<= nums[p] * nums[q] <=y:
                count+=1

        # q = mid+1
        # while q <j+1 and  x<= nums[p] * nums[q] <=y :
        #     q+=1
        #     count+=1

    
    while left <=mid and right<=j:
        if nums[left] >nums[right]:
            # if nums[left] * nums[right] >=x and  nums[left] * nums[right]  <=y:
            #     count+=1
            ans.append(nums[left])
            
            left+=1
        else:
            # if nums[left] * nums[right] >=x and  nums[left] * nums[right]  <=y:
            #     count+=1
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


nums =[6 ,9 ,4 ,15 ,3 ,11 ,13, 9 ,3 ,13 ,5 ,15 ,2 ,12 ,9 ,12 ,15]
# 6 ,9 ,4 ,15 ,3 ,11 ,13, 9 ,3 ,13 ,5 ,15 ,2 ,12 ,9 ,12 ,15

i = 0
j = len(nums)-1

# 9 ,13 ,13 ,2 ,4 ,10 ,10 ,11 ,10 ,6

print(mergeSort(nums,i,j))






# def count_pairs_within_range(nums, x, y):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         for j in range(i + 1, n):
#             product = nums[i] * nums[j]
#             if x <= product <= y:
#                 count += 1
#             else:
#                 break
#     return count

# nums = [5, 3, 7, 9, 7, 9, 7, 7]
# x = 7
# y = 19

# result = count_pairs_within_range(nums, x, y)
# print("Total number of pairs: ", result)
