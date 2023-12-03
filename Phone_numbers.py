import sqlite3
import csv

def create_database():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE contacts
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL)''')

    conn.commit()
    conn.close()
    
create_database()

def add_contact(name, phone): # добавление новых конактов
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    # Вставляем данные в таблицу
    cur.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))

    conn.commit()
    conn.close()
    
def display_contacts(): # просмотт контактов
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    # Получаем все контакты из таблицы
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()

    # Выводим контакты
    for contact in contacts:
        print("Имя: ", contact[1])
        print("Телефон: ", contact[2])
        print("-------------")

    conn.close()

def import_contacts(filename): # импорт контактов
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # Пропускаем заголовок
        next(reader)

        for row in reader:
            name = row[0]
            phone = row[1]

            # Вставляем контакт в таблицу
            cur.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))

    conn.commit()
    conn.close()

def search_contacts(query): # поиск контактов
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    # Выполняем поиск контактов по имени или номеру телефона
    cur.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", ('%' + query + '%', '%' + query + '%'))

    contacts = cur.fetchall()

    conn.close()

    if len(contacts) > 0:
        for contact in contacts:
            print("Имя:", contact[1])
            print("Номер телефона:", contact[2])
            print("---------------------")
    else:
        print("Контакты не найдены.")

