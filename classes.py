# python object-oriented programming

class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1 
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Manoj','Verma', 50000)
emp_2 = Employee('Manish','Verma',80000)



# print(Employee.__dict__)
# print(emp_1.__dict__)

print(Employee.num_of_emps)