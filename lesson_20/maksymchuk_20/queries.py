from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    and_,
    func
)

from lesson_20.maksymchuk_20.main import (
    engine,
    Airport,
    Flight,
)

Session = sessionmaker(bind=engine)
session = Session()


def airports_with_departures_between(start_date, end_date):
    # dd-mm-yyyy
    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")

    print(f"Start date object: {start_date_obj}")
    print(f"End date object: {end_date_obj}")

    a = session.query(Airport).join(Flight, Airport.id == Flight.departure_airport_id).filter(
        and_(Flight.tod >= start_date_obj, Flight.tod <= end_date_obj)
    ).all()

    return a


airports = airports_with_departures_between(start_date="21-03-2023", end_date="22-03-2023")
print(airports)


def flights_longer_than(hours):
    duration = timedelta(hours=hours)
    q = session.query(Flight).filter(
        Flight.toa - Flight.tod > duration
    ).all()
    return q


flights = flights_longer_than(2)
# print(f"long flights: {flights}")


def flight_by_number(number):
    f = session.query(Flight).filter(Flight.flight_number == number).all()
    return f


flight = flight_by_number(number="FQ772")


def flights_by_departure_id(departure_id):
    f = session.query(func.count(Flight.id)).filter(Flight.departure_airport_id == departure_id).all()
    return f


flights = flights_by_departure_id(departure_id=6)
# print(flights)


def calculate_flight_time():
    durations = session.query(func.timestampdiff("second", Flight.tod, Flight.toa)).all()
    print(durations)


calculate_flight_time()
