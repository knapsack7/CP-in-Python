# python object-oriented programming

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com' 
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Manoj','Verma', 50000)
emp_2 = Employee('Manish','Verma',80000)


print(emp_1.fullname())

print(Employee.fullname(emp_2))