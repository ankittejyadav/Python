class Employee_parentclass:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)


class Tester_childclass(Employee_parentclass):
    def run_tests(self):
        print(f"Tests run by {self.name}")
        print(f"Tests are done")


class Developer_childclass(Employee_parentclass):
    def increase_salary(self, percent, bonus=0):  # Method Overriding (bonus=default)
        self.salary += self.salary * (percent / 100)
        self.salary += bonus


class Developer2_childclass(Employee_parentclass):
    def __init__(self, name, age, position, salary, framework):  # Method Overriding
        super().__init__(name, age, position, salary)  # Method resolution order
        self.framework = framework

    def increase_salary(self, percent, bonus=0):  # Method Overriding (bonus=default)
        super().increase_salary(percent)  # Method resolution order
        self.salary += bonus


employee1 = Tester_childclass("Ankit", 20, "L1", 500)
employee1.increase_salary(50)
print(f"Employee 1 salary - {employee1.salary}")
employee1.run_tests()
print(isinstance(employee1, Tester_childclass))
print(isinstance(employee1, Employee_parentclass))
print("---------------------------------------------")

employee2 = Developer_childclass("Ankiket", 22, "L2", 500)
employee2.increase_salary(50, 20)
print(f"Employee 2 salalry - {employee2.salary}")
print(issubclass(Developer_childclass, Employee_parentclass))
print(issubclass(Developer_childclass, object))
print("---------------------------------------------")

employee3 = Employee_parentclass("Ani", 11, "L0", 5)
print(repr(employee3))
print(issubclass(Employee_parentclass, object))
print("---------------------------------------------")

employee4 = Developer2_childclass("Jay", 22, "L2", 500)
employee4.increase_salary(50, 20)
print(f"Employee 4 salary - {employee4.salary}")
