arr = [ 900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = 6
times = []
for i in range(n):
    times.append([arr[i] , dep[i]])


times.sort(key = lambda x: x[1])
print(times)
count = 1
stack = [times[0][1]]
for i in range(1,n):
    done = 0
    for  j in range(len(stack)):
        if times[i][0] >= stack[j]:
            stack[j] = times[i][1]
            done =1 
            break
        else:
            continue

    if done==0:
        count+=1
        stack.append(times[i][1])
    
print(len(stack))