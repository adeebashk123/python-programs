class person:
    def display(self):
        name="shahzan"
        print("name: ",name)
person1=person()   #constructor default will help in creating the object of that class
person1.display()  #calling the method of that class

person2=person()
person2.display()


class persons:
    def __init__(self,p_name,p_age,p_email):
        self.name=p_name
        self.age=p_age
        self.email=p_email
p1=persons("adeeba",21,"adeeba@gmail.com")
print(p1.name)        

p2=persons()
p2.name="adeeba"
p2.age=21
p2.email="adeeba@gmail.com"
print(p2.name," : ",p2.age," : ",p2.email)
 
""" #Traceback (most recent call last):
File "d:\python folder\oop.py", line 20, in <module>
    p2=persons()
       ^^^^^^^^^
TypeError: persons.__init__() missing 3 required positional arguments: 'p_name', 'p_age', and 'p_email' """