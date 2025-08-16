#store following word meanings in a python dictonary
#table : "a piece of furniture","list of facts & figure"
#cat : "a small animal"
dictionary ={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figure"]
    
}
print(dictionary)


#question 2
#you are given a list of subjects. Assume one classroom is required for subject.how many classrooms are needed by all student
#  "python","java","c++","python","javascript","java","python","java","c++","c"
subject={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(len(subject))



#enter marks of 3 subject for the user and store them in dictionary. start with an
#eempty dictioary & add one by one. use subject name as kays marks as value.

marks={}

a=int(input("enter phy: "))
marks.update({"phy" : a})

b=int(input("enter math: "))
marks.update({"math": b})

c=int(input("enter chem: "))
marks.update({"phy": c})

d=int(input("enter hin: "))
marks.update({"hin": d})

print(marks)






#Figure out a way to store 9 & 9.0 as separate values in the set.
#(you con take help of built-in data types)