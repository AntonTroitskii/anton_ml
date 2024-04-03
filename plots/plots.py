import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_rf_features_stat(model):
    featrues = [(i, j) for i, j in zip(
        model.feature_names_in_, model.feature_importances_)]
    featrues.sort(key=lambda x: x[1], reverse=True)
    df_featrures = pd.DataFrame(featrues, columns=['fname', 'importance'])
    return df_featrures

def save_importance(importance_path, model):
    df_featrures = get_rf_features_stat(model)
    sns.barplot(data=df_featrures, y='fname', x='importance')
    plt.savefig(importance_path, bbox_inches='tight')