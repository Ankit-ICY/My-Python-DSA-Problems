n = 10
chess =[
    [13, 2],
[2 ,4],
[2 ,12],
[19 ,17],
[3 ,17],
[3 ,17],
[20 ,15],
[12 ,5],
[12 ,9],
[11 ,1]]


dic = {}
for cell in chess :

    left = cell[0] + cell[1]
    right = cell[0] - cell[1]

    if left not in dic:
        dic[left]=1 

    else:
        dic[left]+=1


    if right not in dic:
        dic[right]=1
    else:
        dic[right]+=1
clash = 0

for count in dic.values():
    if count > 1:
        clash += count - 1

    elif count >2:
        clash += count

print(clash)  # Output: 1





