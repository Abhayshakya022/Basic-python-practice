#Dictionaries are used to store data values in key:value pairs.
#they are unordered, mutable(chanagable) & don't allow duplicaton.

student={
    "name":"abhay",
    "cgpa":9.4,
    "marks":[66,76,45,96]
}
print(student)


#second Example

info={
    "name1":"Ram",
    "subject":["python","java","mysql"],
    "topic":("dictionary","list"),
    "age":112,
    "is don":True
    
    
}


info["name1"]= "Sayam"
info["city"]="agar"


print(info)
print(info["subject"])
print(info["topic"])



#Null_Dictionary

up={}
up["name"]= "agra"
up["State"]= "utter perdash"
print(up)


#Nested Dictionaries
student={
    "name":"xyz",
    "subject":{
        "html":28,
        "java":56,
        "python":63,
    }
}
print(student)
print(len(list(student["subject"])))


#Dictionary Method
#myDict.keys()
#return all key
student={
    "name":"abc",
    "totalNo":"450",
    "age":156
}
print(student.keys())

#myDict.values()
#return all values 
student={
    "name":"india",
    "big":"large",
    11:"cuntery"
}
print(student.values())



#my.items()
#return all (key:values) pairs as tuples

student={
    "name":"karan",
    "age":15,
    "marks":(12,56,23,5),
    "subject":{
        "html":456,
        "java":564,
        "python":2358,
    }
    }
print(student.items())



#myDict.get(key)
#return the key according to value

emply={
    "name":"sumit",
    "age":24,
    "city":"agar",
    "work":{
        "no1":"ac plant",
        "no2":"ac repyar",
    }
}
print(emply.get("age"))



#myDict.update(newDict)
#insert the subject item to the dictonary

worker={
    "name":"rohit",
    "age":27,
    "post":"manager",
    "buyer":{
        "item1":"10 phone",
        "item2":"5 spiker",
        
    }
}
worker={"city":"agra","state":"up"}
worker.update(worker)

print(worker)
print(type(worker))

#null dict
collection={}
collection["name"]="Damun"
print(type(collection))
print(collection)