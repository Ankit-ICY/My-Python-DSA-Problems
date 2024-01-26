


s = "}}}}}{"

# stack = []
# count = 0
# for i in range(len(s)-1,-1,-1):
#     if s[i] == "}" :
#         if stack and stack[-1] == "}":
#             stack.pop()
#             count+=1
#         else:
            
#             stack.append(s[i])
        
#     else:
#         if stack and stack[-1] == "{":
#             stack.pop()
        
#         count+=1
        

#         stack.append(s[i])

# count += len(stack)//2
# print(count)

s = "}}}}}{"

stack = []
cost = 0

for char in s:
    if char == '{':
        stack.append(char)
    elif char == '}':
        if stack and stack[-1] == '{':
            stack.pop()
        else:
            cost += 1


cost += (len(stack))  # Consider each remaining closing bracket as a separate cost

print(cost)