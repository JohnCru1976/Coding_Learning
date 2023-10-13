''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

import sqlite_connection as sc
import sqlite_tables as st

def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task: Tuple (priority, begin_date, end_date, id)
    :return: 
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

if __name__ == "__main__":
    # Connection object
    sc.db_connection = sc.create_connection_disk(sc.db_path)

    # Create tables
    st.create_tables()

    # UPDATE Task - (priority, begin_date, end date, id)
    update_task(sc.db_connection, (3, '2023-01-04', '2023-01-06', 2))
