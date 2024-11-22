"""num1=int(input("enter num:"))
num2=int(input("enter num:"))
result=0
try:
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("number can't be divided by 0")
else:
    print("no error",result)
finally:
    print("this is finally block")"""
    
    
my_list = [1, 2, 3, 4, 5]

try:
    tenth_element = my_list[9]
    print(tenth_element)
except IndexError as e:
    print("Error: Attempted to access an index that is out of range.")
    print(f"Exception message:",e)