from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def addEmployee(self, newEmployee):
        self.employees.append(newEmployee)

    def displayEmployee(self):
        print("Employees\n")
        for i in self.employees:
            print(i.fname, i.lname)
            print("--------------------------")

    def displaySalary(self):
        print("\nPaying Employees\n")

        for i in self.employees:
            print("Paycheck for:", i.fname, i.lname)
            print(f"Amount: ${i.calculatePaycheck():,.2f}")
            print("--------------------------")


def main():
    myCompany = Company()
    employee1 = SalaryEmployee("Ankit", "Yadav", 50000)
    myCompany.addEmployee(employee1)
    employee2 = HourlyEmployee("Ank", "Yad", 50, 40)
    myCompany.addEmployee(employee2)
    employee3 = CommissionEmployee("A", "Y", 50000, 5, 50)
    myCompany.addEmployee(employee3)
    myCompany.displayEmployee()
    myCompany.displaySalary()


main()
