#!/usr/bin/python3
"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """You are late"""


class RepeatedResultError(Exception):
    """This result has been added earlier"""


class Person:
    """This is a helper parent class

    :param first_name: first name of a person
    :type first_name: str
    :param last_name: last name of a person
    :type last_name: str
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        """Constructor method"""
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """This is a class initiates the homework task whuch shold be done

    :param text: homework text
    :type text: str
    :param days_for_work: time to complete homework expressed in days
    :type days_for_work: int
    """

    def __init__(self, text: str, days_for_work: int) -> None:
        """Constructor method"""
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=days_for_work)

    def is_active(self) -> bool:
        """Сhecks if there is time left to complete the homework

        :return: `True` if there is time left to complete the homework, `False` otherwise
        :rtype: bool
        """
        return datetime.datetime.now() < self.created + self.deadline


class Student(Person):
    """This is a class initiates the students who do homework

    :param Person: helper parent class
    :type Person: Person
    """

    def do_homework(self, homework: Homework, result: str):
        """Try to solve homework and return result

        :param homework: a :class:'Homework' objects, which provide homework to complete
        :type homework: __main__.Homework
        :param result: homework result information
        :type result: str
        :raises DeadlineError: raises an error if student has no time to do homework
        :return: A :class:'HomeworkResult', which represent homework result
        :rtype: HomeworkResult
        """
        if homework.is_active():
            return HomeworkResult(self, homework, result)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    """This is a class initiates the homework result

    :param author: homework text
    :type author: __main__.Student
    :param homework: a :class:'Homework' objects, which provide homework to complete
    :type homework: __main__.Homework
    :param solution: homework solution
    :type solution: str
    :raises TypeError: raises an error if not :class:'Homework' objects was given
    """

    def __init__(self, author: Student, homework: Homework, solution: str) -> None:
        """Constructor method"""
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Teacher(Person):
    """This is a class initiates the teachers who assigns and reviews homeworks

    :param Person: helper parent class
    :type Person: Person
    :param homework_done: storage of reviewed homeworks
    :type homework_done: collections.defaultdict
    """

    homework_done = defaultdict(set)

    def create_homework(self, text: str, days_for_work: int) -> Homework:
        """Returns a :class:'Homework' objects representing
        home work for students

        :param text: homework text
        :type text: str
        :param days_for_work: time to complete homework expressed in days
        :type days_for_work: int
        :return: A :class:'Homework', which represent homeworks
        :rtype: Homework
        """
        return Homework(text, days_for_work)

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        """Try to add reviewed homework to the storage 'homework_done'

        :param homework_result: homework result
        :type homework_result: __main__.HomeworkResult
        :raises RepeatedResultError: raises an error if homework result had been added earlier to storage
        :return: `True` if attempt was successful, `False` otherwise
        :rtype: bool
        """
        if homework_result in self.homework_done[homework_result.homework]:
            raise RepeatedResultError("This result has been added earlier")
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(self, homework: Homework = None) -> None:
        """Reset homework result in storage or entire storage

        :param homework: a :class:'Homework' objects, which represent homeworks, defaults to None
        :type homework: __main__.Homework, optional
        """
        if homework:
            self.homework_done[homework] = set()
        else:
            self.homework_done.clear()


# if __name__ == "__main__":
#     opp_teacher = Teacher("Daniil", "Shadrin")
#     advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

#     lazy_student = Student("Roman", "Petrov")
#     good_student = Student("Lev", "Sokolov")

#     oop_hw = opp_teacher.create_homework("Learn OOP", 1)
#     docs_hw = opp_teacher.create_homework("Read docs", 5)

#     result_1 = good_student.do_homework(oop_hw, "I have done this hw")
#     result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
#     result_3 = lazy_student.do_homework(docs_hw, "done")
#     try:
#         result_4 = HomeworkResult(good_student, "fff", "Solution")
#     except Exception:
#         print("There was an exception here")
#     opp_teacher.check_homework(result_1)
#     temp_1 = opp_teacher.homework_done

#     # advanced_python_teacher.check_homework(result_1)
#     temp_2 = Teacher.homework_done
#     assert temp_1 == temp_2

#     opp_teacher.check_homework(result_2)
#     opp_teacher.check_homework(result_3)

#     print(Teacher.homework_done[oop_hw])
#     Teacher.reset_results()
