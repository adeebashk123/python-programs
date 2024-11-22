"""class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary=salary
    def display(self):
        print(self.name," : ",self.age," : ",self.salary)
    def acceptemp(self):
        self.name = input("Enter Employee Name: ")
        self.age=int(input("enter value:"))
        self.salary=int(input("enter sal:"))
        
emp1=employee("shahzan",12,40000)
emp1.display()

emp1.acceptemp()
emp1.display()"""


class Product:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.price = 0.0
        self.qty = 0
    def get_product_details(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
    def display_product(self):
        print(self.id,":",self.name,":",self.price,":",self.qty)

product1 = Product(101)
product1.get_product_details("Laptop", 1500.00, 10)
product1.display_product()
