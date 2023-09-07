def guess(num: int):
    if num < 0:
        return "не получилось"
    
    for i in range(1, num + 1):
        if i * i == num:
            return i
   
    return "не получилось"

num = int(input("Введите число: "))

print( guess(num))
