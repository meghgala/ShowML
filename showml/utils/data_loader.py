from typing import Tuple
import numpy as np
import pandas as pd
from typing import Tuple


def load_wine() -> Tuple[np.ndarray, np.ndarray]:
    """
    A method to load the Auto.csv file, include the necessary columns and return X_train and y_train
    return X_train: The input training data
    return y_train: The input training labels
    """
    wine = (
        pd.read_csv(
            "./data/Wine_Quality.csv", sep=";", na_values="?", dtype={"ID": str}
        )
        .dropna()
        .reset_index()
    )
    X_train = wine[
        [
            # "fixed acidity",
            # "volatile acidity",
            # "citric acid",
            # "residual sugar",
            # "chlorides",
            # "free sulfur dioxide",
            # "total sulfur dioxide",
            # "density",
            # "pH",
            "sulphates",
            "alcohol",
        ]
    ].values

    # Remap wine quality to only 2 groups
    wine["quality"] = wine["quality"].map({3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1})
    y_train = wine[["quality"]].values

    # Make y_train 1D if its not
    if y_train.ndim > 1:
        y_train = y_train[:, 0]
    return X_train, y_train


def load_auto() -> Tuple[np.ndarray, np.ndarray]:
    """
    A method to load the Auto.csv file, include the necessary columns and return X_train and y_train
    return X_train: The input training data
    return y_train: The input training labels
    """
    auto = (
        pd.read_csv("./data/Auto.csv", na_values="?", dtype={"ID": str})
        .dropna()
        .reset_index()
    )
    X_train = auto[
        [
            "cylinders",
            "displacement",
            "horsepower",
            "weight",
            "acceleration",
            "year",
            "origin",
        ]
    ].values
    y_train = auto[["mpg"]].values

    # Make y_train 1D if its not
    if y_train.ndim > 1:
        y_train = y_train[:, 0]

    return X_train, y_train


def load_salary() -> Tuple[np.ndarray, np.ndarray]:
    """
    A method to load the Salary.csv file, include the necessary columns and return X_train and y_train
    return X_train: The input training data
    return y_train: The input training labels
    """
    salary_data = (
        pd.read_csv("./data/Salary.csv", na_values="?", dtype={"ID": str})
        .dropna()
        .reset_index()
    )
    X_train = salary_data[["YearsExperience"]].values
    y_train = salary_data[["Salary"]].values

    # Make y_train 1D if its not
    if y_train.ndim > 1:
        y_train = y_train[:, 0]

    return X_train, y_train
