#numeric datatypes-int,float,complex
a=10+4j
print(type(a))
#sequence data types-list,tuple,range
#Boolean type
a=""
print(bool(a))
print(type(a))
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
#list operations
#range of indexes
a=["banana","mango",24,54,True]
print(type(a))
print(a[1:4])
#insert items
a.insert(6,"false")
print(a)
#Append
a.append("swetha")
print(a)
#Extend
b=['anupama','pooja']
a.extend(b)
print(a)
#remove specific items
a.remove('pooja')
print(a)
#remove specific index
a.pop(5)
print(a)
#del the list

#clear the list
c=[1,2,3]
print(c)
c.clear()
print(c)
#sort the list
d=[3,5,1,4]
d.sort()
print(d)
#join the list
l1=[1,2]
l2=[3,4]
print(l1+l2)