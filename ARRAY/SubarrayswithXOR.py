nums = [5, 6, 7, 8, 9]
k = 5
pre = {}
xor = 0
count = 0
for i in range(len(nums)):
    xor = xor ^ nums[i]

    score = xor ^ k
    if score == 0:
        count +=1

    if score in pre:
        count += pre[score]

    if xor in pre:
        pre[xor] +=1

    else:
        pre[xor] = 1

print(count)
