def boolCheck(board,ind,i,j,dp,word,map,ans):
  
    if ind==len(word):
        return True


     
    if i>=len(board) and j>=len(board[0]) and ind!=len(word):
        return False


    else:
        #DOWN
        if i+1<len(board) and not map[i+1][j] and board[i+1][j] == word[ind]:
            map[i+1][j] = True
            dp[(i,j,ind)] =  boolCheck(board,ind+1,i+1,j,dp,word,map,ans)
            map[i+1][j] = False
        #RIGHT
        if j+1<len(board[0]) and  not map[i][j+1] and board[i][j+1] == word[ind]:
            map[i][j+1] = True
            dp[(i,j,ind)]= boolCheck(board,ind+1,i,j+1,dp,word,map,ans)
            map[i][j+1] = False

        #LEFT
        if j>0 and  not map[i][j-1] and board [i][j-1] == word[ind]:
            map[i][j-1] = True
            dp[(i,j,ind)] =  boolCheck(board,ind+1,i,j-1,dp,word,map,ans)
            map[i][j-1] = False
            
        
        #UP
        if i>0 and  not map[i-1][j]  and  board [i-1][j] == word[ind]:
            map[i-1][j]  = True
            dp[(i,j,ind)] = boolCheck(board,ind+1,i-1,j,dp,word,map,ans)
            map[i-1][j]  = False
    
    return ans  
    
    

board = [ ["A","B","C","E"]
         ,["S","F","C","S"]
         ,["A","D","E","E"]]
word = "ABCCED"

map =[]
ans = []
for  i in range(len(board)):
    a =[]
    for j in range(len(board[0])):
        a.append(False)
    map.append(a)

sin =0         
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == word[0]:
            map[i][j]  = True
            if 1 in boolCheck(board,1,i,j,{},word,map,[]):
                print(True)
                sin =1
                break
            
        map[i][j] = False
    if sin==1:
        break

