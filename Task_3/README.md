Case study: task 3
==============================

The goal is to write a SQL query, in which you will retrieve the information about the students who scored a 4 and above on their algebra exam.

If the requirements for the python and jupyter notebook versions are done, to run 
code you need to install [requirements](requirements.txt) using pip3 or conda.

        pip3 install -r requirements.txt
        conda install --file requirements.txt

When requirements are collected, you can use notebooks and scripts, the flow of work is:
1) create database by run [make_database.py](src/data/make_database.py) script in project directory.

        1.1) cd src/data 
        2.2) python3 make_database.py
        or use && to join 2.1 and 2.2 elements (for linux)

2) to send a query you can use [script](src/send_query.py) or [notebook](notebooks/SQL_Querry.ipynb). To use script
as above, open directory and run script.

        2.1) cd src/
        2.2) python3 send_query.py


Final report is available from [here](reports/Final_report.md).
Query result is available from [here](reports/query_result.html)

Project Organization
------------

    ├── README.md          <- README.
    ├── database           <- Database location [empty on remote repository]
    │
    ├── reports            <- Generated analysis.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.
    │
    ├── src                <- Source code for use in this project.
        │
        ├── data           <- Scripts to generate data.
             └── make_database.py <- Scripts to generate data base in ../../database/ location.
             └── tables_raw_format <- Directory with tables in *.csv sheets.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
