# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:25:18 2020

@author: ZiRa_Omega
"""

import spotipy
from spotipy import util

scope = "user-top-read playlist-read-private playlist-modify-private"
while 1==1:
    web = input("Go to URL : https://developer.spotify.com , register and get client_id and client_secret then type YES ")
    if web == "YES":
        break
username = input("Username :  ")
client_id = input("Client id = ")
client_secret = input("Client secret = ")
redirect_uri = "http://localhost/"
playlist_id_id = input("Playlist id = ")
token = util.prompt_for_user_token(
    username,
    scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
)

spotify = spotipy.Spotify(auth=token)
top_track = spotify.current_user_top_tracks(limit=50, time_range='medium_term')
def create_playlist_best_of(nbr_tracks):
    titre_top_tracks = []
    for i in range(0,nbr_tracks,1):
        titre_top_track = top_track['items'][i]['id']
        titre_top_tracks.append(titre_top_track)
    spotify.user_playlist_add_tracks(user=username, playlist_id=playlist_id_id, tracks=titre_top_tracks)
    choice()
def replace_playlist_tracks_best_of(nbr_tracks):
    titre_top_tracks = []
    for i in range(0,nbr_tracks,1):
        titre_top_track = top_track['items'][i]['id']
        titre_top_tracks.append(titre_top_track)
    spotify.user_playlist_replace_tracks(user=username, playlist_id=playlist_id_id, tracks=titre_top_tracks)
    choice()
def choice():
    end = 0
    end = input("1 : Créer ou ajouter le best of des titres\n2 : Remplacer les titres présent par votre nouveau best of\n3 : STOP\n")
    if end == "1" :
        nbr_tracks = int(input("Combien de titres : (limite = 50) "))
        create_playlist_best_of(nbr_tracks)
    elif end=="2":
        nbr_tracks = int(input("Combien de titres : (limite = 50) "))
        replace_playlist_tracks_best_of(nbr_tracks)        
    elif end =="3":
        exit
    else:
        print("Une erreur est survenue")
        choice()
choice()
