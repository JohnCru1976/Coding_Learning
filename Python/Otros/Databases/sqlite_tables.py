''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

import sqlite_connection as sc



if __name__ == "__main__":
    sc.db_connection = sc.create_connection_disk(sc.db_path)
