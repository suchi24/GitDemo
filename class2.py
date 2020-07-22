# example for self and class variables
class Calculator1:
    num = 100

    def __init__(self,a, b):
        self.first = a
        self.second = b
        print("This is parent class constructor")

    def summation(self):
        return self.first + self.second + Calculator1.num

obj = Calculator1(3,5)
print(obj.summation())

# obj1 = Calculator1(5,7)
# print(obj1.summation())