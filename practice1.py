#	Q. you have to determine if the string contain all unique character. 
# It simply means there has to be no duplicate character in the given string
#use for loop and input
strdata=input("enter a string value:")
message=True
for i in range(len(strdata)):
    for j in range(i+1,len(strdata)):
        if (strdata[i]==strdata[j]):
            message=False
      
print(message)