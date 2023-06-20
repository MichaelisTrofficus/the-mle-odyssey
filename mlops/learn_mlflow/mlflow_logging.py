import matplotlib.pyplot as plt
import mlflow
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch

try:
    mlflow.create_experiment(name="logging_experiment")
except mlflow.exceptions.MlflowException:
    print("The experiment already exists")

with mlflow.start_run(experiment_id=mlflow.get_experiment_by_name("logging_experiment").experiment_id):
    # Params: It doesnt change the value
    mlflow.log_param(key="optimal_tree_depth", value=5)

    # Metrics (Changes its value over the course of the execution)
    # For example, the score of a neural network
    my_list = range(10)
    for item in my_list:
        mlflow.log_metric(key="neural_network_score", value=item)

    # Figures (Matplotlib / Plotly)
    N = 400
    t = np.linspace(0, 2*np.pi, N)
    r = 0.5 + np.cos(t)
    x, y = r * np.cos(t), r * np.sin(t)

    fig, ax = plt.subplots()
    ax.plot(x, y, "k")
    ax.set(aspect=1)

    mlflow.log_figure(fig, artifact_file="Logged figure from mlflow.png")



