Case Study: Task 1
==============================

The goal of this task is to build a model to classify iris species.
### How to run
If the requirements for the python and jupyter notebook versions are done, to run 
notebooks you need to install [requirements](requirements.txt) using pip3 or conda.

        pip3 install -r requirements.txt
        conda install --file requirements.txt

When requirements are collected, you can use notebooks, the flow of work is:
1) [Pre-processing](notebooks/Preprocessing.ipynb)
2) [Standarization](notebooks/Standardization.ipynb)
3) [Training](notebooks/Training_models.ipynb)
4) [Models evaluation](notebooks/Models_evalutaion_and_comparison.ipynb)

The interim and processed data, models, metrics and figures are generated during notebooks work.

[General report for this task is available from here](reports/Final_report.md)

Project Organization
------------

    ├── README.md          <- README.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    │
    ├── reports            <- Generated analysis. And the final report.
    │   └── figures        <- Generated figures.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
  
 
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
