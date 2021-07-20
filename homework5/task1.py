#!/usr/bin/python3
"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Teacher:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, days_for_work):
        return Homework(text, days_for_work)


class Student:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        return homework if homework.is_active() else print("You are late")


class Homework:
    def __init__(self, text, days_for_work):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=days_for_work)

    def is_active(self):
        return datetime.datetime.now() < self.created + self.deadline


# if __name__ == '__main__':
#     teacher = Teacher('Daniil', 'Shadrin')
#     student = Student('Roman', 'Petrov')
#     print(teacher.last_name)  # Daniil
#     print(student.first_name) # Petrov

#     expired_homework = teacher.create_homework('Learn functions', 0)
#     print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
#     print(expired_homework.deadline)  # 0:00:00
#     print(expired_homework.text)  # 'Learn functions'

#     # create function from method and use it
#     create_homework_too = teacher.create_homework
#     oop_homework = create_homework_too('create 2 simple classes', 5)
#     print(oop_homework.deadline)  # 5 days, 0:00:00

#     student.do_homework(oop_homework)
#     student.do_homework(expired_homework)  # You are late
