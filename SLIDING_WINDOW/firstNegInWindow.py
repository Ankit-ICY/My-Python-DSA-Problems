nums = [-8, 2, 3, -6, 10]
k=2   
n = 5
ans = []

i =0 
j = 0
s = []
while(j<n):
    if nums[j]<0:
        s.append(nums[j])


    if j-i+1==k:
        if not s:
            ans.append(0)

        elif s[0] == nums[i]:
            ans.append(s[0])
            s.pop(0)

        else:
            ans.append(s[0])
        i+=1

    j+=1

print(ans)


# vector<long long> printFirstNegativeInteger(long long int A[],
#                                              long long int N, long long int K) {
#     int i=0,j=0;
#     list<int>ls;
#     vector<long long>ans;


#     while(j<N){
#             if(A[i]<0){
#                 ls.push_back(A[i]);
#             }
#             if(j-i+1 <K)
#             j++;
            
#             else if(j-i+1 == K){
#             if(ls.size() == 0){
#                  ans.push_back(0);
#              } 
#              else if(ls.front() == A[i]){
#                 ans.push_back(ls.front());
#                 ls.pop_front();
#             }
#             else{
#                 ans.push_back(ls.front());
#             }


#             i++;
#         }
#         j++;
#     }
#     return ans;
#  }

# # A = [-8, 2, 3, -6, 10]
# # K=2   
# # N = 5

# # i = 0
# # j = 0
# # ls = []
# # ans = []

# # while j < N:
# #     if A[i] < 0:
# #         ls.append(A[i])
  
# #     if j - i + 1 == K:
# #         if not ls:
# #             ans.append(0)
        
# #         ans.append(ls[0])
# #         elif ls[0]==A[i]
# #             ls.pop(0)

# #         if A[i] == ls[0]:
# #         i += 1

    
# #     j += 1

# # print(ans)