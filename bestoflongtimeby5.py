# -*- coding: utf-8 -*-


import spotipy
from spotipy import util
import tkinter
from tkinter import messagebox
# from sys import exit

scope = "user-top-read playlist-read-private playlist-modify-private"
username = "Maxime Diet"
client_id = "52a838937f0c4b36a0660567f4d2b2ec"
client_secret = "f52a63baf5c7487b99fa0ae406f6772d"
playlist_id_short = "1phno7FvaFAJ5sxNoPlL17"
playlist_id_medium = "5cqFT8oPyuewlfApBXVtmK"
playlist_id_long = "1Ga0geeZu10isWoUXJMint"
playlist_id_long_moment = "5MQECwbZbQwuO0e4Tiu6OI"
redirect_uri = "http://localhost:8080"
token = util.prompt_for_user_token(
    username,
    scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
)

spotify = spotipy.Spotify(auth=token)

top_track_long_moment = spotify.current_user_top_tracks(limit=50, time_range="short_term")
playlist_top_long_moment= spotify.playlist(playlist_id_long_moment, fields=None, market=None, )
y=0
save = open("id_long.txt","r")
saves_id = save.readlines()
save_id=list()
for saved_ids in saves_id:
    
    saved_ids=saved_ids.rstrip("\n")
    save_id.append(saved_ids)
    print(saved_ids)
save.close()
id_deja_present=list()
playlist_top_long_moment= spotify.playlist(playlist_id_long_moment, fields=None, market=None, )
idd = 0
p=0
id_list=list()
fichier= open("id_long.txt","a")
s = playlist_top_long_moment['tracks']['total'] 

for k in range(0,50,1):
    id_long = top_track_long_moment['items'][k]['id']
    if id_long not in save_id:
            id_list.append(id_long)
spotify.user_playlist_add_tracks(user=username, playlist_id=playlist_id_long_moment, tracks=id_list)

for element in id_list:

    fichier.write(element)
    fichier.write("\n")
fichier.close()
# print(id_list)