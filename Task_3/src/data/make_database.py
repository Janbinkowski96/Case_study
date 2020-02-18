import sqlite3
import pandas as pd
import os


def connect():
    """Function to create / connect with database and return cursor"""
    connection = sqlite3.connect("../../database/db.db")
    cursor = connection.cursor()

    return cursor, connection


def create_tables(cursor):
    """Function to create tables if not exist"""

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        student_id INT NOT NULL,
        name varchar(200) NOT NULL,
        surname varchar(200) NOT NULL,
        birth_date date NOT NULL,
        faculty varchar(200) NOT NULL);
        
        CREATE TABLE IF NOT EXISTS exam_results (
        id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        student_id INT NOT NULL,
        class_id INT NOT NULL,
        exam_date date NOT NULL,
        grade float NOT NULL);
        
        CREATE TABLE IF NOT EXISTS class_catalogue (
        id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        class_id INT NOT NULL,
        class_name varchar(200) NOT NULL,
        professor_id INT NOT NULL,
        semester varchar(200) NOT NULL)
    """)


def get_tables_from_file():
    """Function to load tables from file"""
    tables_list = os.listdir("tables_raw_format")
    raw_inserts = {}

    for table in tables_list:
        insert = pd.read_csv("tables_raw_format/{}".format(table)).values.tolist()

        table_name = table.split(".")[0]
        raw_inserts.update({table_name: insert})

    return raw_inserts


def fill_tables(cursor, connection, students=None, exam_results=None,
                class_catalogue=None):
    """Function to fill tables"""

    cursor.executemany("""INSERT INTO students 
    (student_id, name, surname, birth_date, faculty) VALUES (?, ?, ?, ?, ?)""", students)

    cursor.executemany("""INSERT INTO exam_results 
    (student_id, class_id, exam_date, grade) VALUES (?, ?, ?, ?)""", exam_results)

    cursor.executemany("""INSERT INTO class_catalogue 
    (class_id, class_name, professor_id, semester) VALUES (?, ?, ?, ?)""", class_catalogue)

    connection.commit()


if __name__ == '__main__':
    curr, conn = connect()
    create_tables(curr)
    raw_insert = get_tables_from_file()
    fill_tables(curr, conn, **raw_insert)
