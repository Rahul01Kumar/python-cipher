#Add items from one set to another
#set1={10,20,30,40}
#set2={50,60}
#set1.update(set2)
#print(set1)

#Remove Item
#myset={10,20,30}
#myset.remove(20)#when the element is not present it gives error
#myset.discard(20)#it does not give error
#myset.pop()
#print(myset)

#for i in myset:
 #   print(i)

#join the sets
#set1={'a','b','c','c','b'}
#set2={10,20,30,10,20}
#set3=set1.union(set2)
#print(set3)

x={10,20,30,40,50}
y={40,50,60,70}
#x.intersection_update(y)
#print(x)
x.symmetric_difference(y)
print(x)
print(y)

