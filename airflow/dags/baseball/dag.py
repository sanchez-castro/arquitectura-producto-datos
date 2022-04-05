"""ELT DAG for Baseball"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from baseball.get_pitches import get_pitches

args = {
    'owner': 'Jake Klein',
    'email': 'JakeKlein94@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}

params = {
    'bucket': Variable.get("bucket"),
    'folder': 'baseball'
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
