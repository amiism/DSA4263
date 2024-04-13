DSA4263
==============================
Sense-making Case Analysis: Business and Commerce
Final Project: Twitter Bot Detection
by Binali Manilka Pilapitiya De Alwis, Amirtha D/O Anbalagan, Chang An Le Harry Jr, Eldora Boo Puay Eng, Bryan Yeo, Dongmen Runze
 
Summary
------------
Using 2 different datasets from Bot Repository, our project aims to use various machine learning models to detect bots from genuine accounts (using a 'Users dataset'), as well as from their respective tweets ('Tweets dataset'). Our project will also explore and test up to 6 different hypotheses we have defined, namely:

1. Bots have a disproportionate ratio of followers to friends, indicating non-reciprocal relationships.
2. Bots are more likely to have a default or generic profile setup.
3. Bots engage less with content in terms of likes and retweets but may post content that is heavily retweeted within bot networks.
4. Bots are less likely to be geographically consistent or provide accurate location data.
5. Bots generate tweets with more hashtags and links compared to genuine accounts. 
6. Bots may exhibit different temporal dynamics in terms of when they are active compared to genuine users. They may also post at certain times or post a lot of tweets at a stretch. 

Based on the data pipeline we have defined for our respective models, we will then recommend our solution to ensure that this can be reproducible at the industry level.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
