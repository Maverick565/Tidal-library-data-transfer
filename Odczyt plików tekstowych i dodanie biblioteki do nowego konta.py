import tidalapi
from tqdm import tqdm
import requests
import os

# Zaloguj się na swoje drugie konto TIDAL
session2 = tidalapi.Session()
print('Skopiuj link i zaloguj się na nowe konto')
session2.login_oauth_simple()
uid2 = session2.user.id
TidalUser2 = tidalapi.Favorites(session2, uid2)

# Dodawanie ulubionych albumów do drugiego konta TIDAL
print('Adding albums ...')
with open('album_id_list.txt') as f:
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        album_id = lines[i].strip()  # Usuń zbędne białe znaki na początku i końcu
        try:
            TidalUser2.add_album(album_id)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Album {album_id} not found.")
            else:
                print(f"An error occurred while adding album {album_id}: {e}")
        except Exception as e:
            print(f"An error occurred while adding album {album_id}: {e}")

# Dodawanie ulubionych artystów do drugiego konta TIDAL
print('Adding artists ...')
with open('artist_id_list.txt') as f:
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        artist_id = lines[i].strip()  # Usuń zbędne białe znaki na początku i końcu
        try:
            TidalUser2.add_artist(artist_id)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Artist {artist_id} not found.")
            else:
                print(f"An error occurred while adding artist {artist_id}: {e}")
        except Exception as e:
            print(f"An error occurred while adding artist {artist_id}: {e}")

# Dodawanie ulubionych playlist do drugiego konta TIDAL
print('Adding playlists ...')
with open('playlist_id_list.txt') as f:
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        playlist_id = lines[i].strip()  # Usuń zbędne białe znaki na początku i końcu
        try:
            TidalUser2.add_playlist(playlist_id)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Playlist {playlist_id} not found.")
            else:
                print(f"An error occurred while adding playlist {playlist_id}: {e}")
        except Exception as e:
            print(f"An error occurred while adding playlist {playlist_id}: {e}")

# Dodawanie ulubionych utworów do drugiego konta TIDAL
print('Adding tracks ...')
with open('track_id_list.txt') as f:
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        track_id = lines[i].strip()  # Usuń zbędne białe znaki na początku i końcu
        try:
            TidalUser2.add_track(track_id)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Track {track_id} not found.")
            else:
                print(f"An error occurred while adding track {track_id}: {e}")
        except Exception as e:
            print(f"An error occurred while adding track {track_id}: {e}")

os.system("pause")
