def Fibo(n,dp):
    if n<=1:
        return n
    if (n) in dp:
        return dp[(n)]

    dp[(n)] = Fibo(n-1,dp) + Fibo(n-2,dp)
    return dp[(n)]

n = 3
dp ={}
print(Fibo(n,dp))