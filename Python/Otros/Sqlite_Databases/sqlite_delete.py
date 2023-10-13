''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

import sqlite_connection as sc
import sqlite_tables as st

def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

if __name__ == "__main__":
    # Connection object
    sc.db_connection = sc.create_connection_disk(sc.db_path)

    # Create tables
    st.create_tables()

    # Delete tasks
    delete_task(sc.db_connection, 2)
    # delete_all_tasks(sc.db_connection)
