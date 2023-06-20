import logging
import mlflow

try:
    mlflow.create_experiment(name="mandingo")
except mlflow.exceptions.MlflowException:
    logging.warning("Using previous experiment ...")

with mlflow.start_run(experiment_id=mlflow.get_experiment_by_name("mandingo").experiment_id):
    print("Hello from nowhere")
