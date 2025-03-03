from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruits",
    schedule='10 0 * * 6#1',
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    t1_orange = BashOperator(
        task_id="select_fruits",
        bash_command="/opt/airflow/plugins/select_fruit.sh ORANGE",
    )