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
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Manoj','Verma', 50000)
emp_2 = Employee('Manish','Verma',80000)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-30000'

new_emp_1 = Employee.from_string(emp_str_1)

import datetime

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))

# print(Employee.__dict__)
# print(emp_1.__dict__)
print(new_emp_1.email)
print(new_emp_1.pay)

print(Employee.num_of_emps)