from homework6.task1 import User


class User2(User):
    def __new__(cls, a):
        return super(cls, cls).__new__(cls)

    def __init__(self, a):
        super().__init__()


def test_from_example1():
    assert User.get_created_instances() == 0


def test_from_example2():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0


def test_for_class_passed_in_reset_counter():
    user, _, _ = User(), User(), User()

    assert User.get_created_instances() == 3
    assert User.reset_instances_counter() == 3
    user.get_created_instances() == 0
    assert User.get_created_instances() == 0


def test_for_child_class():
    assert User2.get_created_instances() == 0
    User2("test")
    assert User2.get_created_instances() == 1
    assert User.get_created_instances() == 0
