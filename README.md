# Working-with-SQL-databases

Задание 1
Напишите модуль users.py, который регистрирует новых пользователей. Скрипт должен запрашивать следующие данные:

имя
фамилию
пол
адрес электронной почты
дату рождения
рост
Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3.

Задание 2
Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:

запросить идентификатор пользователя;
если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
если пользователя с таким идентификатором нет, вывести соответствующее сообщение.

Exercise 1
Write a users.py module that registers new users. The script should request the following data:

name
surname
floor
E-mail address
date of birth
growth
Save all user data in the user table of our sochi_athletes.sqlite3 database.

Assignment 2
Write the find_athlete.py module to find the athlete closest to the user. The logic of the module is as follows:

request a user ID;
if a user with such an identifier exists in the user table, then display two athletes: the closest by date of birth to this user and the closest in height to this user;
if there is no user with this identifier, display a corresponding message.
