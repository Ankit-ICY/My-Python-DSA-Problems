ans = [0]
def solve(num,dp):
    if num > h:
        return

        last = num % 10        
        
        if num>=l and num<=h:
            ans[0] +=1
        if last> 0:
            solve(num*10 + last-1,dp)

        if last<9:
            solve(num*10 + last + 1,dp)

    return ans[0]


low = "101"
high = "342"

l = int(low)
h = int(high)
dp= {}
cnt = 0
for i in range(1, 10):
    fin = solve(i , dp)

print(fin)