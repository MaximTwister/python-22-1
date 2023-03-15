from typing import Callable

import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.sql import SQL, Identifier, Composable


def with_dict_cursor(**creds):
    def with_cursor_decorator(f: Callable) -> Callable:
        def with_cursor_wrapper(*args, **kwargs):
            connection_data = {"dbname": "nlupkslc", "host": "mahmud.db.elephantsql.com"}
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


@with_dict_cursor(user="nlupkslc", password="4n-Zvtq9r_WKBvJPuLZjoy5_Fqa1X_oB")
def create_table(table_name, field, cur=None):

    query = SQL(
       "CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
    ).format(
         table_name=table_name,
         fields=SQL(", ".join(field))
    )
    print(f"Raw SQL query: {query.as_string(cur)}")
    cur.execute(query)


@with_dict_cursor(user="nlupkslc", password="4n-Zvtq9r_WKBvJPuLZjoy5_Fqa1X_oB")
def insert_table_data(table_name, data, columns, cur):
    for data_el in data:
        q = SQL('INSERT INTO {table_name} ({columns}) VALUES (%s, %s, %s)').format(
            table_name=Identifier(table_name),
            columns=SQL(',').join([Identifier(colum) for colum in columns]),
        )

        print(f"raw query: {q.as_string(cur)}")
        cur.execute(q, (*data_el, ))


@with_dict_cursor(user="nlupkslc", password="4n-Zvtq9r_WKBvJPuLZjoy5_Fqa1X_oB")
def home_1(cur):

    query = SQL(
       "select customer_id, count(customer_id) from orders group by customer_id order by count desc limit 1;"
    )
    print(f"Raw SQL query: {query.as_string(cur)}")
    cur.execute(query)
    result = cur.fetchall()
    print(f"Result => {result}")


@with_dict_cursor(user="nlupkslc", password="4n-Zvtq9r_WKBvJPuLZjoy5_Fqa1X_oB")
def home_2(cur):

    query = SQL(
       "select avg(order_sum) from orders;"
    )
    print(f"Raw SQL query: {query.as_string(cur)}")
    cur.execute(query)
    result = cur.fetchall()
    print(f"Result => {result}")


field_names = ["customer_id", "name", "mail", "phone"]
field_descr = ["SERIAL PRIMARY KEY", "VARCHAR(50) NOT NULL", "VARCHAR(50) NOT NULL", "VARCHAR(50) NOT NULL"]
field = ["{} {}".format(name, descr) for name, descr in zip(field_names, field_descr)]

create_table(Identifier("customers"), field)

field_names = ["order_id", "order_date", "customer_id", "order_sum"]
field_descr = ["SERIAL PRIMARY KEY", "VARCHAR(50) NOT NULL", "INTEGER NOT NULL", "INTEGER NOT NULL"]
field = ["{} {}".format(name, descr) for name, descr in zip(field_names, field_descr)]
field.append("FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE")

create_table(Identifier("orders"), field)

data = [['Lisa Simpson', 'ssss@gmail.com', "0976545670"], ['Flint Stone', 'flint@gmail.com', "09876759087"]]
insert_table_data(table_name="customers", data=data, columns=["name", "mail", "phone"])

data = [['12.04.2023', '2', 78], ['03.09.2021', '4', 66]]
insert_table_data(table_name="orders", data=data, columns=["order_date", "customer_id", "order_sum"])

home_1()
home_2()
