"""Predcition DAG for Baseball"""

from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.models import Variable
from datetime import datetime
import os

args = {
    'owner': 'Jake Klein',
    'email': 'JakeKlein94@gmail.com',
    'retries': 2,
    'depends_on_past': True,
}
path = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(path, 'sql')
predictions_path = os.path.join(sql_path, 'transverse_spin')
ddl_path = os.path.join(predictions_path, 'ddl.sql')
ddl = open(ddl_path, mode='r').read()
features_path= os.path.join(predictions_path, 'features.sql')
features = open(features_path, mode='r').read()
predictions_path= os.path.join(predictions_path, 'predictions.sql')
predictions = open(predictions_path, mode='r').read()

params = {
    'bucket': Variable.get("bucket"),
    'folder': 'baseball',
    'project_id': Variable.get("project_id"),
    'features_table': 'transverse_spin_features',
    'predictions_table': 'transverse_spin_predictions'
}

dag = DAG(
    dag_id='baseball_predictions_dag',
    default_args=args,
    schedule_interval='0 12 * * *',
    start_date=datetime(2022, 3, 19),
    catchup=True,
    max_active_runs=1
)

# Task 1: External Task Sensor on ELT
task1 = ExternalTaskSensor(
    dag=dag,
    task_id='elt_task_sensor',
    external_dag_id='baseball_elt_dag',
    external_task_id='transform_task'
)
# Task 2: Run DDL
task2 = BigQueryOperator(
    dag=dag,
    params=params,
    task_id='ddl_task',
    sql=ddl,
    use_legacy_sql=False
)
# Task 3: Generate Features
task3 = BigQueryOperator(
    dag=dag,
    params=params,
    task_id='features_task',
    sql=features,
    use_legacy_sql=False
)
# Task 4: Generate Predictions
task4 = BigQueryOperator(
    dag=dag,
    params=params,
    task_id='predictions',
    sql=predictions,
    use_legacy_sql=False
)
task1 >> task2 >> task3 >> task4
