import psycopg2
from connect import connect
from config import load_config

def get_contacts(name):
    contacts = []
    config = load_config()

    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_all_by_name' ,(name, ))

                rows = cur.fetchall()
                for row in rows:
                    contacts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        return contacts
    
def get_contacts_locations(name):
    contacts = []
    config = load_config()

    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_contLocation_by_name' , (name,))

                rows = cur.fetchall()
                for row in rows:
                    contacts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        return contacts
    
if __name__ == '__main__':
    print(get_contacts((f'%r%',)))
    print(get_contacts_locations((f'%r%',)))