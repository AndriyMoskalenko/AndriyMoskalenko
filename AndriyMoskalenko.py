def print_h(a, b):
    count = 0
    while count < a:
        print("Значение", count, "- еще нет")
        count = count + b
    else:
        print("Значение", count, "Дождались!")
print_h(5, 1)
