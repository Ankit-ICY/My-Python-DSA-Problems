start = [12 ,6 ,16 ,12 ,6 ,9 ,16 ,6, 17 ,5]
end = [17 ,13 ,16 ,18 ,17 ,10 ,18 ,12 ,18 ,11]
n = 10
meeting = []
for i in range(n):
    a = []
    a.append(start[i])
    a.append(end[i])
    meeting.append(a)

meeting.sort(key = lambda x: x[1]) 

endMeet = meeting[0][1]
meet = [1]

for i in range(1,n):
    if meeting[i][0]>endMeet:
        meet.append(i+1)
        endMeet = meeting[i][1]


print(meet)