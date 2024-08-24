# Performance Testing of SQL Queries

## Описание
Этот проект предназначен для тестирования производительности различных SQL запросов в базе данных MySQL. Скрипт выполняет несколько типов запросов, измеряет время их выполнения и визуализирует результаты в графиках с использованием библиотеки Matplotlib.

## Стек технологий
- **Python**
- **MySQL**
- **Matplotlib**
- **mysql-connector-python**
- **pyodbc**

## Установка

1. **Клонируйте репозиторий:**
    ```bash
    git clone  https://github.com/Spy230/stress_testing-master/tree/main
    ```

 
## Использование

1. **Настройте подключение к базе данных в файле `performance_test.py`.**
    Измените параметры подключения в разделе:
    ```python
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Users"
    )
    ```

2. **Запустите тестирование производительности:**
    ```bash
    python performance_test.py
    ```

3. **Результаты будут выведены в консоль, а также будет создан график с временем выполнения запросов.**

## Примеры работоспособности

### Время выполнения запросов
![image](https://github.com/user-attachments/assets/7da52486-876b-479c-80fe-4c8d311ea50f)

### Пример графика
![image](https://github.com/user-attachments/assets/7c2b8cc8-4435-4bcc-890f-f4cb1b82909d)
