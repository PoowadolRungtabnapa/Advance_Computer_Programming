class employee() :
    def __init__(self, name, age, Id, salary) :
        self.name = name
        self.age = age
        self.Id = Id
        self.salary = salary
    
    def show_employee(self) :
        print('Employee Name ', self.name, 'Age',
                self.age,' Salary', self.salary, 'Id',self.Id)

emp1 = employee("Peter",22, 1000, 1234)
print(emp1.__dict__)
emp2 = employee("Bob",23 ,2000, 2234)
emp2.show_employee()