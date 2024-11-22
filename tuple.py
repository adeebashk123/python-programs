data=()
print(data)
data=(1,2,3,4,5)
print(data)
data=(12,"adeeba","mumbai",400070)
print(data)

data1=(11,12,35,45,35,11)
print(data1)
print(data1[3])

print(data1[0]+data1[5])


tuple1=(110,210,220)
tuple2=(300,400,500)
print(tuple1+tuple2)
tuple3=tuple1+tuple2
print("the result: ",tuple3)

#repitition *-> by what
tuple4=(1,2,3,4,5)*4
print(tuple4)

#important methods of tuple
tuple5=(123,124,125,126,123,132,125)
print(tuple5.count(123))
print(tuple5.index(126))

#find out the max value the tuple contains 
tuple6=(89,56,99,34,101,73,123,45,56)
#use for loop  dont use max function find max value
max_val=tuple6[0]
for i in tuple6:
    if i>max_val:
        max_val=i

print(max_val)

max_val=tuple6[0]
for i in tuple6:
    if i<max_val:
        max_val=i

print(max_val)

#find the count of a number whih is repeated in a tuple. the tuple is 89,56,99,89,34,101,34,73 use for loop and take input from user
tuple7=(89,56,99,89,34,101,34,73)
print("enter the number:")
count=0
num=int(input())
for i in tuple7:
    if i==num:
        count+=1
print(count)

student=(10,"adeeba","adeeba@gmail.com","mumbai")
id,name,email,city=student
print("id: ",id)
print("name: ",name)
print("email: ",email)
print("city: ",city)

id2=student
print("id:",id2)



        
        

    
        
        