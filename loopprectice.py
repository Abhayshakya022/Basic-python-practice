#wihle loop 
# the while loop repeatedly executes a block of code
# as long as a given condition remains True. it checks 
# the condition before each iteration
count =5
while count>=1:
    print(count)
    count -=1
else:
    print("while loop ended:")
    
    
    
# For loop
# The for loop in python is used to iterate over a sequence
# (such as a list,tuple,dictionary,sey,or string) and execute
# a block of code for each element in that sequence  

str=("python")
for india in str:
    print(india)
    
    
    #example 2
#range(stop)
#range(start,stop,step)
#range(start,stop,step)
for i in range(1,12,3 ):  #start, stop, step argument.
    print(i)
    
    
for i in range(5):
    print(i)
else:
    print("for loop ended")        

    
    
    
# Loop Control Statements     
# 1. pass Statement    
# 2. break Statement
# 3. continue Statement
    
    
    #pass control Statement in loop python 
    count =5 
    while count > 0:
      if count==3:
        pass
    else:
        print(count)
        count -=1