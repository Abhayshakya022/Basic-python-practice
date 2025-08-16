#Set
#Set is the collection of the unordered items.
#Eech element in the must be unique & mutable.
#set of element is immutables.
#Do not Duplicate values in set

collection={1,2,2,"hello","word",4,5}
print(collection)
print(type(collection))
print(len(collection))

#empty set; syntax
collection =set()
collection.add(9)
collection.add(12)
collection.add("india is great")
#collection.remove()
#collection.clear()
print(type(collection))
print(len(collection))
print(collection)


#set.add() method
collection=set()
collection.add(1)#set.add()
collection.add(2)
collection.add("apna ghar")
collection.add((1,2,3,4,"vikey"))
print(collection)


#set.remove() method

collection=set()
collection.add(6)
collection.add(8)
collection.add("rohit")
collection.add(("rohan"))
collection.remove("rohan")#set.remove()
print(collection)





#set.pop() method
collection={"hello","great","kahli","xyz","abcd"}
print(collection.pop())
print(collection.pop())#set.pop()
print(collection.pop())
print(len(collection))



#set.clear()
collection =set()
collection.add(9)
collection.add(12)
collection.add("india is great")
collection.remove(12)
collection.clear()#set.clear() 
print(type(collection))
print(len(collection))
print(collection)




#set.union(set2) combines both set values & return new
set1= {1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1)
print(set2)



#set.intersection(set2)
#combines common values & return new.

a={4,8,6}
b={6,7,8}
print(a.intersection(b))