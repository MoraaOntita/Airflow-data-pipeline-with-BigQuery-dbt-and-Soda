# Creating a data pipeline

from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule= None, #we are triggering the data pipeline manually
    catchup=False,
    tags=['retail'], #tags are useful to categorize and filter data pipelines on the airflow UI
)

