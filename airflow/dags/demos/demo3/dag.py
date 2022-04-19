"""Demo DAG for using Bash and Python Operators"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago
import os

path = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(path, 'twelve_days_of_christmas.py')
params = {
    'script': script_path,
    'verses': 5
}

dag = DAG(
    dag_id='demo_scripting_dag',
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    tags=['bash', 'python', 'lab8', 'demo'],
    max_active_runs=1
)

bash_task = BashOperator(
    dag=dag,
    params=params,
    task_id='bash_task',
    bash_command='python3 {{ params.script}} --verses {{ params.verses }}'
)

def singing_function(num_verses):
    lyrics = [
        'A partridge in a pear tree',
        'Two turtledoves',
        'Three French hens',
        'Four calling birds',
        'Five golden rings',
        'Six geese a-laying',
        'Seven swans a-swimming',
        'Eight maids a-milking',
        'Nine ladies dancing',
        'Ten lords a-leaping',
        'Eleven pipers piping',
        'Twelve drummers drumming',
    ]

    verse_num = 1
    while verse_num <= num_verses:
        verses = lyrics[0:verse_num]
        verses.reverse()
        print(f"On the {verse_num} day of Christmas, my true love gave to me:")
        for verse in verses:
            print(verse)
        print("")
        verse_num +=1

python_task = PythonOperator(
    dag=dag,
    task_id='python_task',
    python_callable=singing_function,
    op_kwargs={'num_verses': 10}
)
