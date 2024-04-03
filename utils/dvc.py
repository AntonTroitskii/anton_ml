from pathlib import Path
import pandas as pd
import yaml
import argparse


def parse_config():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    return args.config


def load_params(path='params.yaml'):
    with open(Path(path)) as config_file:
        return yaml.safe_load(config_file)


def load_X_y_from_csv(path: Path, params):
    df = pd.read_csv(path)
    if params['base']['target'] in df.columns:
        X = df.drop(columns=params['base']['target'], axis=1)
        y = df[params['base']['target']]
    else:
        X = df
        y = None

    return X, y
