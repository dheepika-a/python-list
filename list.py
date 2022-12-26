""" list1=["mon","tue","wed","thur","fri","sat"]  
list2=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]
c=list1+list2
c.sort()
c.reverse()
s=c[0:3]
del c[0:3]
d=c+s
print(d) """

list1=["mon","tue","wed","thur","fri","sat"]  
list1.append("sun")
print(list1)

list1=["mon","tue","wed","thur","fri","sat"]  
list1.clear()
print(list1)

list1=["mon","tue","wed","thur","fri","mon"]
print(list1.count("mon"))

list1=["mon","tue","wed","thur","fri","sat"]  
list1.extend(["sun","jan"])
print(list1)

list1=["mon","tue","wed","thur","fri","sat"]  
print(list1.index("thur"))

list1=["mon","tue","wed","thur","fri","sat"]  
list1.insert(2,"deep")
print(list1)

list1=["mon","tue","wed","thur","fri","sat"]  
list1.insert(2,"deep")
print(list1)

list1=["mon","tue","wed","thur","fri","sat"]  
print(list1.pop(2),list1)

list1=["mon","tue","wed","thur","fri","sat"]  
list1.remove("mon")
print(list1)

list1=["mon","tue","wed","thur","fri","sat"]  
list1.reverse()
print(list1)

list1=["mon","tue","wed","thur","fri","sat"]  
list1.sort()
print(list1)
