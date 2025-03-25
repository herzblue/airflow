import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwrags",
    schedule="30 6 * * *",  # 각 자리 = 분, 시, 일, 월, 요일
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist_t2 = PythonOperator(
        task_id="regist2_t1",
        python_callable=regist2,
        op_args=["herzblue", "man", "kr", "seoul"],
        op_kwargs={"email": "herzblue@gmail.com", "phone": "010"},
    )

    regist_t2
