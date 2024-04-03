
import pandas as pd


def save_results_as_csv(results, file_path):
    data_df = pd.DataFrame(results)
    data_df.to_csv(file_path, index=True, index_label='epoch')
