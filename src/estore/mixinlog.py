class MixinLog:
    """Миксин для вывода информации об объекте при создании объекта"""

    def __init__(self, *args):
        self.__init_args = args
        # print(f"Создан объект класса {self.__class__.__name__} с аргументами: {args}")
        print(repr(self))

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"<{class_name}{self.__init_args}>"
