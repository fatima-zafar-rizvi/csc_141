# make_album.py

def make_album(artist, title, number_of_songs=None):
    """Build a dictionary describing a music album."""
    album_info = {
        'artist': artist,
        'title': title,
    }
    
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs
    
    return album_info

if __name__ == "__main__":
    album = make_album("Taylor Swift", "Folklore", number_of_songs=16)
    print(album)

# show_messages.py

def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

if __name__ == "__main__":
    messages = ["Hello", "How are you?", "Goodbye"]
    show_messages(messages)

# make_sandwich.py

def make_sandwich(*items):
    """Summarize the sandwich order."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

if __name__ == "__main__":
    make_sandwich("lettuce", "tomato", "turkey")
