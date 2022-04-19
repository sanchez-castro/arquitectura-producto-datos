"""Demo DAG for Using BigQueryOperator"""

from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
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
    dag_id='demo_bigquery_operator',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    tags=['bigquery', 'lab8', 'demo'],
    max_active_runs=1
)

ddl = """
CREATE TABLE IF NOT EXISTS demos.crypto_ethereum_transactions (
    ds DATE,
    transactions INT64,
    total_value FLOAT64
)
PARTITION BY
  ds
"""

dml = """
INSERT INTO demos.crypto_ethereum_transactions
SELECT
  CAST('{{ ds }}' as DATE) as ds,
  COUNT(transaction_hash) as transactions,
  SUM(SAFE_CAST(value as FLOAT64)) as total_value
FROM
  `bigquery-public-data.crypto_ethereum.token_transfers`
WHERE
  DATE(block_timestamp) = '{{ ds }}'
"""

ddl_task = BigQueryOperator(
    task_id='ddl_task',
    dag=dag,
    sql=ddl,
    use_legacy_sql=False
)

dml_task = BigQueryOperator(
    task_id='dml_task',
    dag=dag,
    sql=dml,
    use_legacy_sql=False
)

ddl_task >> dml_task
