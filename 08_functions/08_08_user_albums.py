def make_album(artist, title, number_of_songs=None):
    """Build a dictionary describing a music album."""
    album_info = {
        'artist': artist,
        'title': title,
    }
    
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs
    
    return album_info

# Loop to get user input for album details
while True:
    print("\nEnter the album details:")
    artist = input("Artist (or 'quit' to exit): ")
    if artist.lower() == 'quit':
        break
    
    title = input("Album title (or 'quit' to exit): ")
    if title.lower() == 'quit':
        break
    
    # Optional: get the number of songs
    songs_input = input("Number of songs (press enter to skip): ")
    number_of_songs = int(songs_input) if songs_input.isdigit() else None
    
    # Create the album dictionary
    album = make_album(artist, title, number_of_songs)
    
    # Print the album information
    print("\nAlbum information:", album)
