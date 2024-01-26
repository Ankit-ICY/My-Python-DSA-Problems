dp = {}
def solve(nums1,nums2,i,j):
    if i>=len(nums1) or j>=len(nums2):
        return 0
        
    e1 = nums1[i]
    e2 = nums2[j]

    if (i,j) in dp:
        return dp[(i,j)] 

    x1  = solve(nums1,nums2,i+1,j)
    x2 = e1 * e2 + solve(nums1,nums2,i+1,j+1)
    x3 = solve(nums1,nums2,i,j+1)

    x = max(x1,x2,x3)
    dp[(i,j)] = x
    return x

nums1 = [-5,-1,-2]
nums2 = [3,3,5,5]
i=0
j=0

print(solve(nums1,nums2,i,j))

