class TrieNode:
    def __init__(self) :
        self.children = [None]*26
        self.eow = False
    

class Trie:
    def __init__(self) :
        self.word_count = {}
        
    

    def countNodes(self,root):
        
        if  not root:
            return 0

        count = 0

        for i in range(26):
            if root.children[i] != None:
                count +=  self.countNodes(root.children[i])
           
        

        return count + 1
    
    def insert(self,word ,root):
        for i in range(len(word)):
            ind = ord(word[i])-ord("a")
            if root.children[ind] == None:
                root.children[ind] = TrieNode()
            
            if i==len(word)-1:
                if root.children[ind].eow == True:
                    self.word_count[word] +=1

                else:
                    root.children[ind].eow = True
                    self.word_count[word] =1



            root = root.children[ind]


    def search(self, key,root):
        for i in range(len(key)):
            ind = ord(key[i])-ord("a")
            if root.children[ind] == None:
                return False

            
            if i==len(key)-1:
                if root.root.children[ind].eow == False:
                    return False
                
            root = root.children[ind]
            

        return True

            
            
    def startsWith(self,root,prefix):
        for i in range(len(prefix)):
            ind = ord(prefix[i])-ord("a")
            if root.children[ind] == None:
                return False

            root = root.children[ind]


        return True


    def longestWord(self,curr,string, root):
        for i in range(26):
            if root.children[i]!= None and root.children[i].eow == True:
                curr += chr(i + ord('a'))
                if len(string[0]) <len(curr):
                    string[0] = curr
                self.longestWord(curr,string, root.children[i])
                curr = curr[:-1]

        return string

    def isEmpty(self,root):
        for i in range(26):
            if root.children[i] :
                return False
            
        return True

    def delete(self,key,root , index):
        if index == len(key):
            if root.eow :
                root.eow = False
            else:
                return root
        
            if self.isEmpty(root):
                del root
                root = None
                return root
        
        ind = ord(key[index]) - ord('a')
        if root.children[ind]:
            root.children[ind] = self.delete(key,root.children[ind], index+1)
        else:
            return True

        if self.isEmpty(root) and not root.eow:
            del root
            root = None
            return root


        return root
    

    def countWordsStartingWith(self, root, word):
        for i in range(len(word)):
            ind = ord(word[i]) - ord('a')
            if root.children[ind] :
                root = root.children[ind]
            else:
                return 0
        count = 0
        
        for i in range(26):
            if root.children[i]:
                count+=1

        return count

    def count_Total_word(self,root,word):
        if word in self.word_count:

            return self.word_count[word]
        else:
            return 0





wordList = ["there" , "a" , "their" , "any" ]
root = TrieNode()
ob = Trie()
# for i in range(len(wordList)):
#     ob.insert(wordList[i] , root)

# print(ob.search("any" , root))

# prefix = "ax"
# print(ob.startsWith(root,prefix))
# print(ob.countNodes(root))

words = ["apple","banana", "banana", "apple" , "apple"]

for i in range(len(words)):
    ob.insert(words[i] , root)

# print(ob.longestWord("",[""], root))

# print(ob.delete("app", root, 0))
word = "app"

print(ob.count_Total_word(root,word))

# print(ob.countWordsStartingWith(root, word))