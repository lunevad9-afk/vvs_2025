def lvl_1(metod_1, txt_1):
    if metod_1 == "upper":
        txt_1 = txt_1.upper()
    elif metod_1 == "lower":
        txt_1 = txt_1.lower()
    elif metod_1 == "capitalize":
        txt_1 = txt_1.capitalize()
    return txt_1

def lvl_2(metod, txt, number_1, number_2):
    if metod == "найти":
        result = txt.find(number_1)
    elif metod == "заменить":
        result = txt.replace(number_1, number_2, 1)
    elif metod == "подсчет":
        result = txt.count(number_1)
    return result

def lvl_3(metod, txt):
    if metod == "разделить":
        result = txt.split(',')
    else:
        result = ";".join(txt)
    return result

def lvl_4(metod, txt):
    if metod == "проверка на число":
        result = txt.isdigit()
    elif metod == "проверка на буквы":
        result = txt.isalpha()
    elif metod == "убрать пробелы":
        result = txt.strip()
    return result

def open_menu():
    print("ДОСТУПНЫЕ УРОВНИ И МЕТОДЫ:")
    print("Уровень 1 - Изменение регистра:")
    print("   upper - преобразовать в верхний регистр")
    print("   lower - преобразовать в нижний регистр")
    print("   capitalize - сделать первую букву заглавной")
    print()
    print("Уровень 2 - Поиск и замена:")
    print("   найти - найти расположение элемента")
    print("   заменить - заменить первый найденный элемент")
    print("   подсчет - подсчитать количество вхождений")
    print()
    print("Уровень 3 - Разделение и объединение:")
    print("   разделить - разделить строку по запятым")
    print("   объединить - объединить элементы через точку с запятой")
    print()
    print("Уровень 4 - Проверка и очистка:")
    print("   проверка на число - проверить, состоит ли строка из цифр")
    print("   проверка на буквы - проверить, состоит ли строка из букв")
    print("   убрать пробелы - удалить пробелы в начале и конце")
    print("\nДля выхода введите 'выход'")


def main():

    
    while True:
        open_menu()
        
        lvl = input("\nВыберите уровень (1-4) или 'выход' для завершения: ").strip().lower()
        
        if lvl == 'выход':
            print("Программа завершена!")
            break
            
        if lvl == '1':
            txt_1 = input("Введите текст: ")
            metod_1 = input("Выберите метод (upper/lower/capitalize): ").strip().lower()
            result = lvl_1(metod_1, txt_1)
            print(f"Результат: {result}")
            
        elif lvl == "2":
            txt_2 = input("Введите текст: ")
            metod_2 = input("Выберите метод (найти/заменить/подсчет): ").strip().lower()
            number_to_find = input("Выберите элемент для операции: ")
            number_to_replace = ""
            if metod_2 == "заменить":
                number_to_replace = input("Введите замену: ")
            result = lvl_2(metod_2, txt_2, number_to_find, number_to_replace)
            print(f"Результат: {result}")
            
        elif lvl == "3":
            txt_3 = input("Введите текст: ")
            metod_3 = input("Выберите метод (разделить/объединить): ").strip().lower()
            result = lvl_3(metod_3, txt_3)
            print(f"Результат: {result}")
            
        elif lvl == "4":
            txt_4 = input("Введите текст: ")
            metod_4 = input("Выберите метод (проверка на число/проверка на буквы/убрать пробелы): ").strip().lower()
            result = lvl_4(metod_4, txt_4)
            print(f"Результат: {result}")
            
        else:
            print("Неверный выбор уровня. Выберите от 1 до 4.")
            
    
        input("\nНажмите Enter чтобы продолжить...")


if name == "__main__":
    main()