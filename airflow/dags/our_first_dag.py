from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import requests

HOME_DIR = '/home/stanislav/Hadoop'

def deploy_model():
    requests.post('http://127.0.0.1:5005/reload')

default_args = {
    'owner': 'MenacingDwarf',
    'retries': 5,
    'retry_delay': timedelta(seconds=5)
}
 
with DAG(
    dag_id='model_training_dag_v11',
    default_args=default_args,
    description='This dag will download neccessary for training data, retrain model and save its parameters to the ML flow',
    start_date=datetime(2021, 12, 21, 20),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='download_data',
        bash_command=f'bash {HOME_DIR}/scripts/load_data.sh '
    )
    
    task2 = BashOperator(
        task_id='train_model',
        bash_command=f'bash {HOME_DIR}/scripts/train_model.sh '
    )
    
    task3 = PythonOperator(
        task_id='deploy_model',
        python_callable=deploy_model
    )
    
    task1 >> task2 >> task3
 
