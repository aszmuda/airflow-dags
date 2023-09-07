from pendulum import datetime
from airflow.configuration import conf
from airflow.decorators import dag, task
import random

with DAG(
    dag_id="kubernetes_operator_example",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=["example"],
) as dag:
    task = KubernetesPodOperator(
        namespace="mds",
        image="registry.access.redhat.com/ubi9/ubi-minimal:9.2-717",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        name="airflow-test-pod",
        task_id="task",
        on_finish_action="delete_pod",
        in_cluster=True,
        get_logs=True,
    )

    task
