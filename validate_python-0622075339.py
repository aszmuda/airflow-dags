from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "validate_python-0622075339",
}

dag = DAG(
    "validate_python-0622075339",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Use this pipeline to test your JupyterLab, Kubeflow Pipelines, or Apache Airflow environment setup.

If your setup is correct, this pipeline should run as is:
 - To test JupyterLab, click the "run" button and choose "Local Runtime" as Runtime Platform.
 - To test Kubeflow Pipelines, create a Kubeflow Pipelines runtime configuration, then click the "run" button and select "Kubeflow Pipelines" as Runtime Platform.
 - To test Apache Airflow, create an Apache Airflow runtime configuration, then click the "run" button and select "Apache Airflow" as Runtime Platform.
    """,
    is_paused_upon_creation=False,
)


# Operator source: examples/pipelines/setup_validation/python_notebook.ipynb
op_8a43f7ec_e001_4f39_964d_a3437cb3b797 = KubernetesPodOperator(
    name="python_notebook",
    namespace="ml",
    image="amancevice/pandas:1.4.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L file:///elyra-deps/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio.ml.svc.cluster.local:9000 --cos-bucket airflow --cos-directory 'validate_python-0622075339' --cos-dependencies-archive 'python_notebook-8a43f7ec-e001-4f39-964d-a3437cb3b797.tar.gz' --file 'examples/pipelines/setup_validation/python_notebook.ipynb' "
    ],
    task_id="python_notebook",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "validate_python-0622075339-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: examples/pipelines/setup_validation/python_script.py
op_105b829d_832f_4f54_ab5d_ba464ce15abe = KubernetesPodOperator(
    name="python_script",
    namespace="ml",
    image="tensorflow/tensorflow:2.8.0",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L file:///elyra-deps/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio.ml.svc.cluster.local:9000 --cos-bucket airflow --cos-directory 'validate_python-0622075339' --cos-dependencies-archive 'python_script-105b829d-832f-4f54-ab5d-ba464ce15abe.tar.gz' --file 'examples/pipelines/setup_validation/python_script.py' "
    ],
    task_id="python_script",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "validate_python-0622075339-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_105b829d_832f_4f54_ab5d_ba464ce15abe << op_8a43f7ec_e001_4f39_964d_a3437cb3b797
