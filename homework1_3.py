import random

while True:
    first_term = random.randint(1, 1000)
    second_term = random.randint(1, 10000)

    print('Решите примеры:')
    print(first_term, '+', second_term)
    solution = input() 

    if int(solution) == first_term + second_term:
        print('Вы правильно ответили на этот пример!!!\n Если хотите ответить на него ещё раз, запустите код заново\n')
        break
    else:
        print('Вы неправильно ответили на пример, попробуйте ещё раз.')
        print("Правильный ответ: {}".format(first_term + second_term))
        print("Попробуйте ещё раз!\n\n")


















