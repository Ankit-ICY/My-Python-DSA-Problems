
beginWord = "AACCGGTT"
endWord = "AAACGGTA"
wordList = ["AACCGGTA","AACCGCTA","AAACGGTA"]
n = len(wordList)
distance ={}
visited = {}
for i in range(-1,len(wordList)):
    if i == -1:
        if beginWord not in distance:
            distance[beginWord] = 1e9
            visited[beginWord] = False

    else:
        if wordList[i] not in distance:
            distance[wordList[i]] = 1e9
            visited[wordList[i]] = False

q = [[0, beginWord]]

distance[beginWord] = 0
visited[beginWord] = True

while q:
    word = q.pop()
    step = word[0]
    w = word[1]
    if w == endWord:
        print(step)
        break
    visited[w] = True                    
    for i in range(n):
        count = 0
        if not visited[wordList[i]]:
            for j in range(len(w)):
                if wordList[i][j] == w[j]:
                    count +=1

            if count == len(w)-1:
                match = wordList[i]
                if step + 1 < distance[match]:
                    distance[match] = step +1
                    q.append([step+1 , match]) 
            



# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog"]
# n = len(wordList)
# s = ""
# visited = {}
# distance = {}
# adj = {}

# for i in range(-1, len(wordList)):
#     if i==-1:
#         visited[beginWord] = False
#         distance[beginWord] = 1e9
#     if i>-1:
#         visited[wordList[i]] = False
#         distance[wordList[i]] = 1e9
#     count = 0
#     for j in range(len(wordList)):

#         if wordList[i]==wordList[j] :continue
#         if i==-1:
     
#             for k in range(len(beginWord)):
#                 if beginWord[k] == wordList[j][k]:
#                     count+=1

#             if count == len(beginWord)-1:
#                 if beginWord not in adj:
#                     adj[beginWord] = [wordList[j]]
#                 else:
#                     adj[beginWord].append(wordList[j])

#         else:
#             count = 0
#             for k in range(len(wordList[i])):
#                 if wordList[i][k] == wordList[j][k]:
#                     count+=1


#             if count == len(wordList[i])-1:
#                 if wordList[i] not in adj:
#                     adj[wordList[i]] = [wordList[j]]
#                 else:
#                     adj[wordList[i]].append(wordList[j])

# for i in range(len(wordList)):
#     if wordList[i] not in adj:
#         adj[wordList[i]] = []



# # print(adj)
# q = [[1, beginWord]]
# distance[beginWord] = 0
# while q:
#     word = q.pop(0)
#     dist = word[0]
#     w = word[1]
#     visited[w] = True   
#     for i in adj[w]:
#         if dist + 1 < distance[i] and not visited[i]:
#             distance[i] = dist + 1
#             q.append([distance[i], i] )


            

# print(distance)


