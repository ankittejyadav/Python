def BubbleSort(elements):
    for j in range(len(elements) - 1):
        swapped = False
        for i in range(len(elements) - 1 - j):
            if elements[i] > elements[i + 1]:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [3, 7, 1, 3, 90, 34, 59, 25, 80, 25, 29]
    BubbleSort(elements)
    print(elements)
