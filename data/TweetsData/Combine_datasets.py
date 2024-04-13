import pandas as pd

# Paths to your datasets
bots_data_path = '/Users/bryanyeo/final_dataset_ss.csv'
real_accounts_data_path = '/Users/bryanyeo/final_dataset_ga.csv'

# Load the datasets
bots_df = pd.read_csv(bots_data_path)
real_accounts_df = pd.read_csv(real_accounts_data_path)

# Add the 'IsBot' column to each DataFrame
# We're setting it to 1 for bots and 0 for real accounts
bots_df['IsBot'] = 1
real_accounts_df['IsBot'] = 0

# Concatenate the two DataFrames
# This will automatically handle the headers, including the new 'IsBot' column
combined_df = pd.concat([bots_df, real_accounts_df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('final_dataset_combined.csv', index=False)
