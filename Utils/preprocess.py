import pandas as pd
import numpy as np


def light(df_name):
    df = pd.read_csv(df_name)
    df = df.drop("user_id", axis=1)
    df = np.array(df)
    return df
