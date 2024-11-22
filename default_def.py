def greeting(message="hello all........"):
    print("the output is:",message)
greeting()
greeting("welcome home")

def addition(num2,num1=100):
    result=num1+num2
    print(result)
addition(10)

#*arguments means any lenght
def greet(*args):  #implicity from a tuple
    print(*args)
greet(1,2,3,4,5,6)


#unpack operation are not contain directly
def greetings(*args):
    print(*args)
greetings("hello","welcome","mumbai")