class Employee:

    raise_amount = 1.04

    def __init__(self,firstname,lastname,amount):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + '.' + lastname+'@company.com'
        self.amount = amount

    def fullname(self):
        return '{} {}'.format(self.firstname, self.email)

    def raiseAmount(self):
        return self.raise_amount

class Developer(Employee):
    def __init__(self,firstname,lastname,amount,language):
        super().__init__(firstname,lastname,amount)
        self.language = language

emp_1 = Developer('Anshul','Khare',500000,'Python')
emp_1 = Developer('Anshul1','Khare2',600000,'Java')
print(emp_1.language)

#Changing value for perticular object only
emp_1.raise_amount = 1.05
print(emp_1.raise_amount)

#Value will not change by calling variable from class name
print(Employee.raise_amount)
