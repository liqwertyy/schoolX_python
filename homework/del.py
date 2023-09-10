def find(a, b):
    if a <= 0 or b <= 0:
        return 0

    while b != 0:
        a, b = b, a % b

    return a

a = 150
b = 84
result = find(a, b)

print("Наибольший общий делитель чисел", a, "и", b, "равен", result)
