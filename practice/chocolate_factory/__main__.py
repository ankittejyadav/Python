from factories import loader

for factory_name in (
    "lindt_factory",
    "mars_factory",
    "snickers_factory",
    "hersheys_factory",
):
    factory = loader.load_factory(factory_name)
    chocolate = factory.create_chocolate()
    chocolate.eat()
    chocolate.review()
