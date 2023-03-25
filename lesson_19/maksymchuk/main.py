from psycopg2.sql import SQL, Identifier, Placeholder

from utils import (
    with_dict_cursor,
    generate_clients,
    generate_main_courses,
)
from constants import TABLES


@with_dict_cursor(user="siznzyoa", password="qqzSmuo7hsD8DeP7l-zWV9A4pqGEOJIh")
def create_table(tables, cur=None):
    for table_name, columns in tables.items():
        # c => ("id", "SERIAL PRIMARY KEY") => "id SERIAL PRIMARY KEY"
        fields = [SQL("{} {}").format(SQL(c[0]), SQL(c[1])) for c in columns]
        print(f"fields: {fields}")

        query = SQL("CREATE TABLE IF NOT EXISTS {tbl_name} ({fields});").format(
            tbl_name=Identifier(table_name),
            fields=SQL(', ').join(fields)
        )

        print(f"query: {query.as_string(cur)}")
        cur.execute(query)


@with_dict_cursor(user="siznzyoa", password="qqzSmuo7hsD8DeP7l-zWV9A4pqGEOJIh")
def fill_table(table: str, data: dict, cur=None):

    query = SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
        table=Identifier(table),
        columns=SQL(", ").join(Identifier(col) for col in data.keys()),
        values=SQL(", ").join(Placeholder() * len(data)),
    )
    print(f"query: {query.as_string(cur)}")
    cur.execute(query, list(data.values()))


if __name__ == "__main__":
    # create_table(TABLES)
    # for client in generate_clients(10):
    #     fill_table("customers", client)
    for main_course in generate_main_courses(10):
        fill_table("main_courses", main_course)
