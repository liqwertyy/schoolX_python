numbers: list=[
    1, 2, 4, 5, 6, 7, 8, 9, 15
]
# for n in numbers: 
#     if n % 3 == 0:
#         print(f'Число - {n} кратно 3')
#     if n % 3 !=0:
#         print(f'Число {n} не кратно 3')


# for n in numbers: 
#     if n % 3==0 and n%5==0:
#         print(f'Число - {n} кратно 5 и 3') 
#     elif n % 5 == 0:
#        print(f'Число - {n} кратно 5') 
#     elif n % 3==0:
#         print(f'Число - {n} кратно 3') 
#     else:
#         print(f'Число {n} не подходит')


# word: str = input('введите слово')
# vowel: str='aeiouy'
# vowel_count: int =1 
# for c in word:
#     if c in vowel: 
#         vowel_count+=1

# print(vowel_count)




n: int = int(input('N: '))
# sum_all=0

# for i in range(n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         sum_all = sum_all+i
# print(sum_all) 


list3: list=[

]
list5: list=[

]
for i in range(n+1):
    if i % 3 == 0:
        list3.append(i)
    if i % 5 == 0:
        list3.append(i)
set3 = set()