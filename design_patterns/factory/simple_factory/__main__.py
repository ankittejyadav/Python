from autofactory import AutoFactory

"""ProblesmsSolved - Open/Close Violation - Simple to add new automobiles, create new class
and drop them in autos package and add in __init__ module

Eliminated dependencies on implementation of automobile classes - Main program knows only
to implement abstract method from abstarct base class, start and stop methods

separated concerns of main program and autofactoryloader

Note - we are limited to 1 factory"""

factory = AutoFactory()

for carname in "Toyota", "Mercedes", "BMW", "Vroom":
    car = factory.create_instance(carname)
    car.start()
    car.stop()
