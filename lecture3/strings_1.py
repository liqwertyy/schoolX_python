# import string

# # name: str = input('name:')
# # greet_message = 'hello bob'

# # # greet_message: str = (
# # #     greet_message[:-3] + name
# # # )

# # greet_message: str = greet_message.replace(' bob ', name)
# # # print(greet_message[-3:])
# # print(greet_message)


# # river: str = 'mmmmississippi'
# # word: str = '<!--- dsa dsa dsa---!>'
# # # print(
# # #     'm' + river.lstrip('m')  #обрезать слева - lstrip
# # #     )
# # print(
# #     word.strip('<>!-').split()  
# #     )



# numbers: str = string.digits #импорт строки с числами
# word: str = 'dfds qr 213 wd 12312d1 d112d'
# _word: str = ''
# for ch in word:
#     if ch in numbers:
#         continue
#     else:
#         _word+=ch
# word=_word
# del _word #. Инструкция удаляет переменные, элементы, ключи, срезы и атрибуты.
# print(word)

# # for number in numbers:
# #     word = word.replace(number,'')
# # print(
# #     word.replace(numbers, '')
# # )


words: str = 'Hellol Bob daf!! BVBVB!!'
# words = words.find('Bob')
words = words.lower().replace('bob', 'gregory')
_word=''
while True:
    bob_index = words.lower().find('bob')
    if bob_index == -1:
        break
    else:
        # _word=words[:bob_index]
        
        print(_word)
    break


# print(
#     words.capitalize(),#маленькие буквы кроме первой
#     words.upper()#верхн регистр .lower - нижний

# )





_list: list = [1,2,3]
_str: str = '123'
_tuple: tuple = (1,2,3)

_list[-1]=5
_str[-1]=5 #нельзя изменять списки
_tuple[-1]=5 #тожже нельзя имз НО можно так:
_tuple: tuple=(
    [1,3],
    [2,3],
    [4,3],
    [9,6]
)

_tuple[1][1]=5
print(_list,_str,_tuple)