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


def clear_all(dir_path: Path):
    for item in dir_path.iterdir():
        if item.is_dir():
            shutil.rmtree(item, ignore_errors=True)
        elif item.is_file():
            item.unlink()


def make_folder(fpath: Path):
    if fpath.exists() and fpath.is_dir():
        clear_all(fpath)
    else:
        fpath.mkdir(parents=True, exist_ok=True)
