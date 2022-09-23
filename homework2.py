
yes = 'ДА'
no = 'НЕТ'

print('Чтобы заполнить анкету введите следующую информацию:')

print('Введите ваш возраст:')
age = int(input())

print('Введите ваше хобби:')
hobbie = str(input())

print('Введите ваше имя:')
name = str(input())

print('Вот вся информация: ваш возраст: {0}, ваше хобби: {1}, ваше имя: {2}. \nВы уверены что хотите продолжить? (да \ нет) \n'.format(age, hobbie, name))
Are_you_sure = str(input()).upper()

if Are_you_sure == yes:
    print('Спасибо за заполнение анкеты, информация придёт к вам на почту')
elif Are_you_sure == no:
    print('Спасибо, мы отменили запись')
else:
    print('Попробуйте ещё раз')














