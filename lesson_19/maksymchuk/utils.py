from random import uniform
from typing import Callable

import psycopg2
from faker import Faker
from psycopg2.extras import DictCursor

from providers import main_courses_provider

fkr = Faker()
fkr.add_provider(main_courses_provider)


def with_dict_cursor(**creds):
    def with_cursor_decorator(f: Callable) -> Callable:
        def with_cursor_wrapper(*args, **kwargs):
            connection_data = {"dbname": "siznzyoa", "host": "mahmud.db.elephantsql.com"}
            connection_data.update(creds)
            conn = psycopg2.connect(**connection_data)
            cur = conn.cursor(cursor_factory=DictCursor)

            try:
                f(*args, **kwargs, cur=cur)
            except Exception as e:
                conn.rollback()
                print(f"SQL query failed with error: {e}")
                raise e
            else:
                conn.commit()
            finally:
                cur.close()
                conn.close()

        return with_cursor_wrapper
    return with_cursor_decorator


def generate_clients(amount=1):
    clients = []
    for _ in range(amount):
        profile = fkr.profile()
        client = {
            "customer_name": profile.get("name"),
            "email":  profile.get("mail"),
        }
        clients.append(client)

    return clients


def generate_main_courses(amount=1):
    main_courses = []
    for _ in range(amount):
        main_course = {
            "main_course_name": fkr.main_course(),
            "price": round(uniform(15.00, 40.00), 2)
        }
        main_courses.append(main_course)

    return main_courses
