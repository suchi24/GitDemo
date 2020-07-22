#Example for Class

class Calculator:
    a = 0
    b = 0

    #constructor
    def __init__(self, x=None, y=None):
        print("This is default constructor")
        self.a = x
        self.b = y
    def add(self):
        c = self.a+ self.b
        return c

#obj = Calculator()
obj = Calculator(10,20)
#c = obj.add()
#print(c)