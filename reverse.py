from math import floor
num=int(input("enter value:"))
rev=0
rem=0
temp=num
while temp>0:
    rem=temp% 10
    rev=rev*10+rem
    print("temp= ",temp,"rem= ",rem,"rev= ",rev)
    temp=floor(temp/10)
    
#num1=input("enter a number:")
if rev==num:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
print("reverse:",rev)
