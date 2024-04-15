import csv
import pandas as pd

df = pd.read_csv("all_classified_fewshot.csv")

threshold = 0.5  # Adjust this threshold as needed

df['Fraud'] = df['Fraud'].apply(lambda x: 1 if x >= threshold else 0)
combination_counts = df.groupby(['Bot', 'Fraud']).size().reset_index(name='Count')
print(combination_counts)

bot_fraud_counts = combination_counts[combination_counts['Bot'] == 1]
human_fraud_counts = combination_counts[combination_counts['Bot'] == 0]
bot_fraud_rate = bot_fraud_counts[bot_fraud_counts['Fraud'] == 1]['Count'].sum() / bot_fraud_counts['Count'].sum()
human_fraud_rate = human_fraud_counts[human_fraud_counts['Fraud'] == 1]['Count'].sum() / human_fraud_counts['Count'].sum()
print("Bot Fraud Rate:", bot_fraud_rate)
print("Human Fraud Rate:", human_fraud_rate)