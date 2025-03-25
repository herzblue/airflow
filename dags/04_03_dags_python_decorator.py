import pendulum
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",  # 매일 06시 30분
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="python_task_1")
    def print_context(some_input):
        print(f"some_input: {some_input}")

    python_task_1 = print_context(some_input="task decorator 실행")
