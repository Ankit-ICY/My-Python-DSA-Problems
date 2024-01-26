

def findbase(n, base):
    temp = ""
    while n > 0:
        temp += str(n%base)
        n = n//base

    return temp[::-1]
n = 9

for i in range(2, n-1):
    
    s = findbase(n , i)
    if s != s[::-1]:
        print(False)
        break



