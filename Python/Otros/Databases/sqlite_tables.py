''' Here I practise with sqlite using the link
https://www.sqlitetutorial.net/sqlite-python/
'''

import sqlite_connection as sc

# Se crean variables con el código SQL para la creación de las tablas
sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                ); """

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        # El objeto cursor es una interfaz entre la BD y la aplicación
        # Su objeto es permitir realizar consultas y recuperar datos 
        c = conn.cursor()
        c.execute(create_table_sql)
    except sc.Error as e:
        print(e)

def create_tables():
     # create tables
    if sc.db_connection:
        # create projects table
        create_table(sc.db_connection, sql_create_projects_table)

        # create tasks table
        create_table(sc.db_connection, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == "__main__":
    # Connection object
    sc.db_connection = sc.create_connection_disk(sc.db_path)

    # create tables
    if sc.db_connection:
        # create projects table
        create_table(sc.db_connection, sql_create_projects_table)

        # create tasks table
        create_table(sc.db_connection, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

