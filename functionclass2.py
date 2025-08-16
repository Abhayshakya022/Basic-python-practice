def helloindia():
    print("india")
output= helloindia() 
print(output)
    
 
 
 # Q 1 print the length of a list.(list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbia","chennai"]
heroes=["thor","iranman","captain"]
def citieslen(list):
    print(len(list))
    
citieslen(cities)
citieslen(heroes)


# Q 2 print tne element of a list in a single line.(list is the parameter)
heroes=["thor","iranman","captain"]
def hero (list):
    for item in list:
        print(item, end=" ")
        
print(heroes)        



#Q 3 average of 3 numbers 
def avgnum(a,b,c):
        sum = a+b+c
        avg = sum /3
        print(avg)
        return avg
avgnum(55,59,57) 



# Q 4 find the factorial of n. (n is the perameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
        
cal_fact(5)

        
        
      
# Q 5 Convert USD to INR.
def converter(usdval):
    inrval = usdval*83
    print(usdval,"USD Value=", inrval,"INR")    
         
converter(73)           
    
    
    
#input by user function number return even, odd number
def check_even_odd():
    num= int(input("enter a number="))
    if num % 2==0:
       print(num,"is number even")
    else:
        print(num,"is numder odd")
        
check_even_odd()        


#Recursion
#when a function calls ifself repeatendly
#recursion function
def show(n):
    if(n==11):
        return
    print(n)
    show(n+1)
 #   print("end")
show(1)


#Recursion example 2
def fact(n):
    if(n==0 or n==1): 
        return 1
    return fact(n-1)*n
print(fact(5))#1*2*3*4*5=120


#Q 1. write a recursive function to calculate the sum of first n natural numbers.
def numsum(n):
    if(n==0):
        return 0
  #  print(n)
    return numsum(n-1) + n
sum= numsum(5)
print(sum)#output= 1+2+3+4+5=15


#Q 2. write a recursive function to print all element in a list
# Hint: use list & index as parameters.

def printlist(list, idx):
    print(list[idx])
    printlist(list,idx+1)
    
fruits = ["apple","litchi","mango","banana"]
print(fruits)    
