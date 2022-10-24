from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "validate_python-1024190526",
}

dag = DAG(
    "validate_python-1024190526",
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


# Operator source: /home/aszmuda/Downloads/examples/pipelines/setup_validation/python_notebook.ipynb

op_8a43f7ec_e001_4f39_964d_a3437cb3b797 = KubernetesPodOperator(
    name="python_notebook",
    namespace="default",
    image="tensorflow/tensorflow:2.8.0",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'validate_python' --cos-endpoint http://localhost:9000 --cos-bucket test --cos-directory 'validate_python-1024190526' --cos-dependencies-archive 'python_notebook-8a43f7ec-e001-4f39-964d-a3437cb3b797.tar.gz' --file '/home/aszmuda/Downloads/examples/pipelines/setup_validation/python_notebook.ipynb' "
    ],
    task_id="python_notebook",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "validate_python-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: /home/aszmuda/Downloads/examples/pipelines/setup_validation/python_script.py

op_105b829d_832f_4f54_ab5d_ba464ce15abe = KubernetesPodOperator(
    name="python_script",
    namespace="default",
    image="tensorflow/tensorflow:2.8.0",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'validate_python' --cos-endpoint http://localhost:9000 --cos-bucket test --cos-directory 'validate_python-1024190526' --cos-dependencies-archive 'python_script-105b829d-832f-4f54-ab5d-ba464ce15abe.tar.gz' --file '/home/aszmuda/Downloads/examples/pipelines/setup_validation/python_script.py' "
    ],
    task_id="python_script",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "validate_python-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_105b829d_832f_4f54_ab5d_ba464ce15abe << op_8a43f7ec_e001_4f39_964d_a3437cb3b797
