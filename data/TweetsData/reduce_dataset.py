import pandas as pd

file_path = 'Downloads/cresci-2017.csv/datasets_full.csv/genuine_accounts.csv/tweets.csv'

new_file_path = "new_file.csv"

try:
    original_df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    try:
        original_df = pd.read_csv(file_path, encoding='latin1')
    except UnicodeDecodeError:
        try:
            original_df = pd.read_csv(file_path, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            original_df = pd.read_csv(file_path, encoding='Windows-1252')

new_df = original_df.head(30000)
new_df.to_csv("final_dataset_ga.csv", index=False)