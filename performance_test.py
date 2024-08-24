import mysql.connector
import time
import matplotlib.pyplot as plt
import matplotlib

# Отобразить текущий используемый бэкенд
print(f"Используемый бэкенд: {matplotlib.get_backend()}")

# Подключение к базе данных
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Users"
)

cursor = conn.cursor()

# Словарь для хранения времени выполнения запросов
query_times = {}

# Пример простого запроса
start_time = time.time()
cursor.execute("SELECT COUNT(*) FROM Users")
count_result = cursor.fetchone()
end_time = time.time()
query_times['COUNT Query'] = end_time - start_time
print(f"Время выполнения запроса COUNT: {query_times['COUNT Query']} секунд")
print(f"Количество записей: {count_result[0]}")

# Пример сложного запроса
start_time = time.time()
cursor.execute("SELECT * FROM Users WHERE Email LIKE '%a%'")
like_result = cursor.fetchall()
end_time = time.time()
query_times['LIKE Query'] = end_time - start_time
print(f"Время выполнения запроса LIKE: {query_times['LIKE Query']} секунд")
print(f"Найдено записей: {len(like_result)}")

# Пример запроса с ограничением
start_time = time.time()
cursor.execute("SELECT * FROM Users LIMIT 10")
limit_result = cursor.fetchall()
end_time = time.time()
query_times['LIMIT Query'] = end_time - start_time
print(f"Время выполнения запроса LIMIT: {query_times['LIMIT Query']} секунд")
print(f"Найдено записей: {len(limit_result)}")

# Пример запроса с сортировкой
start_time = time.time()
cursor.execute("SELECT * FROM Users ORDER BY Email DESC LIMIT 10")
order_result = cursor.fetchall()
end_time = time.time()
query_times['ORDER BY Query'] = end_time - start_time
print(f"Время выполнения запроса ORDER BY: {query_times['ORDER BY Query']} секунд")
print(f"Найдено записей: {len(order_result)}")

# Пример агрегатного запроса
start_time = time.time()
cursor.execute("SELECT AVG(Age) FROM Users")  # Пример числового столбца
avg_result = cursor.fetchone()
end_time = time.time()
query_times['AVG Query'] = end_time - start_time
print(f"Время выполнения запроса AVG: {query_times['AVG Query']} секунд")

# Пример запроса с объединением
start_time = time.time()
cursor.execute("""
SELECT Users.FirstName, Orders.OrderID
FROM Users
INNER JOIN Orders ON Users.ID = Orders.ID
""")
join_result = cursor.fetchall()
end_time = time.time()
query_times['JOIN Query'] = end_time - start_time
print(f"Время выполнения запроса JOIN: {query_times['JOIN Query']} секунд")

cursor.close()
conn.close()

# Создание графиков
queries = list(query_times.keys())
times = list(query_times.values())

plt.figure(figsize=(14, 8))
plt.bar(queries, times, color=['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'cyan'])
plt.xlabel('Тип запроса')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение времени выполнения запросов')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Принудительное отображение графика
plt.show(block=True)
