nums = ["23:59","00:00"]
nums.sort()


t1 = nums.pop(0)
t2 = nums.pop(0)


temp = "23.60"
if t1 == "00:00":
    t1 = temp
if t2 == "00:00":
    t2  = temp


if ":" in t1 :
    t1 = t1.replace(":", ".")

if ":" in t2:
    t2 = t2.replace(':' , '.')


t1= int(t1)
t2= int(t2)

ans = abs(t1-t2)

ans = str(ans)

sol = ""
for i in range(len(ans)-1,-1,-1):
    if ans[i] == ".":
        break
    else:
        sol = ans[i] + sol

print(sol)