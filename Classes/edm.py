class Edm:
    # def __init__(self):
    # self.__dict__["name"] = "Ankit"
    # self.__dict__["age"] = 25
    # self.__dict__["position"] = "associate"
    # self.__dict__["salary"] = 500

    # self.name = "Ankit"
    # self.age = 25
    # self.position = "associate"
    # self.salary = 500

    def __init__(self, name, age, position, salary, exp, end_dt, start_dt):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.exp = exp
        self.end_dt = end_dt
        self.start_dt = start_dt
        self._annual_salary = None

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def exp(self):
        exp = end_dt - start_dt

    def info(self):
        print(
            f"Edm {self.name} is {self.age} yrs old and is an {self.position} who earns {self.salary}"
        )

    def __str__(self):
        return f"{self.name} is {self.age} yrs old and is an {self.position} who earns {self.salary}"

    def __repr__(self):
        return f"Edm ({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 1:
            raise ValueError("Min salary 1")
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        if exp < 0:
            raise ValueError("Min 0")
        self.__exp = exp


# e = Edm()
# print(e)
# print(e.__dict__)
# print(e.name)
# print(e.__class__)

e = Edm("Ankit", 25, "asscoiate", 500, 0, 2, 2)
# print(e.increase_salary(10))
# # print(e.info())
# print(str(e))

# print(e)
# print(repr(e))
# print(eval(repr(e)))

# e.set_salary(10)
# print(e.get_salary())
# e.salary = 1
# print(e.salary)

# e.exp = 10
# print(e._Edm__exp)

e.salary = 100
print(e.annual_salary)
e.salary = 200
print(e.annual_salary)
