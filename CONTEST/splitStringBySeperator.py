words = ["one.two.three","four.five","six"]


separator = "."
s = ""
for i  in range(len(words)):
    s+=words[i]+ separator
    

s = s[:-1]

words = s.split(separator)

i = 0
while i<len(words):
    if not words[i]:
        words.pop(i)

    else:
        i+=1

print(words)