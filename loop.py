#name = "xyz"
#while name:
   # print("nmae")




i = 5
while i >=1:
    print(i)
    i -=1
    print("loop ended")
    
    
    #print numbers form 1 to 100. 
    
num =1
while num <=100:
        print(num)
        num +=1
        
        
    #print numbers from 100 to 1.
    
    
num =100
while num >=1:
        print(num)
        num -=1
        
        
        
    # print the multiplication table of a nunber n.
    
n=int(input("enter number : "))
i=1
while i<=10:
           print(n*i)
           i+=1
           
           
  #print the elements of the following list usings a loop:
  #[1,4,9,16,25,36,49,64,81,100]       
    
nums = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index <len(nums):
    print(nums[index])
    index +=1
    
    
    
    state = ["agra","dehli","noida","gaziabad"]
index = 0
while index <len(state):
    print(state[index])
    index += 1
    
    
    
    
    #Search for a number x in this tuple using loop:
     #(1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,16,25,36,49,64,81,49,100)
x = 49
i = 0
while i < len(nums):
    if(nums[i]==x):
        print("found at index",i)
    i +=1
   
   
   
   #Break: used to terminate the loop when encountered.
   
num=(1,4,9,16,25,36,49,64,81,49,100) 
x=49
i=0
while i < len(num):
   if(num[i]==x):
         break
   print("found at idx: ",i)
   i +=1
   
   
   #Coutinue: terminates execution in the current iteration 
   # & continues executon of the loop with the next iteration.
   
   
   i = 0
   while i<=5:
       if(i==3):
           i+=1
           continue
       print(i)
       
       i+=1
       
       
#print ODD number


  
   i = 1
   while i<=10:
       if(i%2 ==0):
           i+=1
           continue
       print(i)
       
       i+=1
       
       
       #print even number
       #while i<=10:
       # if(i%2 !=0):
      #     i+=1
      #  continue
      # print(i)
       
      # i+=1