import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def model_report(y_test, predictor):
    conf_matrix = confusion_matrix(y_test, predictor)

    class_names = ['Edible', 'Poisonous']
    # Define the labels for the matrix
    labels = [["True Negative", "False Positive"], ["False Negative", "True Positive"]]

    # Plotting the confusion matrix using matplotlib
    fig, ax = plt.subplots(figsize=(10, 7))
    cax = ax.matshow(conf_matrix, cmap='BuPu')
    plt.colorbar(cax)

    # Set ticks and labels
    ax.set_xticks(np.arange(len(class_names)))
    ax.set_yticks(np.arange(len(class_names)))
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(j, i, f"{labels[i][j]}\n{conf_matrix[i, j]}", ha="center", va="center", color="black", fontsize=12)

    ax.set_title('Edible vs Not-Edible Mushrooms Confusion Matrix')
    plt.show()
