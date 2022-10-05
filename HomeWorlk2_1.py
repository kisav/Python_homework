import time



print('Вы попали в калькулятор')
print('Перед вами 5 проводов по которым можно забраться')
first_option = int(input('Выберете любой провод: '))
if first_option == 1:
    print('Вы полезли вверх...')
    time.sleep(5)
    print('Вы полезли вверх но вас ударило током')
elif first_option == 2:
    print('Вы полезли в верх...')
    time.sleep(2)
    print('Вы увидели огромного муравья\n который живёт в этом калькуляторе')
    time.sleep(1)
    print('Он вас съел.')
elif first_option == 3:
    print('Вы полезли в верх...')
    time.sleep(4)
    print('Вы подобрались к кнопкам\n но на них кто-то нажимал')
    time.sleep(1)
    print('Вас раздавило')
elif first_option == 4:
    print('Вы выбрались на следующий этаж...')
    time.sleep(1)
    print('Перед вами 2 щели')
    print('В какую из них пролезть?')
    second_option = int(input('1 или 2?'))
    if second_option == 1:
        print('Вы выбрались наружу')
    elif second_option == 2:
        print('Вы шли долго...')
        time.sleep(1)
        print('Вы пришли в тупик.')



if first_option == 5:
    print('Вы полезли в верх...')
    time.sleep(6)
    print('Вы непонятно куда лезете уже несколько лет\n game over')
else:
    print('Попробуйте ещё раз')

