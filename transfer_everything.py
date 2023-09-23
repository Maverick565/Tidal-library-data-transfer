import tidalapi
from tqdm import tqdm
import requests
import os

# Zaloguj się na swoje pierwsze konto TIDAL
session1 = tidalapi.Session()
print('Enter your credentials for the account you want to transfer from')
session1.login_oauth_simple()
uid1 = session1.user.id
TidalUser1 = tidalapi.Favorites(session1, uid1)

# Pobierz ulubione albumy, artystów, playlisty i utwory z pierwszego konta
albums = TidalUser1.albums()
artists = TidalUser1.artists()
playlists = TidalUser1.playlists()
tracks = TidalUser1.tracks()

# Sortowanie albumów, artystów, playlist i utworów według daty dodania (od najnowszego do najstarszego)
sorted_albums = sorted(albums, key=lambda x: x.user_date_added, reverse=False)
sorted_artists = sorted(artists, key=lambda x: x.user_date_added, reverse=False)
sorted_playlists = sorted(playlists, key=lambda x: x.last_updated, reverse=False)
sorted_tracks = sorted(tracks, key=lambda x: x.user_date_added, reverse=False)

# Tworzenie lub otwieranie plików do zapisu dla ID albumów, artystów, playlist i utworów z kodowaniem UTF-8
with open('album_id_list.txt', 'w', encoding='utf-8') as album_id_file:
    for album in sorted_albums:
        album_id = album.id
        album_id_file.write(f'{album_id}\n')

with open('artist_id_list.txt', 'w', encoding='utf-8') as artist_id_file:
    for artist in sorted_artists:
        artist_id = artist.id
        artist_id_file.write(f'{artist_id}\n')

with open('playlist_id_list.txt', 'w', encoding='utf-8') as playlist_id_file:
    for playlist in sorted_playlists:
        playlist_id = playlist.id
        playlist_id_file.write(f'{playlist_id}\n')

with open('track_id_list.txt', 'w', encoding='utf-8') as track_id_file:
    for track in sorted_tracks:
        track_id = track.id
        track_id_file.write(f'{track_id}\n')

# Tworzenie lub otwieranie plików do zapisu z pełnymi informacjami z kodowaniem UTF-8
with open('album_list.txt', 'w', encoding='utf-8') as full_info_album_file:
    for album in sorted_albums:
        album_id = album.id
        album_name = album.name
        added_date = album.user_date_added
        full_info_album_file.write(f'Album ID: {album_id}, Album Name: {album_name}, Added Date: {added_date}\n')

with open('artist_list.txt', 'w', encoding='utf-8') as full_info_artist_file:
    for artist in sorted_artists:
        artist_id = artist.id
        artist_name = artist.name
        added_date = artist.user_date_added
        full_info_artist_file.write(f'Artist ID: {artist_id}, Artist Name: {artist_name}, Added Date: {added_date}\n')

with open('playlist_list.txt', 'w', encoding='utf-8') as full_info_playlist_file:
    for playlist in sorted_playlists:
        playlist_id = playlist.id
        playlist_name = playlist.name
        last_updated = playlist.last_updated
        full_info_playlist_file.write(f'Playlist ID: {playlist_id}, Playlist Name: {playlist_name}, Last Updated: {last_updated}\n')

with open('track_list.txt', 'w', encoding='utf-8') as full_info_track_file:
    for track in sorted_tracks:
        track_id = track.id
        track_name = track.name
        added_date = track.user_date_added
        full_info_track_file.write(f'Track ID: {track_id}, Track Name: {track_name}, Added Date: {added_date}\n')

print('Albums saved to album_id_list.txt and album_list.txt')
print('Artists saved to artist_id_list.txt and artist_list.txt')
print('Playlists saved to playlist_id_list.txt and playlist_list.txt')
print('Tracks saved to track_id_list.txt and track_list.txt')

# Zaloguj się na swoje drugie konto TIDAL
session2 = tidalapi.Session()
print('Enter your credentials for the account you want to transfer to')
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
