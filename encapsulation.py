class employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        
    def set_salary(self,salary):
        self.salary = salary
    def get_salary(self):
        return self.salary
emp1=employee("adeeba",34000)
emp1.set_salary(35000)
print(emp1.get_salary())