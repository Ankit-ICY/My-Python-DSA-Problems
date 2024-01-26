nums1 =  [2,4]
nums2 = [1,2,3,4]
stack = []

dic ={}
dic[nums2[-1]] = -1
for i in range(len(nums2)-1 , -1 ,-1):
    x = nums2[i]

    if len(stack)>0 and nums2[i]<stack[-1]:
        dic[nums2[i]] = stack[-1]

    elif len(stack)>0 and nums2[i]>stack[-1]:
        while len(stack)!=0 and nums2[i]>stack[-1]:
            stack.pop()

        if len(stack)==0:
            dic[nums2[i]]= -1
        else:
            dic[nums2[i]] = stack[-1]
        
    stack.append(x)


for i , j in dic.items():
    if i in nums1:
        ind = nums1.index(i)
        nums1[ind] = j

print(nums1)