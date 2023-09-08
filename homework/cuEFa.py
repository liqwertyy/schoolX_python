input_text = input('Ввод: ')
f_player, s_player = input_text.split(' ')

if f_player == 'камень' and s_player == 'ножницы':
    print('игрок 1 выиграл')
elif f_player == 'ножницы' and s_player == 'бумага':
    print('игрок 1 выиграл')
elif f_player == 'бумага' and s_player == 'камень':
    print('игрок 1 выиграл')
elif f_player == s_player:
    print('ничья')
else:
    print('игрок 2 выиграл')