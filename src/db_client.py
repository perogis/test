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
                        price INTEGER,
                        title CHARACTER VARYING(300),
                        description CHARACTER VARYING,
                        date CHARACTER VARYING(30),
                        city CHARACTER VARYING(10)
                    )''')


def insert_flat(flat):
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            INSERT INTO flats (link, price, title, description, date, city) VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (link) DO UPDATE
            SET
            link = EXCLUDED.link,
            price = EXCLUDED.price,
            title = EXCLUDED.title,
            description = EXCLUDED.description,
            date = EXCLUDED.date,
            city = EXCLUDED.city
            ''', (flat.link, flat.price, flat.title, flat.description, flat.date, flat.city))
