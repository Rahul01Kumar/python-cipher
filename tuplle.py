#tuple1=(10,20,30)
#del tuple1 #this del function delete the tuple 
#print(tuple1)

#in the python we can extract the values into diff vriables.this is unpacking
no=(10,20,30,40,50,60,70,80)#packing
(num1,*num2,num3)=no# no of variables should match number of items in tuple
# * function extract the no. as copied manner in list
print(num1)
print(num2)
print(num3)
