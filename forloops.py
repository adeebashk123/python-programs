"""cube=0
n = int(input("Enter a positive integer: "))
for i in range(1, n + 1,1):
    cube = i*i*i
    print(cube)

square=0
n = int(input("Enter a positive integer: "))
for i in range(1, n + 1,1):
    square = i*i
    print(square)"""
    
    
"""
number =int( input("Enter a number: "))
reversed_number =0
for i in number:
    reversed_number = i + reversed_number
if reversed_number==number:
    print("The number is a palindrome")
else:
   print("The number is not a palindrome")
print("Reversed number:", reversed_number)"""


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
    
num1=int(input("enter a number:"))
rev=0
for i in num1:
    rev=1+rev
if rev==num1:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
print("reverse:",rev)


"""

# Initialize an empty list
ones_list = []

# Use a for loop to append 1 to the list 50 times with an if-else condition
for i in range(50):
    if i >= 0:  # Always true in this case, but you can use any condition
        ones_list.append(1)
    else:
        ones_list.append(0)  # This part won't be executed

# Print the list
print(ones_list)"""


