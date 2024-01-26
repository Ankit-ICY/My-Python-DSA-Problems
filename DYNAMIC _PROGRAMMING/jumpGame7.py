def jumpGame(s, ind, dp ,minJump, maxJump,n):
    if ind==n-1:
        return True
    
    for i in range(ind+minJump , min(ind+maxJump+1 , n )):
        if s[i] == "0" and jumpGame(s, i, dp ,minJump, maxJump,n):
            return True
        

    return False


s = "01101110"
minJump = 2
maxJump = 3
ind = 0
n = len(s)
dp ={}
print(jumpGame(s, ind, dp ,minJump, maxJump,n))