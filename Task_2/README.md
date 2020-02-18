Case Study: Task 2
==============================

Aim of this task is to create binary classification model for headline type (sarcastic / not sarcastic) based on headline content.
Final report is available form [here](reports/Final_report.md)
### How to run
If the requirements for the python and jupyter notebook versions are done, to run 
notebooks you need to install [requirements](requirements.txt) using pip3 or conda.

        pip3 install -r requirements.txt
        conda install --file requirements.txt

When requirements are collected, you can use notebooks, the flow of work is:
1) [Data processing](notebooks/Data_processing.ipynb) (this part of work was carried out in google cloud instance
                                                        because of high resource consumption by distilBERT)       
2) [Classification](notebooks/Classification.ipynb)

Additional files such as models, metrics, interim and processed data are generated during the notebooks work.

Project Organization
------------



    ├── README.md          <- README.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   │   │
    │   │   │── distilBERT_output <- packages with data to train final model
    │   │
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original data.
    │
    │
    ├── models             <- Trained model.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    │
    ├── reports            <- Generated analysis.
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
