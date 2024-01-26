n= 2

seen = set()

while sum not in seen:
    seen.add(n)

    
    sum =0
    while n!=0 :
        x = n%10
        sum += x**2
        n = n//10
    
    if sum ==1:
        print(True)
        break

    n  = sum
