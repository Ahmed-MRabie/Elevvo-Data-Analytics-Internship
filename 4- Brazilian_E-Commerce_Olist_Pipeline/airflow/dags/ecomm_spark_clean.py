from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import papermill as pm
import psycopg2


# PostgreSQL Config
PG_HOST = "postgres"
PG_PORT = 5432
PG_USER = "admin"
PG_PASSWORD = "password"
PG_DATABASE = "admin"

# ---------------------------------------------------------
# TASK 1 - Create 'olist_dwh' databases in PostgreSQL

def create_postgres_database():
    print("🚀 Connecting to PostgreSQL...")
    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
        database=PG_DATABASE,
    )
    conn.autocommit = True
    cur = conn.cursor()

    # ------ Create olist_dwh database if not exists ------
    cur.execute("SELECT 1 FROM pg_database WHERE datname = 'olist_dwh';")
    exists = cur.fetchone()
    if not exists:
        print("📦 Creating database 'olist_dwh'...")
        cur.execute("CREATE DATABASE olist_dwh;")
        print("✅ Database 'olist_dwh' created.")
    else:
        print("ℹ️ Database 'olist_dwh' already exists.")

    conn.commit()
    cur.close()
    conn.close()

# ---------------------------------------------------------
# TASK 2 - Run Spark ETL Notebook

def run_notebook():
    pm.execute_notebook(
        '/opt/airflow/dags/notebooks/ecomm_etl_spark_job.ipynb',     # input
        '/opt/airflow/dags/notebooks/ecomm_etl_spark_job.ipynb'      # output
    )

#===========================================================

with DAG(
    dag_id='run_etl_job',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['etl', 'notebook']
) as dag:
    
    # ---------------------------------------------------------
    # Operators
    
    init_postgres_task = PythonOperator(
        task_id='create_postgres_dwh',
        python_callable=create_postgres_database,
    )

    run_etl = PythonOperator(
        task_id='run_spark_etl_job',
        python_callable=run_notebook
    )

    init_postgres_task >> run_etl  