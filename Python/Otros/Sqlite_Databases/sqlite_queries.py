''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

import sqlite_connection as sc
import sqlite_tables as st

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: cursor.fetchall()
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    return rows

def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return: cursor.fetchall()
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    return rows

if __name__ == "__main__":
    # Connection object
    sc.db_connection = sc.create_connection_disk(sc.db_path)

    # Create tables
    st.create_tables()

    # USING QUERIES
    tasks = select_task_by_priority(sc.db_connection, 3)
    for task in tasks:
        print(task)
    tasks = select_all_tasks(sc.db_connection)
    for task in tasks:
        print(task)