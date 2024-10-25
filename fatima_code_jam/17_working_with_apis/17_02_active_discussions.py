# Loading the data from hn_submissions.py
from operator import itemgetter
import requests

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                          reverse=True)

for submission_dict in submission_dicts:
   print(f"\nTitle: {submission_dict['title']}")
   print(f"Discussion link: {submission_dict['hn_link']}")
   print(f"Comments: {submission_dict['comments']}")

# 17_02_active_discussions.py

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Assuming hn_submissions.py data is imported or available in a DataFrame
# For example, data could look like this:
# data = pd.read_json('hn_submissions.json')

# Sample structure of the DataFrame
data = pd.DataFrame({
    'title': ['Quantized Llama models with increased speed and a reduced '
              'memory footprint', 
              'Launch HN: Skyvern (YC S23) – open-source AI agent for browser '
              'automations', 
              'Security research on Private Cloud Compute', 
              'Bitwarden SDK relicensed from proprietary to GPLv3', 
              'OpenFeature – a vendor-agnostic, community-driven API for '
              'feature flagging'],
    'num_comments': [63, 53, 49, 28, 0],
    'url': ['https://news.ycombinator.com/item?id=41938473', 
            'https://news.ycombinator.com/item?id=41936745', 
            'https://news.ycombinator.com/item?id=41937664', 
            'https://news.ycombinator.com/item?id=41940580', 
            'https://news.ycombinator.com/item?id=41941493']
    })

# Sort the data by number of comments
data = data.sort_values(by='num_comments', ascending=False)

# Prepare the links, comments, and hover texts
titles, comments, urls = [], [], []
for index, row in data.iterrows():
    try:
        title = row['title']
        url = row['url']
        # Create HTML link for the title
        repo_link = f"<a href='{url}' target='_blank'>{title}</a>"
        titles.append(repo_link)
        comments.append(row['num_comments'])
        urls.append(f"{title}: {row['num_comments']} comments")
    except KeyError:
        continue  

# Create the bar chart using Plotly
title = "Most Active Discussions on Hacker News"
labels = {'x': 'Discussion Title', 'y': 'Number of Comments'}
fig = px.bar(x=titles, y=comments, title=title, labels=labels,
             hover_name=urls)

# Update layout for better readability
fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

# Show the figure
fig.show()