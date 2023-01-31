from application.services.db_connection import DBConnection


def create_table():
    with DBConnection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phones (
                    pk INTEGER NOT NULL PRIMARY KEY,
                    contact_name VARCHAR NOT NULL,
                    phone value INTEGER NOT NULL
                    )
            """
            )
