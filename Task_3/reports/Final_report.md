#### Case study: task 3

The goal of this task was to retrieve the information about 
the students who scored a 4 and above on their algebra exam. 

Database was created using [script](../src/data/make_database.py).
SQL query to retrieve the information: 

        querry = (
                """
                SELECT * FROM exam_results
                INNER JOIN students ON exam_results.student_id = students.student_id
                INNER JOIN class_catalogue ON exam_results.class_id = class_catalogue.class_id
                WHERE exam_results.grade >= 4 AND class_catalogue.class_name = 'algebra'
                """)

Query result [is here](query_result.html).