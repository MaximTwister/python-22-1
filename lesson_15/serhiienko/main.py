from abc import ABC, abstractmethod


def check_typing(func):
    def wrapper(*args, **kwargs):
        return_type = func.__annotations__["return"]
        array_types = [{key: ttype} for key, ttype in func.__annotations__.items() if not key == "return"]

        if args:
            for index in range(len(args) - 1):
                typing = [item for item in array_types[0].values()][0]
                if not isinstance(args[index + 1], typing):
                    raise TypeError(f"Param {index} must be type {typing}")

        if kwargs:
            for obj_type in array_types:
                for key, typing in obj_type.items():
                    if not isinstance(kwargs[key], typing):
                        raise TypeError(f"Param {key} must be type {typing}")

        result = func(*args, **kwargs)

        if not isinstance(result, return_type):
            raise TypeError(f"Return value must be type {return_type}")

        return result
    return wrapper


class Figure(ABC):
    @abstractmethod
    def calc_area(self, width: int | float) -> int | float:
        pass

    @abstractmethod
    def calc_volume(self, width: int | float) -> int | float:
        pass


class Square(Figure):
    @check_typing
    def calc_area(self, width: int | float) -> int | float:
        return width**2

    @check_typing
    def calc_volume(self, width: int | float) -> int | float:
        return width**3


def main():
    square = Square()
    print("volume", square.calc_volume(5))
    print("area", square.calc_area(5))


main()
