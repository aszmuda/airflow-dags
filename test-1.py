from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "test-1",
}

dag = DAG(
    "test-1",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Test",
    is_paused_upon_creation=False,
)


# Operator source: convert-nb.py
op_264e5b20_a85d_4de2_bc21_39778d17e301 = KubernetesPodOperator(
    name="convert_nb",
    namespace="ml",
    image="quay.io/eformat/airflow-runner:2.3.2",
    cmds=["sh", "-c"],
    arguments=[
        "date"
    ],
    task_id="convert_nb",
    in_cluster=True,
    config_file="",
    dag=dag,
)

op_264e5b20_a85d_4de2_bc21_39778d17e301.image_pull_policy = "Always"




