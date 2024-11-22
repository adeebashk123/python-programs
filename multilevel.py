class Person:
    def __init__(self, name):
        self.name = name
        
    def display_person(self):
        print("Name:", self.name)

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
        
    def display_employee(self):
        print("Company:", self.company)

class Freelance(Employee):
    def __init__(self, name, company, salary):
        super().__init__(name, company)
        self.salary = salary
        
    def display_freelance(self):
        print("Salary:", self.salary)
freelancer1 = Freelance("Adeeba", "Freelance Inc.", 50000)
freelancer1.display_person()  
freelancer1.display_employee()  
freelancer1.display_freelance() 
