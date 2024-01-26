def solve(digits , n , ind,s):

    if ind>=len(digits):
        return 0
    

   
    if int(s + digits[ind]) < n:
        x1 = 1 + solve(digits , n , ind,s + digits[ind])
        
        x2 = solve(digits , n , ind+1,s)
        x = x1 + x2
    else:
        x = solve(digits , n , ind+1,"")

    return x


digits = ["1","3","5","7"]
n = 100


ind = 0
dp = {}
print(solve(digits , n , ind,""))