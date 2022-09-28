from pathlib import Path
from loguru import logger
import sqlite3


logger.add('db_log.log')
cwd_path = Path.cwd()
db_path = cwd_path.joinpath('data/pylib_db.db')

if not db_path.exists():
    logger.debug('the code is running for the first time.')
    
    # creating database
    conn = sqlite3.connect('data/pylib_db.db')
    logger.debug('database is created.')
    c = conn.cursor()
    
    # creating tables
    c.execute("""CREATE TABLE members (
            fname text,
            lname text,
            national_id integer,
            email text,
            phone integer,
            age integer,
            edu_level text,
            major text
            )""")
    logger.debug('Table members is correctly made in the data base.')
    c.execute("""CREATE TABLE booklist (
            title text,
            keywords text,
            isbn integer,
            author text,
            total_number,
            available_number
            )""")
    logger.debug('Table booklist is correctly made in the data base.')

    c.execute("""CREATE TABLE barrow_log (
            btitle text,
            user_ID text,
            startdate integer,
            status text,
            returndate text
            )""")
    logger.debug('Table barrow_log is correctly made in the data base.')
    logger.debug(f'database is created in this path: {str(db_path)}')

else:
    logger.debug(f'database is existed in this path: {str(db_path)}')
    