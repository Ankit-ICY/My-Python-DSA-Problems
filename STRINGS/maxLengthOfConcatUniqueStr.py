ans = 0
def solve(nums,dic,ind,flag):
    global ans
    if ind>=len(nums):
        ans = max(len(dic) , ans)
        return 0

    for i in range(len(nums[ind])):
        if nums[ind][i] in dic or nums[ind][i] in nums[ind][i+1:]:
            flag =1
            break

    if flag == 0:
        for i in range(len(nums[ind])):
            dic.append(nums[ind][i])

        solve(nums,dic,ind+1,flag)
        for i in range(len(nums[ind])):
            dic.pop()
        solve(nums,dic,ind+1,flag)

    else:
        solve(nums,dic,ind+1, 0)
    ans = max(len(dic) , ans )

    return 



nums = ["cha","r","act","ers"]

dic = []


solve(nums,dic,0 , 0)
print(ans)