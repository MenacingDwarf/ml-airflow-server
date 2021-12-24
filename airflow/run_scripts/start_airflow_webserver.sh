source venv/bin/activate
export AIRFLOW_HOME=.
airflow db init
airflow webserver
