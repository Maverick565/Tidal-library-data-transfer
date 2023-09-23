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
tracks = TidalUser1.tracks()

# Sortowanie utworów według daty dodania (od najnowszego do najstarszego)
sorted_tracks = sorted(tracks, key=lambda x: x.user_date_added, reverse=False)

# Tworzenie lub otwieranie pliku do zapisu dla ID utworów z kodowaniem UTF-8
with open('track_id_list.txt', 'w', encoding='utf-8') as id_file:
    for track in sorted_tracks:
        track_id = track.id
        id_file.write(f'{track_id}\n')

# Tworzenie lub otwieranie pliku do zapisu z pełnymi informacjami z kodowaniem UTF-8
with open('track_list.txt', 'w', encoding='utf-8') as full_info_file:
    for track in sorted_tracks:
        track_id = track.id
        track_name = track.name
        added_date = track.user_date_added
        full_info_file.write(f'Track ID: {track_id}, Track Name: {track_name}, Added Date: {added_date}\n')

print('Tracks saved to track_id_list.txt and track_list.txt')

filepath = 'track_id_list.txt'

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
