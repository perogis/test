import psycopg2

DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "postgres"
HOST = "localhost"


def create_flats_table():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
                    CREATE TABLE IF NOT EXISTS flats(
                        id serial PRIMARY KEY,
                        link CHARACTER VARYING(300),
                        price CHARACTER VARYING,
                        title CHARACTER VARYING(300),
                        description CHARACTER VARYING,
                        date CHARACTER VARYING(100),
                        city CHARACTER VARYING(10),
                        images CHARACTER VARYING,
                        email CHARACTER VARYING(100)
                    )''')


def insert_flat(flat):
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            INSERT INTO flats (link, price, title, description, date, city, images, email) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (flat.link, flat.price, flat.title, flat.description, flat.date, flat.city, flat.images, flat.emeil))

 # create_flats_table()