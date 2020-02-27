# а) Дана послідовність а, що складається з символів s1, s2, .... Відомо, що символ s1
# відмінний від знаку оклику і що серед s2, s3, ... є хоча б один знак оклику. Припустимо
# s1, ..., sn – символи даної послідовності, що передують першому знаку оклику (n
# заздалегідь не відомо). Визначити, чи міститься у послідовності а усі букви, що входять у
# слово «казка».
#
#
while True:
    while True:
        try:
            a = input().split()
            break
        except ValueError or NameError:
            print('it must be digits')
    for k in range(len(a)):
        if len(a[k]) == 1:
            continue
        else:
            print('Symbol must consists of 1 ')
            print('Would you try again? Write yes or no')
            answer = input('')
            if answer == 'yes':
                continue
            else:
                break
    if a[0] != '!':
        for i in range(len(a)):
            if a[i] == '!':
                a1 = (' '.join(a[: a.index('!')]))
                print(a1)
                for j in range(len(a1)):
                    j += 1
                    n = {'казка'}
                    if a1[j] in n:
                        print('yes,all letters')
                    else:
                        print('Not all letters from word "казка"')
                        print('Would you try again? Write yes or no')
                        answer = input('')
                        if answer == 'yes':
                            continue
                        else:
                            break
    else:
        print('Firs symbol is !')
        print('Would you try again? Write yes or no')
        answer = input('')
        if answer == 'yes':
            continue
        else:
            break
