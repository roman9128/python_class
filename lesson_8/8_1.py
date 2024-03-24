# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from easygui import *
import json
from pprint import pprint 
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
        contacts = { 
            "Name1": {"phones": [1234, 2341], "birthday": "01.01.2000", "email": "name1@email.internet"},
            "Name2": {"phones": [7890], "birthday": "02.02.2002"}
        }
    return contacts

def show(contacts):
    clear()
    pprint(contacts)

def change(contacts):
    item_to_change = input("Что меняем: ")
    new_item = input("На что меняем: ")

    return contacts

def find(contacts):
    name = input("Кого ищем? ")
    try:
        print(contacts[name])
    except:
        print("Здесь такого нет")

contacts = load_contacts()

while True:
    user_choice = input("Ваше действие:\n\
                            1 - Посмотреть справочник\n\
                            2 - Найти контакт\n\
                            3 - Добавить контакт\n\
                            4 - Изменить контакт\n\
                            5 - Удалить контакт\n\
                            Чтобы выйти, нажмите любую иную клавишу\n")
    if user_choice == "1":
        show(contacts)
    elif user_choice == "2":
        clear()
        find(contacts)
    elif user_choice == "3":
        add(contacts)
        save()
    elif user_choice == "4":
        change(contacts)
        save()
    elif user_choice == "5":
        remove(contacts)
        save()
    else:
        save()
        print("Увидимся")
        break