
import pandas as pd


def save_dict_as_cvs(data, file_path):
    data_df = pd.DataFrame(data)
    data_df.to_csv(file_path, index=True, index_label='epoch')
