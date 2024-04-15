import spacy
import classy_classification
import csv
import pandas as pd
import os

#define a function to process your input and output
def few_shot(doc, csv_file):
    df = pd.read_csv(csv_file)
    data = {}
    sample_size = 30

    candidate_labels = df['Fraud'].unique().tolist()

    for label in candidate_labels:
        candidate_values = df.query(f"`Fraud` == '{label}'").sample(
            n=sample_size)['text'].values.tolist()
        data[label] = candidate_values
   
    nlp = spacy.blank("en")
    nlp.add_pipe(
        "classy_classification",
        config={
            "data": data,
            "model": "sentence-transformers/all-mpnet-base-v2",
            "device": "gpu"
        }
    )

    dictionary = nlp(doc)._.cats
    print(dictionary)
    return dictionary

def classify(probabilities):
    return probabilities['Fraud']
    
genuine = 'genuine_accounts.csv/tweets.csv'
social = 'social_spambots_2.csv/tweets.csv'
traditional = 'traditional_spambots_1.csv/tweets.csv'

def read(csv_file):
    df = pd.read_csv('datasets_full.csv/'+csv_file, encoding='latin-1')
    sample_df = df.sample(n=100)
    return sample_df

gen = read(genuine)
soc = read(social)
tra = read(traditional)

# For genuine DataFrame (gen)
gen['Bot'] = 0

# For social spambots (soc) and traditional spambots (tra) DataFrames
soc['Bot'] = 1
tra['Bot'] = 1


# Classify and add a new column to each DataFrame
gen['Fraud'] = gen['text'].apply(lambda x: classify(few_shot(x, "all_classified.csv")))
soc['Fraud'] = soc['text'].apply(lambda x: classify(few_shot(x, "all_classified.csv")))
tra['Fraud'] = tra['text'].apply(lambda x: classify(few_shot(x, "all_classified.csv")))

all_class = pd.concat([gen, soc, tra], ignore_index=True)

# Save modified DataFrames as new datasets
gen.to_csv('genuine_accounts_classified_fewshot.csv', index=False)
soc.to_csv('social_spambots_classified_fewshot.csv', index=False)
tra.to_csv('traditional_spambots_classified_fewshot.csv', index=False)
all_class.to_csv('all_classified_fewshot.csv', index=False)