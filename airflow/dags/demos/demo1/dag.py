"""Demo DAG for using Bash and Python Operators"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago

args = {
    'owner': 'Jake Klein',
    'email': 'JakeKlein94@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}

dag = DAG(
    dag_id='demo_bash_and_python_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    tags=['bash', 'python', 'lab8', 'demo'],
    max_active_runs=1
)

task1 = BashOperator(
    dag=dag,
    task_id='task1',
    bash_command='echo "This is a BashOperator"'
)

def task2_callable():
    print("This is a PythonOperator")

task2 = PythonOperator(
    dag=dag,
    task_id='task2',
    python_callable=task2_callable
)

task3 = BashOperator(
    dag=dag,
    task_id='task3',
    bash_command='echo "The execution date is: {{ ds }}"'
)

def task4_callable(ts):
    print(f'The execution timestamp is: {ts}')

task4 = PythonOperator(
    dag=dag,
    task_id='task4',
    provide_context=True,
    python_callable=task4_callable
)

def print_lyrics(singer):
    singers = ['meatloaf', 'hall & oates']
    if singer.lower() not in singers:
        raise ValueError(f'Expecting value in {singers} but received {singer}')
    elif singer.lower() == 'meatloaf':
        str = """
            I would do anything for love.
            But I won't do that.
            No I won't do that.
        """
    else:
        str = """
            I'll do almost anything.
            But I can't go for that.
            No can do.
        """
    print(str)

task5 = PythonOperator(
    dag=dag,
    task_id='task5',
    python_callable=print_lyrics,
    op_kwargs={'singer': 'Meatloaf'}
)

task6 = PythonOperator(
    dag=dag,
    task_id='task6',
    python_callable=print_lyrics,
    op_kwargs={'singer': 'Hall & Oates'}
)

task7 = PythonOperator(
    dag=dag,
    task_id='task7',
    python_callable=print_lyrics,
    op_kwargs={'singer': 'Simon & Garfunkel'}
)

task8 = BashOperator(
    dag=dag,
    task_id='task8',
    bash_command='echo "Our GCS Bucket is: $BUCKET"',
    env={'BUCKET': Variable.get('bucket')}
)

task1 >> task2 >> [task3, task4]
task3 >> [task5, task6, task7]
task4 >> [task5, task6, task7]
