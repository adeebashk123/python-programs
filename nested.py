"""num1=10
for r in range(1,3,1):
    print()
    for c in range(1,3,1):
        num1+=2
        print(num1, end=" ") """

"""num1=1
for r in range(1,4,1):
    print()
    for c in range(1,4,1):
        num1=r*c
        print(num1,end=" ")"""
        
"""num2=1
for r in range(1,5,1):
    print()
    for c in range(1,5,1):
        num2="*"
        print(num2,end=" ")"""
        
num2=5
for r in range(1,5):
    print()
    for c in range(1,r+1):
        print("*",end=" ")
    
    

"""num4=2
for r in range(1,5):
    print()
    for c in range(1,r+1):
        if num4<=12:
            print(num4,end=" ")
            num4+=2
            
num5=2
for r in range(1,5):
    print()
    for c in range(1,r+1):
        if num5<=12:
            print(num5,end=" ")
            

num2=5
for r in range(5,1,-1):
    print()
    for c in range(r):
        print("*",end=" ")    """
   
num2=5
for r in range(1,5):
    print()
    for c in range(1,r+1):
        print("*",end=" ")
        for c in range(1,r+1):
            print("#",end=" ") 
    