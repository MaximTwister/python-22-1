from abc import ABC, abstractmethod


class TestAbstractCls(ABC):

    @abstractmethod
    def method_1(self, x: int, y: int):
        pass

    @abstractmethod
    def method_2(self, name: str, last_name: str):
        pass


def check_annotations(func):
    def wrapper(*args):
        data_type_in_func = list(func.__annotations__.values())
        print(f"-> origin data type of {func.__name__} is next : {data_type_in_func}")
        c = [*args]
        data_type_got_for_user = [type(el) for el in c].pop(2)
        if data_type_got_for_user in data_type_in_func:
            print(f"Yes! The data type you entered for {func.__name__} matches the function types!")
            return func(*args)
        else:
            print("Your entered wrong data type!\n")
    return wrapper


class ChildTestAbstractCls(TestAbstractCls):
    def __init__(self, name=None, last_name=None, x=None, y=None):
        self.name = name
        self.last_name = last_name
        self.x = x
        self.y = y

    @check_annotations
    def method_1(self, x: int, y: int) -> int:
        res = x + y
        print(f"{x} + {y} = {res}")
        return res

    @check_annotations
    def method_2(self, name: str, last_name: str) -> str:
        res = "Hello, " + name + " " + last_name + "!"
        print(res)
        return res


def main():
    test_obj = ChildTestAbstractCls()
    test_obj.method_1(2, 3)
    test_obj.method_2("John", "Doe")


if __name__ == "__main__":
    main()

