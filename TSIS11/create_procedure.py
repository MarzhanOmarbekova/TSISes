import psycopg2
from config import load_config
from connect import connect

def create_proc():
    # creating procedure in PostgreSql database
    commands = (
        """
        CREATE OR REPLACE PROCEDURE add_new_contact(
            new_name VARCHAR, 
            new_phone_num VARCHAR
            ) 
        AS $$
        BEGIN 
            INSERT INTO contacts(name, phone_number)
            VALUES(new_name, new_phone_num)
            ON CONFLICT (name)
            DO UPDATE SET  EXCLUDED
        END;
        $$
        LANGUAGE PLPGSQL;
        """,
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
    create_proc()