from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import multiprocessing 

def scrape(link):
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(driver=browser, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1rynq56')))

    time.sleep(5)

    content = browser.page_source
    browser.close()

    soup = BeautifulSoup(content, "html.parser")

    tweets_data = []

    tweets = soup.find_all(attrs={"data-testid": "tweetText"})
    tweet_counts = soup.find_all(class_="css-175oi2r r-1kbdv8c r-18u37iz r-1wtj0ep r-1ye8kvj r-1s2bzr4")
    tweet_dates = soup.find_all("time")

    for tweet, tweet_c, tweet_d in zip(tweets, tweet_counts, tweet_dates):
        tweet_text = tweet.text.strip()
        tweet_c_value = tweet_c.get("aria-label")
        tweet_d_value = tweet_d.get("datetime")
        counts = re.findall(r'\d+', tweet_c_value)
        counts = [int(count) for count in counts]
        replies = counts[0] if len(counts) > 0 else None
        reposts = counts[1] if len(counts) > 1 else None
        likes = counts[2] if len(counts) > 2 else None
        bookmarks = counts[3] if len(counts) > 3 else None
        tweets_data.append([tweet_text, replies, reposts, likes, bookmarks, tweet_d_value])

    test_ids = {
        "UserName": "username",
        "UserDescription": "userdesc",
        "UserProfessionalCategory": "usercat",
        "UserUrl": "userurl",
        "UserJoinDate": "userdate",
    }

    user_data = {}
    for key, value in test_ids.items():
        try:
            user_data[value] = soup.find(attrs={"data-testid": key}).text.strip()
        except AttributeError:
            user_data[value] = None

    #indices_to_retrieve = [8, 9, 10, 11, 13, 14, 15, 17]
    #for idx in indices_to_retrieve:
    #    text = extract[idx].text.strip()
    #    if "Joined" in text:
    #        text = text.replace('Joined ', '')
    #    data.append(text)

    return tweets_data, user_data

genuine = 'genuine_accounts.csv/users.csv'
social1 = 'social_spambots_1.csv/users.csv'
social2 = 'social_spambots_2.csv/users.csv'
social3 = 'social_spambots_3.csv/users.csv'
traditional1 = 'traditional_spambots_1.csv/users.csv'
traditional2 = 'traditional_spambots_2.csv/users.csv'
traditional3 = 'traditional_spambots_3.csv/users.csv'
traditional4 = 'traditional_spambots_4.csv/users.csv'

def read(csv_file):
    df = pd.read_csv('datasets_full.csv/'+csv_file)
    num_rows, num_columns = df.shape
    sample_df = df.sample(n=1500)
    name_column = sample_df['screen_name'].tolist()
    return name_column

def read2(*csv_files):
    combined_df = pd.DataFrame() 
    for csv_file in csv_files:
        df = pd.read_csv('datasets_full.csv/'+csv_file)
        combined_df = pd.concat([combined_df, df]) 

    num_rows, num_columns = combined_df.shape
    sample_df = combined_df.sample(n=1500)
    name_column = sample_df['screen_name'].tolist()
    return name_column

gen = read(genuine)
soc = read2(social1, social2, social3)
tra = read2(traditional1, traditional2, traditional3, traditional4)

if __name__ == "__main__":
    conso_data = []
    usernames = gen
    count = 0
    for username in usernames:
        count += 1
        print(f'{count} of 1500')
        data_link = f"https://twitter.com/{username}/"
        tweets_data, user_data = scrape(data_link)
        for tweet in tweets_data:
            tweet.extend(list(user_data.values()))
            conso_data.append(tweet)

    columns = ['Tweet', 'Replies', 'Reposts', 'Likes', 'Bookmarks', 'Posted', 'Username', 'UserDescription', 'UserProfessionalCategory', 'UserUrl', 'UserJoinDate']

    df1 = pd.DataFrame(conso_data, columns=columns)

    print(df1)

    df1.to_csv("gen_data.csv", index=False)
