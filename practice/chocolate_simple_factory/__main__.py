from chocolatefactory import ChocolateFactory

factory = ChocolateFactory()

for chocolate in "Lindt", "Mars", "Snickers", "Hersheys":
    chocolate = factory.create_instance(chocolate)
    chocolate.eat()
    chocolate.review()
