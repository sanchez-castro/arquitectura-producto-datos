"""ELT DAG for Baseball"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.models import Variable
from datetime import datetime
from baseball.get_pitches import get_pitches
import os

args = {
    'owner': 'Jake Klein',
    'email': 'JakeKlein94@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}
path = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(path, 'sql')
elt_path = os.path.join(sql_path, 'elt')
ddl_path = os.path.join(elt_path, 'ddl.sql')
ddl = open(ddl_path, mode='r').read()

params = {
    'bucket': Variable.get("bucket"),
    'folder': 'baseball',
    'project_id': Variable.get("project_id")
}

dag = DAG(
    dag_id='baseball_elt_dag',
    default_args=args,
    schedule_interval='0 12 * * *',
    start_date=datetime(2022, 3, 19),
    catchup=True,
    max_active_runs=1
)

extract_load_task = PythonOperator(
    dag=dag,
    task_id = 'EL_task',
    provide_context=True,
    python_callable=get_pitches,
    op_kwargs={'bucket': params['bucket'], 'path': params['folder']}
)

transform_task = BigQueryOperator(
    dag=dag,
    params=params,
    task_id = 'transform_task',
    use_legacy_sql=False,
    sql=ddl
)

extract_load_task >> transform_task
