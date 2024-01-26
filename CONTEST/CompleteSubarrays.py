from collections import Counter

nums = [1,3,1,2,2]
n = len(nums)

count = len(set(nums)) 
c = 0
d = Counter()

j = 0

for i in range(n):
    d[nums[i]] += 1

    while len(d) >= count:
        c += n - i

        d[nums[j]] -= 1
        if d[nums[j]] == 0:
            del d[nums[j]]
        j += 1

print(c)
# nums = [5,5,5,5]
# n = len(nums)

# from collections import Counter

# dic = Counter(nums)
# count = len(dic)
# c = 0
# d = {}

# for i in range(n):
#     d = {}
#     if nums[i] not in d:
#         d[nums[i]] = 1
#     else:
#         d[nums[i]] += 1

#     if len(d) >= count:
#         c+=1
#     for j in range(i+1,n):
#         if nums[j] not in d:
#             d[nums[j]] = 1

#         else:
#             d[nums[j]]+=1

#         if len(d) >= count:
#             c+=1


# print(c)