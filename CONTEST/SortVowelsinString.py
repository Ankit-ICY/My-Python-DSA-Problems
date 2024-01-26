

from heapq import heapify , heappop ,heappush

s = "lEetcOde"
vowels = ['a','e','i', 'o', 'u' ]
heap =[]
for i in range(len(s)):
    if s[i].upper() in vowels or s[i].lower() in vowels:
        heappush(heap , ord(s[i]))
    
        
ans = ""

for i in range(len(s)):
    if s[i].upper() in vowels or s[i].lower() in vowels:
        ans += chr(heappop(heap))

    else:
        ans +=s[i]

print(ans)



# print(store)

# store.sort(key = get_min)

# print(store)
# x = 0
# ans = ""
# for i in range(len(s)):
#     if s[i] in store:
#         ans += store[x]
#         x+=1
#     else:
#         ans += s[i]

# print(ans)

