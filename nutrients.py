from vitamin import Vitamin


class Nutrients:
    def __init__(self):
        self.vitamins = []

    def addVitamins(self, vitamin):
        self.vitamins.append(vitamin)

    def displayNutrients(self):
        for v in self.vitamins:
            print(v.name)
            print(f"Daily Value: ", v.dailyValue)
            print(f"Max Value: ", v.maxValue)
            print("-----------------------------")


def main():
    myNutrients = Nutrients()
    vitamin1 = Vitamin("Vitamin A", 900, 3000)
    myNutrients.addVitamins(vitamin1)
    myNutrients.displayNutrients()


main()
