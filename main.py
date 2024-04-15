# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# contact_data = {
#     'first_name': None,
#     'second_name': None,
#     'phone_number': None,
# }

def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите Отчество: ")
    
    phone = input("Введите номер телефона: ")
    contact = {
        'second_name': s_name,
        'first_name': f_name,
        'middle_name': m_name,
        'phone_number': phone
    }
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(f'{value}; ')
        file.write('\n')

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(";")))

def find_contact():
    # print(f"Поиск по: \n1 Имени\n2 Фамилии\n3 Отчеству\n4 Номеру\n5 Выход")
    title = ["Номер строки", "Фамилия", "Имя", "Отчество", "Телефон"]
    s_name = input("Введите Фамилию: ")
    count = set()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for cnt,line in enumerate(file):
            line = line.split(";")
            if s_name in line[0]:
                # print(f'{cnt}')
                count.add(cnt)
                print(f'{cnt}\t\t' + "\t\t".join(line))
    return count

def delete_contact():
    print("Для начала давайте найдем кого Вы хотите удалить")
    count = find_contact()
    if len(count) > 1:
        choice = input("Выберите номер кого именно вы хотите удалить: ")
        choice = int(choice)
        if choice in count:
            delete(choice)
        else:
            print("Извините, такого номера нету")
    else:
        delete(count.pop())
def delete(id):
    result = ''
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for cnt,line in enumerate(file):
            if cnt!=id:
                result+=line
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(result)
    print('\n\n\n\n\n Строка успешно удалена!')

def copy_contact():
    print("Для начала давайте найдем кого Вы хотите скопировать")
    count = find_contact()
    if len(count) > 1:
        choice = input("Выберите номер кого именно вы хотите скопировать: ")
        choice = int(choice)
        if choice in count:
            copy(choice)
        else:
            print("Извините, такого номера нету")
    else:
        copy(count.pop())

def copy(id):
    result = ''
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for cnt,line in enumerate(file):
            if cnt==id:
                result=line
    with open('copy.txt', 'w', encoding='utf-8') as file:
        file.write(result)
    print('\n\n\n\n\n Строка успешно скопирована!')

def main():
    isStop = 10
    while isStop!=0:
        print(f"Выберите что хотите сделать: \n1 Найти\n2 Добавить\n3 Удалить\n4 Открыть\n5 Копировать\n0 Выход")
        isStop= int(input(">"))
        if isStop == 2:
            add_new_contact()
        elif isStop == 4:
            open_phonebook()
        elif isStop == 1:
            find_contact()
        elif isStop == 5:
            copy_contact()
        elif isStop == 3:
            delete_contact()
        input("Нажмите Enter чтобы продолжить")
main()