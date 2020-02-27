# Визначити загальну вартість всіх товарів, випущених в поточному році і
# вивести інформацію про ці товари. Поля структури: Найменування, Виробник, Рік
# видання, Кількість, Ціна.
while True:
    while True:
        try:
            a = {'Найменування': input('Найменування '), 'Виробник': input('Виробник '),
                 'Рік видання': int(input('Рік видання ')),
                 'Кількість': int(input('Кількість ')), 'Ціна': float(input('Ціна '))}
            break
        except ValueError or NameError:
            print('it must be digits')
    cy = 2020
    if a['Рік видання'] == cy:
        for key, name in a.items():
            print(key, name)
        print("Загальна вартість = ", a['Кількість'] * a['Ціна'])
        print('Would you try again? Write yes or no')
        answer = input('')
        if answer == 'yes':
            continue
        else:
            break
    else:
        print('Nothing from current year,sorry')
        print('Would you try again? Write yes or no')
        answer = input('')
        if answer == 'yes':
            continue
        else:
            break
