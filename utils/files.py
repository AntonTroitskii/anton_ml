from pathlib import Path
import shutil
import pickle
import yaml
import pandas as pd


def delete_folder(path: Path):
    if path.exists() and path.is_dir():
        try:
            shutil.rmtree(path)
        except Exception as ex:
            print(ex)


def delete_files_in_folder(path: Path):
    if path.exists() and path.is_dir():
        for item in path.iterdir():
            if item.is_file():
                item.unlink()


def clear_all(dir_path: Path, ex_path):
    for item in dir_path.iterdir():
        if item not in ex_path:
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            elif item.is_file():
                item.unlink()


def make_folder(fpath: Path):
    if fpath.exists() and fpath.is_dir():
        delete_files_in_folder(fpath)
    else:
        fpath.mkdir(parents=False, exist_ok=True)


def append_label_save_pkl(X, y, fpath):
    if y is not None:
        output = pd.concat([X, y], axis=1)
    else:
        output = X
        
    with open(fpath, 'wb') as f:
        pickle.dump(output, f)

def load_params(path='params.yaml'):
    with open(Path(path)) as config_file:
        return yaml.safe_load(config_file)


def load_data_from_pkl(path: Path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def load_X_y_from_pkl(path: Path):
    with open(path, 'rb') as f:
        data = pickle.load(f)

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    return X, y


def load_X_y(path: Path, params):
    df = pd.read_csv(path)
    if params['base']['target'] in df.columns:
        X = df.drop(columns=params['base']['target'], axis=1)
        y = df[params['base']['target']]
    else:
        X = df
        y = None

    return X, y


