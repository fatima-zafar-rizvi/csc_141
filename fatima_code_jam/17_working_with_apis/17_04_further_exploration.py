import requests
import plotly.graph_objects as go

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
top_stories_response = requests.get(url)
top_story_ids = top_stories_response.json()[:10]  

# Fetch details for each story
stories = []
for story_id in top_story_ids:
    story_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    story_response = requests.get(story_url)
    stories.append(story_response.json())

titles = [story['title'] for story in stories]
scores = [story.get('score', 0) for story in stories]  

fig = go.Figure(data=[
    go.Pie(labels=titles, values=scores, hole=.3)  
])

fig.update_layout(
    title='Top Hacker News Stories by Score',
    template='plotly_dark'  
)

fig.show()