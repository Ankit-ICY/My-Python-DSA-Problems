nums =  [1,3,4,2,2]

slow = 0
fast = 0
n = len(nums)
while True:
    if slow<n-1:
        slow +=1
    elif slow==n-1:
        slow = 0

    if fast<n-2:
        fast+=2
    elif fast ==n-2:
        fast =0
    elif fast==n-1:
        fast = 1        
    
    if slow != fast and nums[slow] == nums[fast]:
        print(nums[slow])
        break