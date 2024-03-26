# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# from easygui import *
import json
from os import system, name
def clear():
	if name == 'nt':
		_ = system('cls')

def save():
    with open("contacts.txt", "w", encoding = "utf-8") as contact:
        contact.write(json.dumps(contacts, ensure_ascii = False))
    print("Изменения сохранены")

def load_contacts():
    try:
        with open("contacts.txt", "r", encoding = "utf-8") as contact:
            contacts = json.load(contact)
    except:
        contacts = [
        { 
        "name": "Пётр",
        "surname": "Романов",
        "phone number": "123456789",
        "additional phone number": "23402340",
        "birthday": "01.01.2000",
        "email": "name1@email.internet"
        },
        {
        "name": "Славик",
        "surname": "",
        "phone number": "78904563",
        "additional phone number": "",
        "birthday": "02.02.2002",
        "email": "name1@email.internet"
        },
        {
        "name": "Юрий",
        "surname": "Иванов",
        "phone number": "45632107",
        "additional phone number": "3695214",
        "birthday": "03.03.2003",
        "email": ""
        }
        ]
    return contacts

def show(contacts):
    clear()
    for i in contacts:
        print("___________")
        for k, v in i.items():
            print("{0}: {1}".format(k, v))

def find_by_name(contacts):
    name = input("Кого ищем? ")
    flag = False
    for i in contacts:
        if name.casefold() in i["name"].casefold():
            flag = True
            print("___________")
            for k, v in i.items():
                print("{0}: {1}".format(k, v))
    if flag == False:
        print("Ничего не нашлось")

def find_by_number(contacts):
    number = input("Введите номер телефона: ")
    flag = False
    for i in contacts:
        if number in i["phone number"] or number in i["additional phone number"]:
            flag = True
            print("___________")
            for k, v in i.items():
                print("{0}: {1}".format(k, v))
    if flag == False:
        print("Ничего не нашлось")

def find_anything(contacts):
    name = input("Что ищем? ")
    flag = False
    for i in contacts:
        if name in i.values():
            flag = True
            print("___________")
            for k, v in i.items():
                print("{0}: {1}".format(k, v))
    if flag == False:
        print("Ничего не нашлось")

def remove(contacts):
    print("Введите порядковый номер контакта, который хотите удалить")
    for i in range(len(contacts)):
        print(f"{i + 1} - {contacts[i]["name"]} {contacts[i]["surname"]}")
    print("Чтобы выйти в меню, введите 0")
    while True:
        try:
            choice = int(input())
            if choice == 0:
                break
            elif choice > 0 and choice <= len(contacts):
                print(f"Контакт {contacts[choice - 1]["name"]} {contacts[choice - 1]["surname"]} удалён")
                del contacts[choice - 1]
                break
            else:
                print("Что-то не то ввели, попробуйте ещё раз")   
        except:
            print("Что-то не то ввели, попробуйте ещё раз")
    return contacts


contacts = load_contacts()

while True:
    user_choice = input("\
            Ваше действие:\n\
            1 - Посмотреть справочник\n\
            2 - Найти человека по имени\n\
            3 - Найти человека по номеру телефона\n\
            4 - Добавить контакт\n\
            5 - Изменить контакт\n\
            6 - Удалить контакт\n\
            Чтобы выйти, введите любой иной символ\n")
    if user_choice == "1":
        show(contacts)
    elif user_choice == "2":
        clear()
        find_by_name(contacts)
    elif user_choice == "3":
        clear()
        find_by_number(contacts)
    elif user_choice == "4":
        add(contacts)
        save()
    elif user_choice == "5":
        change(contacts)
        save()
    elif user_choice == "6":
        remove(contacts)
        save()
    else:
        save()
        print("Увидимся")
        break