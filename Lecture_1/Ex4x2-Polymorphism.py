class employee() :
    def __init__(self, name, age, Id, salary):
        self.name = name
        self.age = age
        self.Id = Id
        self.salary = salary

    def earn(self) :
        pass

class childemployee1(employee) :
    def earn(self) :
        print('no money')
    
class childemployee2(employee) :
    def earn(self) :
        print('has money')

c = childemployee1
c.earn(employee)
d = childemployee2
d.earn(employee)