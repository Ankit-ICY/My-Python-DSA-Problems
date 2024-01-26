# for i in range(5):
#     # SPACES

#     for j in range(i):
#         print(" ",end="")

#     for k in range(5-i):
#         print("*",end=" ")

    
#     for l in range(i):
#         print(" ",end="")

#     print("\n",end="")


# for i in range(5):
#     # SPACES
#     for j in range(i+1):
#         print("*",end="")

#     for k in range(5-i-1):
#         print(" ",end=" ")

#     print("\n",end="")



# for i in range(4):
#     # SPACES
#     for j in range(4-i):
#         print("*",end="")

#     for k in range(i):
#         print(" ",end=" ")

#     print("\n",end="")



# row,col = int(input().strip().split())
row = int(input())
col = int(input())
for i in range(row):
    for j in range(i+1):
        print("*",end="")
    
    for k in range(col-(2*(i+1))):
        print(" ",end="")

    for l in range(i+1):
        print("*",end="")

    print("\n",end="")

