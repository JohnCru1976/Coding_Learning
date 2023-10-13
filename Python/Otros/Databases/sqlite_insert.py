''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

import sqlite_connection as sc
import sqlite_tables as st

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn: sqlite3.Connection
    :param project: Tuple (name,begin_date,end_date)
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn: sqlite3.Connection object
    :param task: Tuple (name,priority,status_id,project_id,begin_date,end_date)
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid

if __name__ == "__main__":
    # Connection object
    sc.db_connection = sc.create_connection_disk(sc.db_path)

    # Create tables
    st.create_tables()
   
    # create a new project
    project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
    project_id = create_project(sc.db_connection, project)

    # tasks
    task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
    task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

    # create tasks
    task_1_id = create_task(sc.db_connection, task_1)
    task_2_id = create_task(sc.db_connection, task_2)
    