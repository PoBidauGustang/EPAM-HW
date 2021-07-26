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
    class InnerClass(cls):
        counter = 0

        @classmethod
        def init_counter(cls):
            if "counter" not in cls.__dict__:
                cls.counter = 0

        def __init__(self, *args, **kwargs):
            self.init_counter()
            super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        @classmethod
        def get_created_instances(cls):
            cls.init_counter()
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            cls.init_counter()
            try:
                return cls.counter
            finally:
                cls.counter = 0

    return InnerClass


@instances_counter
class User:
    pass


# if __name__ == "__main__":

#     User.get_created_instances()  # 0
#     user, _, _ = User(), User(), User()
#     assert user.get_created_instances() == 3  # 3
#     # user.reset_instances_counter()  # 3

#     class User2(User):
#         def __init__(self, a):
#             self.a = a
#             super().__init__()

#     # print(User2.__dict__)
#     assert User2.get_created_instances() == 0
#     User2("test")
#     assert User2.get_created_instances() == 1
#     print(User.get_created_instances())
