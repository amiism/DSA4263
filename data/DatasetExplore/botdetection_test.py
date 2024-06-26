# -*- coding: utf-8 -*-
"""BotDetection_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RSWchwgOljlfP_sl514zGMvkrBXA9VUH
"""

import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

## allow colab to read from google drive
from google.colab import drive
drive.mount('/content/drive')

##working directory containing the dataset to interact with
data_path = '/content/drive/MyDrive/DSA4263-FinalProject/BotDetection/bot_detection_data.csv'    #please change to your local filepath directory when running

#import data
data_df = pd.read_csv(data_path)

data_df.head()

data_df.info()

# Get the column headers of data_df
column_headers = data_df.columns

# Print the column headers
print(column_headers)

# Calculate the count of each bot label
bot_label_counts = data_df['Bot Label'].value_counts()

# Plot the pie chart
plt.pie(bot_label_counts, labels=['Genuine (Bot Label = 0)', 'Bot (Bot Label = 1)'], autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])

# Add title
plt.title('Distribution of Bot Label')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the plot
plt.show()

# Print comments on the number of data for each label
print("Number of genuine users (Bot Label = 0):", bot_label_counts[0])
print("Number of bots (Bot Label = 1):", bot_label_counts[1])

"""there is a pretty even distribution which is good"""

# Display column headers and types
print(data_df.info())

# Numerical variables vs. Bot Label
numerical_variables = ['Retweet Count', 'Mention Count', 'Follower Count']

for variable in numerical_variables:
    sns.boxplot(x='Bot Label', y=variable, data=data_df)
    plt.title(f'{variable} vs. Bot Label')
    plt.show()

# Categorical variables vs. Bot Label
categorical_variables = ['Verified', 'Location']

for variable in categorical_variables:
    sns.countplot(x=variable, hue='Bot Label', data=data_df)
    plt.title(f'{variable} vs. Bot Label')
    plt.show()

