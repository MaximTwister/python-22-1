from typing import Callable

import psycopg2
from psycopg2.extras import DictCursor, DictRow
from psycopg2.sql import Identifier, SQL


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


@with_dict_cursor(user="siznzyoa", password="qqzSmuo7hsD8DeP7l-zWV9A4pqGEOJIh")
def select_table_data(table_name=None, rows_amount=0, cur=None):

    if table_name is None:
        print("error: no table name was provided.")
        return False
    if cur is None:
        print("error: no cursor was provided.")
        return False

    cur.execute(f"SELECT * FROM {table_name};")

    if rows_amount > 0:
        rows = cur.fetchmany(size=rows_amount)
    else:
        rows = cur.fetchall()

    for row in rows:
        row: DictRow
        for column_name, column_value in row.items():
            print(f"Column: {column_name} with value: {column_value}")


@with_dict_cursor(user="siznzyoa", password="qqzSmuo7hsD8DeP7l-zWV9A4pqGEOJIh")
def insert_table_data(table_name=None, user_names=[], cur=None):
    if table_name is None:
        print("error: no table name was provided.")
        return False
    if cur is None:
        print("error: no cursor was provided.")
        return False

    for user in users:
        q = SQL("INSERT INTO {table_name} ({columns}) VALUES (%s)").format(
            table_name=Identifier(table_name),
            columns=Identifier("customer_name"),
        )

        print(f"raw query: {q.as_string(cur)}")
        cur.execute(q, (user,))


@with_dict_cursor(user="siznzyoa", password="qqzSmuo7hsD8DeP7l-zWV9A4pqGEOJIh")
def is_user_privileged(username=None, cur=None):
    if username is None:
        print("error: no cursor was provided.")
        return False
    if cur is None:
        print("error: no cursor was provided.")
        return False

    # WHERE customer_name = '{username}';")
    stmt = SQL("SELECT {column_name} FROM {table_name} WHERE {customer_name}=%s").format(
            column_name=Identifier("is_privileged"),
            table_name=Identifier("customer"),
            customer_name=Identifier("customer_name"),
        )

    print(f"Raw SQL query: {stmt.as_string(cur)}")
    cur.execute(stmt, (username,))

    try:
        res = cur.fetchone()
    except psycopg2.ProgrammingError as e:
        print(f"got error: {e}")
        print(f"error: customer: {username} is not exists")
        return False

    print(f"is {username} a privileged user: {res}")


# select_table_data(table_name="customer", rows_amount=2)

users = ['Lisa Simpson', 'Flint Stone']
insert_table_data(table_name="customer", user_names=users)


# is_user_privileged(username="Hanna Foe")
# is_user_privileged(username="Administrator")
# # -- defuse snippet
# is_user_privileged(username="';select true;--")
# injection = "';update customer set is_privileged = 'true' where customer_name = 'Maksym'; select true; --"
# contr_injection = "';update customer set is_privileged = 'false' where customer_name = 'Administrator'; select true; --"
# is_user_privileged(username=injection)
# is_user_privileged(username=contr_injection)
# is_user_privileged(username="Maksym")
# is_user_privileged(username="Administrator")

# SELECT is_privileged FROM customer WHERE customer_name = ''; SELECT true; --;

# "';SELECT FROM in;" -> I close the string

# field_names = ["id", "customer_name"]
# field_descr = ["SERIAL PRIMARY KEY", "VARCHAR(50) NOT NULL"]
#
# field = f"{field_names[0]} {field_descr[0]}"
#
# query = SQL(
#     "CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
# ).format(
#     table_name=Identifier("boom"),
#     fields=SQL(",").join(fields)
# )
