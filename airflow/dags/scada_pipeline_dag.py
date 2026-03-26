from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_DIR = "/opt/project"
DBT_DIR = f"{PROJECT_DIR}/dbt/wind_farm_project"

with DAG(
    dag_id="scada_pipeline",
    start_date=datetime(2026, 3, 24),
    schedule=None,
    catchup=False,
    tags=["zoomcamp", "scada", "wind-farm"],
) as dag:

    extract_scada_data = BashOperator(
        task_id="extract_scada_data",
        bash_command=f"""
        cd {PROJECT_DIR} &&
        python ingestion/ingest_scada.py
        """,
    )

    upload_to_gcs = BashOperator(
        task_id="upload_to_gcs",
        bash_command=(
            "mkdir -p /tmp/gcloud && "
            "cp -r /home/airflow/.config/gcloud/* /tmp/gcloud/ 2>/dev/null || true && "
            "export CLOUDSDK_CONFIG=/tmp/gcloud && "
            f"cd {PROJECT_DIR} && "
            "gcloud storage cp data/scada_data.csv "
            "gs://wind-farm-analytics-janio-scada-data/raw/scada_data.csv"
        ),
    )

    load_to_bigquery = BashOperator(
        task_id="load_to_bigquery",
        bash_command=(
            "mkdir -p /tmp/gcloud && "
            "cp -r /home/airflow/.config/gcloud/* /tmp/gcloud/ 2>/dev/null || true && "
            "export CLOUDSDK_CONFIG=/tmp/gcloud && "
            "bq load --replace "
            "--autodetect "
            "--source_format=CSV "
            "--skip_leading_rows=1 "
            "wind-farm-analytics-janio:wind_farm.scada_raw "
            "gs://wind-farm-analytics-janio-scada-data/raw/scada_data.csv"
        ),
    )

    run_dbt_models = BashOperator(
        task_id="run_dbt_models",
        bash_command=(
            f"cd {DBT_DIR} && "
            "mkdir -p /tmp/dbt-logs /tmp/dbt-target && "
            "dbt run "
            "--project-dir . "
            "--profiles-dir /home/airflow/.dbt "
            "--log-path /tmp/dbt-logs "
            "--target-path /tmp/dbt-target"
        ),
    )

    extract_scada_data >> upload_to_gcs >> load_to_bigquery >> run_dbt_models