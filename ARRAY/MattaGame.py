nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = 20

x = 1
jump = 1
while True:
    i = 0
    jump  = 2 * jump

    if jump>n:
        break


    # TO CHECK THE FIRST ELEMENT WHICH IS ALIVE
    while i< n and nums[i]== -1 : 
        i+=1


    # KILL THE RIGHT WALA ELEMENT AND JUMP TO THE ALIVE ELEMENT
    while i <n :
        if i+x<n:
            nums[i+x] = -1  
        i+=jump

    # IF LAST WALA ELEMENT IS NOT ABLE TO KILL KISI KO , 
    # THEN FIND THE FIRST ELEMENT IN ARRAY , JO KILL NAHI HUA


    if n%jump != 0:
        j = 0
        while(j<i - jump and nums[j] == -1)  :
            j+=1
    
        nums[j] = -1    
    x =x *2



print(nums)