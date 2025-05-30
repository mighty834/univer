--Кейс-задача № 3

--Спроектируйте базу данных «Туризм» (перечень предоставляемых услуг, заказ туров и др.).
--При проектировании базы данных необходимо создать 4-5 таблиц предметной области: 3-4 таблицы-справочника и
-- 1 таблицу переменной информации. Для всех таблиц создать первичные ключи. Построить связи между таблицами при помощи
-- внешних ключей: атрибуты таблицы переменной информации должны ссылаться на ключевые атрибуты таблиц справочников.
--Когда вы создаете базу данных в MySQL с помощью MySQL Workbench (или любого другого инструмента),
-- вы можете экспортировать схему базы данных в виде скрипта SQL. Этот скрипт SQL содержит определения таблиц,
-- связей, индексов и других структур базы данных, которые вы создали. Или иным удобным для Вас способом.

CREATE DATABASE Tourism;
USE Tourism;

-- Справочник клиентов
CREATE TABLE Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- Справочник туров
CREATE TABLE Tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_name VARCHAR(100),
    price DECIMAL(10,2),
    destination_id INT,
    FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id)
);

-- Справочник направлений
CREATE TABLE Destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_name VARCHAR(100),
    country VARCHAR(100)
);

-- Справочник услуг
CREATE TABLE Services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Таблица заказов
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    tour_id INT,
    service_id INT,
    order_date DATE,
    total_price DECIMAL(10,2),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (tour_id) REFERENCES Tours(tour_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);
