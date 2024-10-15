from lindt import Lindt
from mars import Mars
from snickers import Snickers
from others import Others


def get_chocolates(chocolate):
    if chocolate == "Lindt":
        return Lindt()
    elif chocolate == "Mars":
        return Mars()
    elif chocolate == "Snickers":
        return Snickers()
    else:
        return Others(chocolate)


for chocolate in "Lindt", "Mars", "Snickers", "Hersheys":
    ankit = get_chocolates(chocolate)
    ankit.eat()
    ankit.review()
