intervals = [[1,5]]

new= [2,3]

intervals.sort()
ans = []
done = 0
i = 0
while(i<len(intervals)):
    a =[]
    if new == intervals[i]:
        break

    elif done==0 and new[0] <= intervals[i][1] and new[1]>=intervals[i][0] :
        a.append(min(intervals[i][0] , new[0]))
        i = i+1
        while(i<len(intervals) and new[1]>=intervals[i][0]):
            i+=1

        a.append(max(intervals[i-1][1] , new[1]))
        done =1
        ans.append(a)
        continue
    else:
        ans.append(intervals[i])
    i+=1

if done==0:
    ans.append(new)
print(ans)




[1,5] [0,3]    

[1,5] [ 0,0]