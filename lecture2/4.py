n: int = int(input('N: '))

# while n > 0:
#     print(n)
#     n= n-1 

array: list = list(range(n))
i = 0
while True:
    if array[i] % 123 ==0:
        print(array[i], 'делится')
        break 
    i+=1
   