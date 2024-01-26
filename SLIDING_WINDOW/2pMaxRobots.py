time = [19,63,21,8,5,46,56,45,54,30,92,63,31,71,87,94,67,8,19,89,79,25]

cost =[91,92,39,89,62,81,33,99,28,99,86,19,5,6,19,94,65,86,17,10,8,42]

budget = 85
count= 0
i = 0
sum = 0
sin = 0
j = 0
ans = 0
while(j<len(cost)):
    if sin == 0:
        count+=1
        sum+=cost[j]
        maxi = max(time[i:j+1])
        total = (((j-i)+1)*sum) + maxi
    if total<=budget:
        sin = 0
        j+=1
        ans = max(count,ans)

    else:
        sin = 1
        sum-=cost[i]
        count-=1
        i+=1
        if i<=j:
            maxi = max(time[i:j+1])
        else:
            maxi = 0
        total = (sum*((j-i)+1)) + maxi


print(ans)