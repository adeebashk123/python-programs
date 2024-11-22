from abc import ABC, abstractmethod
class mathoperation(ABC):
    @abstractmethod
    def calculate(self,a,b):
        pass
class add(mathoperation):
    def calculate(self, a, b):
        return a+b
class sub(mathoperation):
    def calculate(self, a, b):
        return a-b
class multi(mathoperation):
    def calculate(self, a, b):
        return a*b
math1 = add()
print(math1.calculate(10, 5)) 

math2 = sub()
print(math2.calculate(10, 5))

math3 = multi()
print(math3.calculate(10, 5))
