stack = []
target = [1,2,3]
n = 3
nums= []
for i in range(1,n+1):
    nums.append(i)
# [1,3]
# [1,2,3]
i=0
j = 0
while(i<len(target)):
    if target[i]== nums[j]:
        stack.append('Push')
        i+=1
        j+=1

    elif target[i]!= nums[j]:
        stack.append('Push')
        stack.append('Pop')
        j+=1



print(stack)


class Solution:
    def buildArray(self, target, n):
        num= 1
        stack  =[]
        i=0
        while(i<len(target)):
            stack.append('Push')
            if target[i]== num:
                i+=1

            else:
                stack.append('Pop')

            num+=1


        return stack
    
