start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
n = 6
meeting = []
for i in range(n):
    a = []
    a.append(start[i])
    a.append(end[i])
    meeting.append(a)

meeting.sort(key = lambda x: x[1]) 

endMeet = meeting[0][1]
count = 1
for i in range(1,n):
    if meeting[i][0]>endMeet:
        count+=1
        endMeet = meeting[i][1]


    
print(count)