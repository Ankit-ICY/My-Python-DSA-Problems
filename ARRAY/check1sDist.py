nums = [1,0,0,1,0,1]
k = 2

x = -1

for i in range(len(nums)):
    if nums[i]==1 and x==-1:
        x = i

    elif nums[i] == 1:
        a = i-x-1
        if a>=k:
            x = i
            continue
        else:
            print(False)
            break

