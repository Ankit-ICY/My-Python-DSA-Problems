nums = [5 ,10 ,-5]
stack = []
n = len(nums)
sin = 0
for i in range(n):
    while(stack and nums[i]<0 and stack[-1]>0):
        check = nums[i] + stack[-1]
        if check>0:
            sin = 1
            break
        elif check<0:
            stack.pop()
            
        else:
            stack.pop()
            sin = 1
            break


    if sin==0:
        stack.append(nums[i])
    else:
        sin=0

print(stack)