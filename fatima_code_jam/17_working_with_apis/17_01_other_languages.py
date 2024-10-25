import requests
import plotly.express as px
import pandas as pd

# Define the list of languages to search for.
languages = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]
data = []

# Loop through each language and make an API call.
for language in languages:
    url = f"https://api.github.com/search/repositories?q=language:{language}"
    "+sort:stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code for {language}: {r.status_code}")

    # Convert the response object to a dictionary.
    response_dict = r.json()
    if 'items' in response_dict:
        # Get only the top 3 repositories.
        top_repos = response_dict['items'][:3]
        for repo_dict in top_repos:
            data.append({
                'Repository': repo_dict['name'],
                'Stars': repo_dict['stargazers_count'],
                'Owner': repo_dict['owner']['login'],
                'Description': repo_dict['description'],
                'Language': language
            })

# Convert the list of dictionaries to a DataFrame.
df = pd.DataFrame(data)

# Make visualization.
title = "Top 3 Most Popular Repositories by Language"
fig = px.bar(df, x='Repository', y='Stars', color='Language',
             title=title, hover_name='Owner', hover_data=['Description'])
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)
fig.update_traces(marker_opacity=0.6)
fig.show()
