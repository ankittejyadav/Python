s = "hello"
print(f"String s is an object - {type(s)}")


def fun():
    pass


print(f"Function Fun is an object - {type(fun)}")

from datetime import date


class Employee:
    MIN_WAGE = 1

    @classmethod
    def change_min_wage(cls, new_wage):
        if new_wage > 10:
            raise ValueError("Company is bankrupt")
        cls.MIN_WAGE = new_wage

    @classmethod
    def new_employee(cls, name, dob):  # Alternative constructor
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.MIN_WAGE)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.MIN_WAGE:
            raise ValueError("Min salary {Employee.MIN_WAGE}")
        self._annual_salary = None
        self._salary = salary


print(f"Emplyee class is an object - {type(Employee)}")
print("---------------------------------------------")
print(f"Class dictionary - {Employee.__dict__}")
print("---------------------------------------------")

e = Employee("Ankit", 11, 100)
Employee.__dict__["increase_salary"](e, 20)
print(e.salary)
# e.salary = 0
# print(e.salary) # Throws error
print(Employee.salary)
print(e.salary)
print("---------------------------------------------")

print(f"Old Min Wage - {Employee.MIN_WAGE}")
Employee.change_min_wage(9)
print(f"New Min Wage - {Employee.MIN_WAGE}")
print("---------------------------------------------")

e2 = Employee.new_employee("Ali", date(1990, 5, 22))
print(e2.name)
print(e2.age)
print(e2.salary)
