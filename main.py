def main():

    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        x = int(input('Введите x: '))
        c = int(input('Введите c: '))

        if x < 4:
            y =  ((x * x) + (a * a)) * c / (2 * b)
        else:
            y = x * x * x *(a - b)

        print("Ответ: y =  %.1f" % y)
    except ValueError:
            print("Ошибка! Данные не верны")
    except ZeroDivisionError:
            print("Ошибка! Деление на ноль")

    input("Нажмите Enter для выхода")

if __name__ == '__main__':
    main()
