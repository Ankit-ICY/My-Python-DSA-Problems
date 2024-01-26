
a = "xyyyz"
b = "xzyz"
c = "zzz"
# a = "ab"
# b = "ba"
# c = "aba"


i = 0
j = 0

m = len(a)
n = len(b)

s =  ""
while i <m and j<n :
    if a[i] == b[j]:
        s += a[i]
        i+=1
        j+=1
    
    elif a[i]<b[j]:
        s += a[i]
        i+=1

    else:
        s+= b[j]
        j+=1


while i<m:
    s += a[i]
    i+=1

while j<n:
    s+=b[j]
    j+=1


m = len(s)
n = len(c)
i = 0
j = 0

ans  =""

while i <m and j<n :
    if s[i] == c[j]:
        ans += s[i]
        i+=1
        j+=1
    
    elif s[i]<c[j]:
        ans += s[i]
        i+=1

    else:
        ans+= c[j]
        j+=1


while i<m:
    ans += s[i]
    i+=1

while j<n:
    ans+=c[j]
    j+=1

print(ans)