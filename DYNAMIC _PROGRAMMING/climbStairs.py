def climbstairs(i,dp,n):
        if i>n:
            return 0
        
        if i==n:
            return 1
            
        if (i) in dp:
            return dp[(i)]
            
        x1 = climbstairs(i+1,dp,n)
        x2 = climbstairs(i+2,dp,n)
        dp[(i)] = x1 + x2
        
        return dp[(i)]


n = 4
print(climbstairs(0,{},n))
