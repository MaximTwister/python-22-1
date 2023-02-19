import annotate
import calendar
from abc import ABC, abstractmethod
from datetime import datetime
from Constants import YEAR, MONTH, DAY


class Calendar(ABC):
    def date(self, year: int) -> None:
        print(calendar.TextCalendar(0).formatyear(year))

    @abstractmethod
    def celebration(self, year: int, month: int, day: int) -> None:
        pass

    @abstractmethod
    def duration_from_now(self, year: int, month: int, day: int) -> None:
        pass


class Holidays(Calendar):

    def celebration(self, year: int, month: int, day: int) -> None:
        if calendar.weekday(year, month, day) == 0 or calendar.weekday(year, month, day) == 6:
            print(f"The day {YEAR}-{MONTH}-{DAY} is a day off")
        else:
            print(f"The day {YEAR}-{MONTH}-{DAY} isn`t a day off")
        print(Calendar.__annotations__.get('year'))
        print(Holidays.__annotations__.get('month'))
        print(Holidays.__annotations__.get('day'))

    def duration_from_now(self, year: int, month: int, day: int) -> None:
        day_to = datetime(year=year, month=month, day=day)
        if day_to > datetime.now():
            diff = (day_to - datetime.now())
            print(f"Before the date {YEAR}-{MONTH}-{DAY} {diff.days} days")
        else:
            print("This date isn`t correctly")


q = Holidays()
q.date(YEAR)
q.celebration(YEAR, MONTH, DAY)
q.duration_from_now(YEAR, MONTH, DAY)
