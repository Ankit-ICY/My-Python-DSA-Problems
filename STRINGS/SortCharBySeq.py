s = "raaeaedere"


d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] +=1

    else:
        d[s[i]] = 1


d = dict(sorted(d.items(), key=lambda item: item[1]))
string = ""

for i , j in d.items():
    string += i*j

string = string[::-1]

print(string)