''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

from types import NoneType
from typing import Union
import os
import sqlite3
from sqlite3 import Error
from pathlib import Path

# Set the working directory on the file directory
file_directory = os.path.dirname(__file__)
os.chdir(file_directory)

# Test database path
db_path = str(Path("./") / "test.db")
# Connection variable
db_connection: Union[sqlite3.Connection, NoneType]

def create_connection_disk(db_file: str) -> Union[sqlite3.Connection, NoneType]:
    '''Create a connection to a sSQLite database in the DISK
    Returns a Connection object
    If there is an error returns None'''
    connection: Union[sqlite3.Connection, NoneType]

    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        connection = None

    return connection

def create_connection_ram() -> Union[sqlite3.Connection, NoneType]:
    '''Create a connection to a SQLite database in the RAM
    Returns a Connection object
    If there is an error returns None'''
    connect: Union[sqlite3.Connection, None]

    try:
        connect = sqlite3.connect(":memory:")
    except Error as e:
        print(e)
        connect = None

    return connect

if __name__ == "__main__":
    ## TESTS ##
    db_connection = create_connection_ram()
    print(db_connection)
    if db_connection:
        db_connection.close()
    db_connection = create_connection_ram()
    print(db_connection)
    if db_connection:
        db_connection.close()
