from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/" + date)
soup = BeautifulSoup(response.text,"html.parser")
webpage = soup.find_all("span", class_="c-label")
song_name = [song.getText() for song in webpage]


Scope_name = "playlist-modify-private"
CLIENT_ID ="2235d317d16940cbbf810014f82afcd0"
CLIENT_SECRET = "70db139e1355457f89709e45a878bc80"
URL="http://example.com, http://localhost"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=Scope_name,
client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=URL,
show_dialog=True,cache_path="token.txt"))
date = input("Which year do you want? Type the date in this format YYYY-MM-DD:")
user_id = sp.current_user()["id"]
print(user_id)
song_item =[]
year = date.split("-")[0]
for music in song_name:
    result = sp.search(q=f"track:{music} year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_item.append(uri)
    except IndexError:
        print(f"{music} doesn't exist in spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_item)