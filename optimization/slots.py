class Slots:
    # pros:Faster attribute access and reduced memory overhead because each insatnce is not utilizing dictionaries
    # #cons: cannot add attributes dynamically anymore
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


employee1 = Slots("A", 1, 100)
# print(employee1.__dict__) # error no dict
print(f"{employee1.__slots__}")
