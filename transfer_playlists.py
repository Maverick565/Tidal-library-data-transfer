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
playlists = TidalUser1.playlists()

# Sortowanie playlist według daty dodania (od najnowszego do najstarszego)
sorted_playlists = sorted(playlists, key=lambda x: x.last_updated, reverse=False)

# Tworzenie lub otwieranie pliku do zapisu dla ID playlist z kodowaniem UTF-8
with open('playlist_id_list.txt', 'w', encoding='utf-8') as id_file:
    for playlist in sorted_playlists:
        playlist_id = playlist.id
        id_file.write(f'{playlist_id}\n')

# Tworzenie lub otwieranie pliku do zapisu z pełnymi informacjami z kodowaniem UTF-8
with open('playlist_list.txt', 'w', encoding='utf-8') as full_info_file:
    for playlist in sorted_playlists:
        playlist_id = playlist.id
        playlist_name = playlist.name
        last_updated = playlist.last_updated
        full_info_file.write(f'Playlist ID: {playlist_id}, Playlist Name: {playlist_name}, Last Updated: {last_updated}\n')

print('Playlists saved to playlist_id_list.txt and playlist_list.txt')

filepath = 'playlist_id_list.txt'

# Zaloguj się na swoje drugie konto TIDAL
session2 = tidalapi.Session()
print('Enter your credentials for the account you want to transfer to')
session2.login_oauth_simple()
uid2 = session2.user.id
TidalUser2 = tidalapi.Favorites(session2, uid2)

print('Adding ...')
with open(filepath) as f:
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

os.system("pause")
