def findeven():
    numbers=[1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i %2==0:
            print(i)
            
findeven()
number=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x%2==0,number))
print(result)

#oddnumber
number=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x%2!=0,number))
print(result)



#filtering positive number by using filter and lambda combination[-10,-5,0,5,10,15]
number=[-10,-5,0,5,10,15]
result=list(filter(lambda x:x>=0,number))
print(result)

#filter out the string with more than 3 characters["hi","hello","a","world","cat"] by using lambda function
string=["hi","hello","a","world","cat"]
result=list(filter(lambda x:len(x)>=3,string))
print(result)