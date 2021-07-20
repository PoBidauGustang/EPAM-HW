from homework5.task1 import Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")


def test_initiation_teacher():
    assert teacher.last_name == "Shadrin"


def test_initiation_student():
    assert student.first_name == "Roman"


expired_homework = teacher.create_homework("Learn functions", 0)
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)


def test_homework_attributes_1():
    assert str(expired_homework.deadline) == "0:00:00"


def test_homework_attributes_2():
    assert str(oop_homework.deadline) == "5 days, 0:00:00"


def test_homework_attributes_3():
    assert expired_homework.text == "Learn functions"


def test_student_method(capsys):
    assert not student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
