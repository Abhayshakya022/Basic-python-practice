#String

String= "india is big country.\ni live in india"
print(String)

str1= "hello"+"india"
print(str1)

str1="hello"
str2="world"
print(str1+str2)

str1="hello"
str2="bomba"
finalstr = str1+str2
print(finalstr)


#length of str
str1="hello"
len1=len(str1)
print(len1)

str2="world"
len2=len(str2)
print(len2)

finaly_str=str1+str2 
print(len(finalstr))




#Indexing
str="apna_india"
ch=str[0]
#ch=str[2]
print(ch)

#Slicing
str="apna_  india"
#ch=str[0:4]
ch2=str[5:8]
print(ch,ch2)


str ="Apple"
ch=str[-3:-1]
print(ch)


#string function Start
#str.endswith()
str="i am studying python"
print(str.endswith("thon"))

#sts.capitalize()
str="i am studying python"
print(str.capitalize())

#str.replace()
str="i am studying python"
print(str.replace("am","is"))

#str.find()
str="i am studying python"
print(str.find("am"))

#str.count()
str="i am studying am am python"
print(str.count("am"))





#WAP to input user's first name & print its length
name=input("enter your name: ")
print("length of your name is",len(name))

#WAP to find the occurrence of '$' in a String.
str="i am student $ $ $$ $"
str= str.count("$")
print(str)