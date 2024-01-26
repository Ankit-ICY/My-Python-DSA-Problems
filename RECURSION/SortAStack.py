def insert(stack,temp):
    if len(stack)==0 or stack[-1] >=temp:
        stack.append(temp)
        return
    else:
        val = stack[-1]
        stack.pop()
        insert(stack,temp)
        stack.append(val)
    return  stack

def sort(stack):
    if len(stack)==1:
        return
    

    temp = stack[len(stack)-1]
    stack.pop()
    sort(stack)
    insert(stack,temp)
    return stack

stack = [3,2,1]
print(sort(stack ))