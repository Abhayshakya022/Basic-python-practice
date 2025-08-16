#TUPLE METHODS

tup=(2,5,3,5,5,8,6)
print(tup[2])
#print(tup.index(3))


a=(2,5,3,5,5,8,6)
print(type(a))
print(a[2:6])




#returns index of first occurrence
tup=(2,5,3,5,5,8,6)
print(type(tup))
print(tup.index(5))


#returns index of first occurrence
num=(2,8,6,2,6,2,2)
print(type(num))
print(num.count(2))


#list contains a palindrome of elements(hint: use cpoy:)

list1= [1,2,3,2,3]
list1=list1.copy()
list1.reverse()
if(list1==list):
     print("palindrome")
else:
      print("no palindrome")
    
    
    #code ex
    
lista=["m","a","a","m"]
lista=lista.copy()
lista.reverse()
if(lista==lista):
     print("palindrome")
else:
      print(" no palindrome")
      
      
      
      
  
  #    count tne number of student with the "A" greade in the following tuple
          #["C","D","A","A","B","B","A"]
      
grade3=("C","D","A","A","B","B","A")
print(grade3.count("A"))
      
      
      #Store the above values in a list & sort them from "A","D".
      
grade1=["C","D","A","B","z","e"]
grade1.sort()
print(grade1)


# the user to enter names their 3 favarete movies & store them in a list

movies=[]
movies.append(input("enter 1st movie : "))
movies.append(input("enter 2nd movie : "))
movies.append(input("enter 3rd movie :"))
print(movies)