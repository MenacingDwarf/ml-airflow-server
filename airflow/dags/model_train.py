from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

HOME_DIR = '/home/stanislav/Hadoop/dags/text_classification'

def deploy_model():
    print("DEPLOY MODEL!!!")

default_args = {
    'owner': 'MenacingDwarf',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
 
with DAG(
    dag_id='text_classification_training',
    default_args=default_args,
    description='This dag will download neccessary for training data, retrain model and save its parameters to the ML flow',
    start_date=datetime(2021, 12, 22, 20),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='download_data',
        bash_command=f'bash {HOME_DIR}/scripts/load_data.sh '
    )
    
    task2 = BashOperator(
        task_id='preprocessing',
        bash_command=f'bash {HOME_DIR}/scripts/data_preprocessing.sh '
    )
    
    task3 = BashOperator(
        task_id='train_model',
        bash_command=f'bash {HOME_DIR}/scripts/train_model.sh '
    )
    
    task1 >> task2 >> task3
 
