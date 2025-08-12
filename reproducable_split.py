import uuid
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def add_identifiers(df, create_new = True, new_name = "dataframe"):

    df["unique_id"] = [uuid.uuid4().hex for x in range(len(df))]

    if create_new == True:
        df.to_csv(f"{new_name}.csv")
    if create_new == False:
        return df

def create_splitmap(df: pd.DataFrame):
    #create a unique identifier:
    if "unique_id" not in df.columns:
        df = add_identifiers(df, create_new = False)
        
    #split into train and test
    train_ids, test_ids = train_test_split(df["unique_id"], test_size = 0.1, random_state = 10)

    #create the split map to be used later
    train_set = set(train_ids)

    split_map = pd.DataFrame({
        "unique_id": df["unique_id"],
        "which_set": np.where(df["unique_id"].isin(train_set), "train", "test")
    })

    split_map.to_csv("split_mapping.csv", index = False)