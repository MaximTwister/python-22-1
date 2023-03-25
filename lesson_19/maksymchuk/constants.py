TABLES = {
    "customers": (
        ("id", "SERIAL PRIMARY KEY"),
        ("customer_name", "VARCHAR(50)"),
        ("email", "VARCHAR(50)"),
    ),
    "main_courses": (
        ("id", "SERIAL PRIMARY KEY"),
        ("main_course_name", "VARCHAR(50)"),
        ("price", "NUMERIC(10, 2)"),
    ),
    "drinks": (
        ("id", "SERIAL PRIMARY KEY"),
        ("drink_name", "VARCHAR(50)"),
        ("price", "NUMERIC(10, 2)"),
    )
}
