#generate a list from an existing list by adding 100 to every value of the list
number=[1,2,3,4,5,6,7,8,9]
result=set(map(lambda x:x+100,number))
print(result)

number=[1,2,3,4,5,6,7,8,9]
result=list(map(lambda x:x**2,number))
print(result)

#from a given list of number double the even numbers by using lambda,filter,map, list
number=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x%2==0,number))
result1=(list(map(lambda x:x**2,result )))
print(result1)