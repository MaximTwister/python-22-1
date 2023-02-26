from abc import ABC, abstractmethod
from typechecker import typechecker


class AbstractClass(ABC):

    @abstractmethod
    def abstract_method_one(self, param_string: str, param_tuple: tuple) -> list:
        pass

    @abstractmethod
    def abstract_method_two(self, param_integer: int, param_list: list) -> tuple:
        pass


class Implementor(AbstractClass):

    @typechecker
    def abstract_method_one(self, a: str, b: tuple) -> list:
        return [1, 23]

    @typechecker
    def abstract_method_two(self, a: int, b: list) -> tuple:
        return ("a", 1)


i = Implementor()
i.abstract_method_one("33", (1, 2, 3))
i.abstract_method_two(456, ["DOG"])
