def reverseStack(stack):
    if len(stack) == 0:
        return
    

    ele = stack[0]
    stack.pop(0)
    reverseStack(stack)
    stack.append(ele)
    return stack

stack = [3,2,1,7,6]
print(reverseStack(stack))
