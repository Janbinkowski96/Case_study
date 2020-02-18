import pandas as pd
import sqlite3


def start_connection():
    """Function to connect with database"""

    connect = sqlite3.connect("../database/db.db")
    return connect


def send_query(connect):
    """Function to send query to database"""

    querry = (
    """
    SELECT * FROM exam_results
    INNER JOIN students ON exam_results.student_id = students.student_id
    INNER JOIN class_catalogue ON exam_results.class_id = class_catalogue.class_id
    WHERE exam_results.grade >= 4 AND class_catalogue.class_name = 'algebra'
    """)

    full_data = pd.read_sql_query(querry, con=connect)
    return full_data


def prepare_output(full_data):
    """Function to print and save results of query"""
    print(full_data)
    full_data.to_html("../reports/query_result.html")


if __name__ == "__main__":
    con = start_connection()
    full_data = send_query(con)
    prepare_output(full_data)
