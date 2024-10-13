bigSeq = [[1, 1], (2, 1), (4, 1), (9, {5}), 9]
listCount = 0
tupleCount = 0
dictionaryCount = 0
setCount = 0
for i in bigSeq:
    if isinstance(i, list):
        listCount += 1
        print(listCount)
    elif isinstance(i, dict):
        dictionaryCount += 1
        print(dictionaryCount)
    elif isinstance(i, tuple):
        tupleCount += 1
        print(tupleCount)
    elif isinstance(i, set):
        setCount += 1
        print(setCount)
