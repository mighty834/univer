# Тут нужен pip isntall pyodbc
import pyodbc

# Кейс-задача № 4
# Проведите анализ и опишите имеющихся на рынке программного обеспечения информационных систем,
# построенных по архитектуре WEB-приложений. Оцените и опишите возможности предлагаемых систем по архитектуре
# WEB-приложений и варианты их использования в компании. Создайте с помощью Delphi 10.2 и MS Internet Information
# Server (IIS) приложение WEB-архитектуры на любую тему. Базу данных для WEB-приложения создать в MS SQL Server.
# Ответом на задачу будет ссылка на репозиторий GitHub, где хранится Ваша программа. Или иным удобным для Вас способом.
# Когда вы создаете базу данных в MySQL с помощью MySQL Workbench (или любого другого инструмента),
# вы можете экспортировать схему базы данных в виде скрипта SQL. Этот скрипт SQL содержит определения таблиц,
# связей, индексов и других структур базы данных, которые вы создали. Или иным удобным для Вас способом.

# Подключение к MS SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'  # Или IP сервера
    'DATABASE=WebAppDB;'
    'UID=your_username;'  # Заменить на имя пользователя
    'PWD=your_password;'  # Заменить на пароль
)

cursor = conn.cursor()

# Функция для добавления новой заявки
def add_request(title, description):
    cursor.execute("""
        INSERT INTO Requests (RequestTitle, RequestDescription)
        VALUES (?, ?)
    """, (title, description))
    conn.commit()
    print("Заявка добавлена!")


# Функция для получения всех заявок
def get_all_requests():
    cursor.execute("SELECT RequestID, RequestTitle, RequestDescription, CreatedAt FROM Requests")
    rows = cursor.fetchall()
    for row in rows:
        print(
            f"ID: {row.RequestID}, Title: {row.RequestTitle}, Description: {row.RequestDescription}, Created At: {row.CreatedAt}")


# Пример использования
if __name__ == '__main__':
    # Добавить новую заявку
    add_request("Test Request", "This is a test description.")

    # Получить все заявки
    print("\nВсе заявки в базе данных:")
    get_all_requests()

# Закрыть соединение
conn.close()
