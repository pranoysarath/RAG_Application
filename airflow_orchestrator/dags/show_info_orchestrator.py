from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime
import os
import sys

grandparent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, grandparent_dir)
# print(grandparent_dir)
from RAG.show_info_fetcher.show_cleanup.show_cleanup import ShowCleanup
from RAG.show_info_fetcher.show_processor.show_info_writer import ShowInfoWriter
from RAG.show_info_fetcher.show_processor.show_etl import ShowETL

def fetchShowInfoFromTvmaze():
    ShowInfoWriter().get_new_show_info()

def transformAndUpdateDB():
    ShowETL().process_data()


def cleanup_processed_show_info():
    ShowCleanup().cleanup()

with DAG(
    dag_id="show_information_dag_v5",
    description="A Dag for fetching tv show information, formatting it and updating the knowledge DB, and finally cleaning up",
    start_date=datetime(2024, 7, 4),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    fetch = PythonOperator(
        task_id="fetch_show",
        python_callable=fetchShowInfoFromTvmaze,
    )

    process = PythonOperator(
        task_id="format_and_send",
        python_callable=transformAndUpdateDB,
    )


    cleanup = PythonOperator(
        task_id="cleanup",
        python_callable=cleanup_processed_show_info,
    )

    fetch >> process >> cleanup
