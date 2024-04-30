import psycopg2
from config import load_config
from connect import connect

def create_func():
    # creating function in PostgreSql database
    commands =(
            """
            CREATE OR REPLACE FUNCTION  get_contLocation_by_name(name_pattern VARCHAR)
            RETURNS TABLE (name VARCHAR, city VARCHAR , address VARCHAR ) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT name, city, address FROM contacts_location
            WHERE name LIKE name_pattern;

            END ;$$

            LANGUAGE plpgsql;
            """,
            """
            CREATE OR REPLACE FUNCTION get_all_by_name(name_pattern VARCHAR)
            RETURNS TABLE (name VARCHAR, phone_number VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT name, phone_number FROM contacts
            WHERE name LIKE name_pattern;

            END ;$$

            LANGUAGE plpgsql;
            """,
            """
            CREATE OR REPLACE FUNCTION get_with_pagination(limit INT, offset INT)
            RETURNS TABLE (name VARCHAR, phone_number VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT name, phone_number FROM contacts
            ORDER BY name
            LIMIT limit, OFFSET offset;

            END ;$$

            LANGUAGE plpgsql;
            """
    )
    try:
        config = load_config()
        with connect(config) as conn :
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError,Exception ) as error:
        print(error)

if __name__ == "__main__":
    create_func()