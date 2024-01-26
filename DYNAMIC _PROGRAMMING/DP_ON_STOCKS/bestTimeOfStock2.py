# #DP APPROACH
# def buySell(nums,ind,b,s,total,dp):
#     if ind ==len(nums) :
#         return 0
    
#     elif (ind,b,s) in dp:
#         return dp[(ind,b,s)]
#     #BUY
#     if ind<len(nums) and b==1 :
#         total = max(-nums[ind] +  buySell(nums,ind+1,0,1,total,dp),
#                    0 + buySell(nums,ind+1,1,0,total,dp))

#     #SELL
#     if ind<len(nums) and s==1:
    
#         total = max(nums[ind]  + buySell(nums,ind+1,1,0,total,dp),   
#                     0 +   buySell(nums,ind+1,0,1,total,dp))  

     
#     dp[(ind,b,s)] = total   
#     return total

# nums = [7,1,5,3,6,4]
# ind = 0
# b = 1
# s = 0 
# total = 0
# dp = {}
# print(buySell(nums,ind,b,s,total,dp))

# WITHOUT DP

def buySell(nums,ind,b,s,pr,bot,total,list):
    if ind ==len(nums) :
        total.append(sum(list))
        return pr
    
    #BUY
    if ind<len(nums) and b==1 :
        bot = nums[ind]
        b=0
        s=1
        buySell(nums,ind+1,b,s,pr,bot,total,list)
        b=1
        s=0
        bot-=nums[ind]
        buySell(nums,ind+1,b,s,pr,bot,total,list)

    #SELL
    if ind<len(nums) and s==1:
        s=0
        b=1
        pr = nums[ind]-bot
        list.append(pr)
        buySell(nums,ind+1,b,s,pr,bot,total,list)
        pr += nums[ind] 
        list.pop()
        s=1
        b=0
        buySell(nums,ind+1,b,s,pr,bot,total,list)


    return max(total)

nums = [7,1,5,3,6,4]
ind = 0
b = 1
s = 0
bot =0
total =[]
pr =0
list = []
print(buySell(nums,ind,b,s,pr,bot,total,list))
