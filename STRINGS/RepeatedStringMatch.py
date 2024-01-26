a = "aa"
b = "a"
str = a
repeat = len(b)//len(a)
ans = 1
i= 0
while(i<= 2 + repeat  ):
   

    if b in a:
        print(ans)
        break


    a+=str
    ans+=1


    i+=1
