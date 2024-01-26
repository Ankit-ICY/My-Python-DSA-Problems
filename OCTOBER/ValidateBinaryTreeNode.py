n = 5
leftChild = [0,-1,3,1,3]


rightChild =[4,3,0,1,-1]



# n = 4
# leftChild =[3,-1,1,-1]


# rightChild = [-1,-1,0,-1]


def solve(chi ,par,child):
    if child[chi] == par:
        return True

    if chi not in child:
        return False
    

    return solve(child[chi] ,par,child)



child = {}

parent = [[] for _ in range(n)]
for node in range(n):
    left  = leftChild[node]
    right = rightChild[node]
    if left!=-1:
        parent[node].append(left)


        if left not in child:
                
            if node in child and solve(node ,left,child):
                print(False)
                break

            elif left == node:
                print(False)
            child[left] = node 
            

        
        else:
            print(False)
            break

    if right!=-1:
        parent[node].append(right)

        if right not in child:
            if node in child and solve(node ,right,child):
                print(False)
                break
            child[right] = node 

      
        else:
            print(False)
            break


if len(child) != n-1:
    print(False)

    

print(child)
print(parent)