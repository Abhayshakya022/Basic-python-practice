#single line comment
'''mualti line 
comment'''
#arithmetic operators
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #reminder
print(a**b) #a^b


#Relationl operators
a= 5
b= 5  
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)



#Assignment operators
num= 12
num = num+2
print("num:",num)

#Logical operators
#not operators
#reture opposite value
print(not False)
print(not True)

#And operators

value1 =True
value2 =True

print("And operator:",value1 and value2)
#print("and operator:",(a==b)and (a>b))


# OR Operater 

val1=False
val2=True
print("OR Operator:",val1 or val2 )

#Type Conversion
a=5
b=2.2
c=a+b
print(c)


#Type Casting

a = int(4)
b=6.2
c=a+b
print(c)



#input in python
a= 2.4
a= str(a)
print(type(a))


name = input("enter your name:")
print("welcome", name)
int("4")
val = int(input("enter num:"))
print(type(val),val)