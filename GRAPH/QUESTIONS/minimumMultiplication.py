nums  =[2,5,7]
start = 3
end = 30
mod = 1e3
q = [[start , 0]]
flag = 0
distance = [1e9]*1000
distance[start] = 0 
while(q):
    node = q.pop(0)
    num = node[0]
    mulCount = node[1]

    for  i in range(len(nums)):
        n = (num * nums[i])%mod
        if mulCount + 1 < distance[int(n)]:
            distance[int(n)] = mulCount+1
            if n == end:
                flag = 1
                print(distance[int(n)])
                break
            q.append([n, mulCount+1])

    if flag == 1:
        break