import random


def generate_pc():
    pc = random.randint(1, 4)
    return pc


def num_to_word(num):
    if num == 1:
        return 'камень'
    elif num == 2:
        return 'ножницы'
    elif num == 3:
        return 'бумага'
    else:
        return 'карандаш'

my_counter = 0
pc_counter = 0

while True:
    print(40 * '-')
    answer = int(input('Введите ответ 1 - камень 2 - ножницы 3 - бумага 4 - карандаш: '))
    pc = generate_pc()
    print(f'Вы: {num_to_word(answer)}, компьютер: {num_to_word(pc)}')
    if answer == pc:
        print('Ничья')

    elif answer == 1 and pc == 2:
        print('Вы победили')
        my_counter += 1
    elif answer == 1 and pc == 3:
        print('Вы проиграли')
        pc_counter += 1

    elif answer == 2 and pc == 3:
        print('Вы победили')
        my_counter += 1
    elif answer == 2 and pc == 1:
        print('Вы проиграли')
        pc_counter += 1

    elif answer == 3 and pc == 1:
        print('Вы победили')
        my_counter += 1

    elif answer == 3 and pc == 2:
        print('Вы проиграли')
        pc_counter += 1

    if answer == pc:
        print('Ничья')

    elif answer == 1 and pc == 2:
        print('Вы победили')
        my_counter += 1
    elif answer == 1 and pc == 3:
        print('Вы проиграли')
        pc_counter += 1

    elif answer == 2 and pc == 3:
        print('Вы победили')
        my_counter += 1

    elif answer == 2 and pc == 1:
        print('Вы проиграли')
        pc_counter += 1

    elif answer == 3 and pc == 1:
        print('Вы победили')
        my_counter += 1

    elif answer == 3 and pc == 2:
        print('Вы проиграли')
        pc_counter += 1  # Увеличиваем счетчик побед противника
    elif answer == 4 and pc == 1:
        print('Вы проиграли')
        pc_counter += 1
    elif answer == 4 and pc == 2:
        print('Вы проиграли')
        pc_counter += 1
    elif answer == 4 and pc == 3:
        print('Вы победили')
        my_counter += 1
    elif answer == 1 and pc == 4:
        print('Вы проиграли')
        pc_counter += 1
    elif answer == 2 and pc == 4:
        print('Вы проиграли')
        pc_counter += 1
    elif answer == 3 and pc == 4:
        print('Вы проиграли')
        pc_counter += 1

print(f'Счет: Вы: {my_counter}, Компьютер: {pc_counter}')























