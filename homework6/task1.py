#!/usr/bin/python3
"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.counter = 0

    def __new__(parent):
        cls.init_counter()
        obj = super(cls, cls).__new__(cls)
        parent.counter += 1
        return obj

    @classmethod
    def init_counter(cls):
        if "counter" not in cls.__dict__:
            cls.counter = 0

    @classmethod
    def get_created_instances(cls):
        cls.init_counter()
        return cls.counter

    @classmethod
    def reset_instances_counter(cls):
        cls.init_counter()
        tmp_counter = cls.counter
        cls.counter = 0
        return tmp_counter

    cls.__new__ = __new__
    cls.init_counter = init_counter
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls


@instances_counter
class User:
    pass


# if __name__ == "__main__":

#     User.get_created_instances()  # 0
#     user, _, _ = User(), User(), User()
#     assert user.get_created_instances() == 3  # 3
#     # user.reset_instances_counter()  # 3

#     class User2(User):
#         def __new__(cls, a):
#             return super(cls, cls).__new__(cls)
#         def __init__(self, a):
#             super().__init__()

#     assert User2.get_created_instances() == 0
#     User2("test")
#     assert User2.get_created_instances() == 1
#     print(User.get_created_instances())
