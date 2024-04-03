from pathlib import Path
import pickle
import pandas as pd


def load_data_from_pkl(path: Path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def save_data_as_pkl(data, path: Path):
    with open(path, 'wb') as file:
        pickle.dump(data, file)


def load_data_from_pkl(path: Path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def load_X_y_from_pkl(path: Path):
    with open(path, 'rb') as f:
        data = pickle.load(f)

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    return X, y


def append_label_save_pkl(X, y, fpath):
    if y is not None:
        output = pd.concat([X, y], axis=1)
    else:
        output = X

    with open(fpath, 'wb') as f:
        pickle.dump(output, f)
