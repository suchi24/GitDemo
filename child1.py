#Child class from calculator class
from class2 import Calculator1


class child1(Calculator1):
    num2 = 200

    def __init__(self):
        Calculator1.__init__(self, 3,2)

    def getCompleteData(self):
        return self.num2 + self.summation()

obj = child1()
print(obj.getCompleteData())
