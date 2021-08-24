import pytest

from homework12.src.orm.models import Homework, HomeworkResult, Student, Teacher


@pytest.mark.parametrize(
    "record, result",
    [
        ("teacher.first_name", "Daniil"),
        ("homework.teacher.first_name", "Daniil"),
        ("student.first_name", "Roman"),
        ("hw_result.student.first_name", "Roman"),
    ],
)
@pytest.mark.django_db
def test_positive(create_tables, record, result):
    """Test that all created records exist in test db"""

    teacher = Teacher.objects.get(first_name="Daniil")
    homework = Homework.objects.get(teacher=teacher.id)
    student = Student.objects.get(first_name="Roman")
    hw_result = HomeworkResult.objects.get(student=student.id)
    assert eval(record) == result


@pytest.mark.django_db
def test_negative(create_tables):
    """Test that attempt to get an empty query throw an exception"""
    with pytest.raises(Exception):
        teacher = Teacher.objects.get(first_name="Noname")
        assert not teacher.first_name == "Noname"
