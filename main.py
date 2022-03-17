import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

##-----Generate the play list
# date = input("what year you would like to travel to in YYY-MM-DD format: ")
#
# URL = f"https://www.billboard.com/charts/hot-100/{date}"
#
# response = requests.get(url=URL)
# # print(response.text)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# music_all = soup.select(selector="li h3")
# # print(music_all)
# song_list = [song_name.getText().strip('\n') for song_name in music_all[:100]]
#  # print(song_list)
#----------------------------------


client_ID = "25cad40ab73c48fcac2b6f76f7813607"
client_secret = "83759a3032bf4f5ca98f382f7de8d7ec"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_ID,
        client_secret=client_secret,
        scope="playlist-modify-private",
        redirect_uri= "http://example.com",
        show_dialog="true",
        cache_path="token.txt"
    )
)
result = sp.current_user()["id"]


# web_data = response.text
#
# soup = BeautifulSoup(web_data, "html.parser")
#
# songs = soup.select(selector="li h3")
#
# song_titles = [song.getText().strip("\n") for song in songs[:100]]
# print(song_titles)