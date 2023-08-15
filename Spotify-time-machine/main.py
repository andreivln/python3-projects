import json
import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


year_asking = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
url = requests.get("https://www.billboard.com/charts/hot-100/" + year_asking)
response = url.text

soup = BeautifulSoup(response, "html.parser")

song_name_spans = soup.select(selector="li ul li h3")
# artists_name_spans = soup.select(selector="li ul li span")
song_names = [song.getText().strip() for song in song_name_spans]
# artists_names = [name.getText().strip() for name in artists_name_spans]
print(song_names)
# print(artists_names)



CLIENT_ID = os.environ['spotify_client_id']
CLIENT_SECRET = os.environ['spotify_client_secret']
SCOPE = "playlist-modify-private"
REDIRECT_URI = "http://example.com"
CACHE_PATH = os.environ['token']
USERNAME = os.environ['username']

SP = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE,
                                               cache_path=CACHE_PATH,
                                               username=USERNAME,
                                               show_dialog=True
                                               ))

user_id = SP.current_user()["id"]

year = year_asking.split("-")[0]
song_uri = []


for song in song_names:
    result = SP.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    # print(json.dumps(result)) 
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")


playlist = SP.user_playlist_create(user=user_id,
                        name=f"{year_asking} Billboard 100",
                        public=False,
                        description="Top 100 tracks")

SP.playlist_add_items(playlist_id=playlist["id"],
                      items=song_uri)
