#create list
marks=[21,55,656,5656,85,]
print(type(marks))


student=["aman",23,"agra"]
print(student[0])
student[0]="ram"
print(student)


#list Slicing
marks=[45,78,56,35,42,48]
print(marks[1:3])


#nesting List Slicing
marks=[85,45,75,96,42,52]
print(marks[-5:-2])


#list methods
#method 1

list=[2,3,1,4]
list.append(5)
print(list)

#method 2

list=[5,7,4,1,2]
list.sort()
print(list)

#method 3

list=[5,7,4,1,2]
list.sort(reverse=True)
print(list)


#method 4
list=[89,45,23,12,75]
list.reverse()
print(list)


#methods 4
list=[5,2,4,6,3]
list.insert(3,25)
print(list)


#methods 5
list=[5,2,4,6,3]
list.remove(6)
print(list)


#methods 6

list=[3,2,5,8,9]
list.pop(2)
print(list)


#copy list
list1=[1,2,3,4,5,6]
print(list1)
list2=list1.copy()
print(list2)