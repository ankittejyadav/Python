def BubbleSort(elements, key="None"):
    for j in range(len(elements) - 1):
        swapped = False
        for i in range(len(elements) - 1 - j):
            a = elements[i][key]
            b = elements[i + 1][key]
            if a > b:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    # elements = [3, 7, 1, 3, 90, 34, 59, 25, 80, 25, 29]
    # BubbleSort(elements)
    elements2 = [
        {"name": "a", "amount": 1, "device": "ios11"},
        {"name": "k", "amount": 5, "device": "ios7"},
        {"name": "v", "amount": 8, "device": "ios10"},
        {"name": "h", "amount": 2, "device": "ios1"},
    ]
    BubbleSort(elements2, key="name")
    print(elements2)
