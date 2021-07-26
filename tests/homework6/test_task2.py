import pytest

from homework6.task2 import *


@pytest.fixture
def teachers():
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
    return opp_teacher, advanced_python_teacher


@pytest.fixture
def students():
    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")
    return lazy_student, good_student


@pytest.fixture
def homeworks(teachers):
    opp_teacher = teachers[0]
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    return oop_hw, docs_hw


@pytest.fixture
def results(students, homeworks):
    good_student = students[1]
    lazy_student = students[0]
    oop_hw = homeworks[0]
    docs_hw = homeworks[1]
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    return result_1, result_2, result_3


def test_not_homework_object_passed_in_homework_result(students):
    good_student = students[1]

    with pytest.raises(TypeError, match="You gave a not Homework object"):
        result_4 = HomeworkResult(good_student, "fff", "Solution")


def test_teachers_objects_and_Teacher_class_have_common_data(teachers, results):
    opp_teacher = teachers[0]
    advanced_python_teacher = teachers[1]
    result = results[0]

    opp_teacher.check_homework(result)

    temp_1 = opp_teacher.homework_done
    temp_2 = Teacher.homework_done
    temp_3 = advanced_python_teacher.homework_done
    assert temp_1 == temp_2 == temp_3


def test_reset_the_specific_homeworkresult(teachers, results, homeworks):
    opp_teacher = teachers[0]
    result_1 = results[1]
    result_2 = results[2]
    oop_hw = homeworks[0]

    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)

    Teacher.reset_results(oop_hw)
    assert Teacher.homework_done[oop_hw] == set()


def test_reset_all_homework_results(teachers):
    advanced_python_teacher = teachers[1]

    advanced_python_teacher.reset_results()
    assert not advanced_python_teacher.homework_done


def test_DeadlineError(teachers, students):
    opp_teacher = teachers[0]
    lazy_student = students[0]

    out_of_date_hw = opp_teacher.create_homework("Out of Date Task", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(
            out_of_date_hw, "I did not have time to complete this hw"
        )


def test_second_entry_of_the_same_homework_result_is_not_possible(
    students, homeworks, teachers
):
    good_student = students[1]
    oop_hw = homeworks[0]
    opp_teacher = teachers[0]

    result = good_student.do_homework(oop_hw, "Text for example")
    opp_teacher.check_homework(result)

    with pytest.raises(RepeatedResultError, match="This result has been added earlier"):
        opp_teacher.check_homework(result)
