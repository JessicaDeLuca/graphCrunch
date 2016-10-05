import psycopg2
from config import config


def create_table():
    commands = (
    '''
        CREATE TABLE cb_news (
            uuid VARCHAR(1024),
            company VARCHAR(1024),
            title VARCHAR(1024),
            news_url VARCHAR(1024),
            author VARCHAR(1024),
            posted_on date,
            created_at int,
            updated_at int);
'''

conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
