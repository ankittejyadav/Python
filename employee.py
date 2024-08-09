class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculatePaycheck(self):
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourlySalary, hoursWorked):
        super().__init__(fname, lname)
        self.hourlySalary = hourlySalary
        self.hoursWorked = hoursWorked

    def calculatePaycheck(self):
        return self.hourlySalary * self.hoursWorked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales, commissionSalary):
        super().__init__(fname, lname, salary)
        self.sales = sales
        self.commissionSalary = commissionSalary

    def calculatePaycheck(self):
        regularSalary = super().calculatePaycheck()
        totalComission = self.sales * self.commissionSalary
        return regularSalary + totalComission
