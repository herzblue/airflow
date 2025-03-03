import datetime
import pendulum
from airflow import DAG
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = 'dags_email_operator',
    schedule = '0 8 1 * *',
    start_date=pendulum.datetime(2023, 3, 1, tz='Asia/Seoul'),
    catup = False
) as dag:
    
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'herzblue@gmail.com',
        # cc = '' # 참조 설정
        subject = 'Airflow 성공 메일', # 이메일 제목
        html_content = 'Airflow 작업이 완료되었습니다.' # 이메일 본문 내용
    )