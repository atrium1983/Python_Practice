# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. 
# Ваша программа не должна быть линейной

# def enter_first_name():
#     return input("Введите имя: ").title()

# def enter_second_name():
#     return input("Введите отчество: ").title()

# def enter_family_name():
#     return input("Введите фамилию: ").title()

# def enter_phone_number():
#     return input("Введите номер телефона: ").title()

# def enter_adress():
#     return input("Введите адрес: ").title()

# def enter_data():
#     name = enter_first_name()
#     surname = enter_second_name()
#     family_name = enter_family_name()
#     phone = enter_phone_number()
#     adress = enter_adress()
#     with open('phone_book.txt', 'a', encoding='utf-8') as file:
#         file.write(f'{name} {surname} {family_name}\n{phone}\n{adress}\n\n')
        
# def print_data():
#     with open('phone_book.txt', 'a', encoding='utf-8') as file:
#         print(file.read())



# enter_data()


def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title()

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')


def print_data():
     with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())
        
def search_line():
    print('Выберите вариант поиска:\n'
        '1. Имя\n'
        '2. Отчество\n'
        '3. Фамилия\n'
        '4. Номер\n'
        '5. Адрес\n')
    index = int(input('Введите индекс: ')) - 1
    searched = input('Введите данные для поиска: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end='\n\n')
        #file.read().split('\n\n'))
        #file.seek(1)
        #print(file.readlines())
        
def user_interface():
    cmd = 0
    while cmd != '4':
        print('Выберите действие:\n'
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск\n'
            '4. Выход\n')
        cmd = input('Введите индекс: ')
        while cmd not in ('1','2','3','4'):
            print('Некоректный ввод')
            cmd = input('Введите индекс: ')
            
        match cmd:
            case '1': 
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':    
                print('Всего доброго!')
            
#enter_data()
#search_line()
user_interface()


"""
def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('Выбертите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end="\n\n")
        # file.seek(0)
        # print(file.readlines())

def interface():
    cmd = 0
    while cmd != '4':
        print("Выберите действие: \n"
              "1. Добавить контакт\n"
              "2. Вывести все контакты\n"
              "3. Поиск контакта\n"
              "4. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                print('Всего доброго! ')

interface()
"""