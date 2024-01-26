arr =[1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
m = 2
n = 11
mcount = 0
ans = 0
count = 0

j = 0
for i in range(n):
    if arr[i]==1:
        count+=1
    
    elif arr[i] == 0 :
        count+=1
        mcount+=1
        

    if mcount>m:
        while mcount>m:
            if arr[j]==0:
                mcount-=1
            count-=1  
            j+=1

        
    ans = max(ans,count)
    
print(ans)