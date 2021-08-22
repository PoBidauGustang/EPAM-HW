import pytest

from homework12.project.orm.models import Homework, HomeworkResult, Student, Teacher


def create_record_in_db(some_class, **kwargs):
    """Function for creation record in db"""
    instance = some_class(**kwargs)
    instance.save()
    return instance


@pytest.fixture
def create_tables():
    "The fixture creates tables before running tests"
    teacher = create_record_in_db(Teacher, first_name="Daniil", last_name="Shadrin")
    homework = create_record_in_db(Homework, task="ORM", teacher=teacher)
    student = create_record_in_db(Student, first_name="Roman", last_name="Petrov")
    hw_result = create_record_in_db(
        HomeworkResult, homework=homework, solution="hw solution", student=student
    )
    yield
