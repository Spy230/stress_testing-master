import mysql.connector
import random
import string

# Функция для генерации случайных данных
def generate_data(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size)) 

# Подключение к базе данных MySQL
conn = mysql.connector.connect(
    host="localhost",       # Замените на хост вашего MySQL сервера
    user="root",            # Замените на ваше имя пользователя
    password="",            # Замените на ваш пароль
    database="Users"        # Замените на имя вашей базы данных
)

cursor = conn.cursor()

# Генерация и вставка данных
for _ in range(1000000):  # Генерация 100,000 записей
    first_name = generate_data(10)
    last_name = generate_data(10)
    email = generate_data(15) + "@example.com"
    cursor.execute("INSERT INTO Users (FirstName, LastName, Email) VALUES (%s, %s, %s)", 
                   (first_name, last_name, email))

conn.commit()
cursor.close()
conn.close()
