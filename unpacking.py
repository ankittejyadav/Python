values = [1, 2, 3, 4, 5, 6]
# list-> int
print("These", "are", values)

print(*values)
print(1, 2, 3, 4, 5, 6)


def my_sum(a, b, c):
    return a + b + c


values = (1, 2, 3)
print(my_sum(*values))
print(my_sum(values[0], values[1], values[2]))
v1, v2, v3 = values
print(v1, v2, v3)


values = (1, 2, 3, 4, 5, 6)
v1, *v2, v3 = values
print(v1, v2, v3)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, "test", *list2]
combined2 = [1, 2, 3, "test", 4, 5, 6]
print(combined)
print(combined2)
