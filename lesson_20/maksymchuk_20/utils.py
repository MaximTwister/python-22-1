from random import choices, choice, uniform
from string import ascii_uppercase
from datetime import timedelta

from faker import Faker
from sqlalchemy.orm import sessionmaker

from lesson_20.maksymchuk_20.main import (
    engine,
    Airport, Flight,
)

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

# 4 Letters in UpperCase
icao_codes = [''.join(choices(ascii_uppercase, k=4)) for _ in range(20)]
airports = []

for icao_code in icao_codes:
    airport = Airport(name=faker.city(), icao=icao_code)
    airports.append(airport)
    session.add(airport)


session.commit()

for _ in range(20):
    departure_airport = choice(airports)
    arrival_airport = choice(airports)

    while departure_airport == arrival_airport:
        arrival_airport = choice(airports)

    tod = faker.date_time_this_month()
    flight_time_minutes = round(uniform(1, 5), 1) * 60
    flight_delta = timedelta(minutes=flight_time_minutes)
    toa = tod + flight_delta

    flight_number = faker.bothify(text="??###", letters=ascii_uppercase)

    flight = Flight(
        flight_number=flight_number,
        departure_airport_id=departure_airport.id,
        arrival_airport_id=arrival_airport.id,
        tod=tod,
        toa=toa,
    )

    session.add(flight)

session.commit()
session.close()
