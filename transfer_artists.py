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
artists = TidalUser1.artists()

# Sortowanie artystów według daty dodania (od najnowszego do najstarszego)
sorted_artists = sorted(artists, key=lambda x: x.user_date_added, reverse=False)

# Tworzenie lub otwieranie pliku do zapisu dla ID artystów z kodowaniem UTF-8
with open('artist_id_list.txt', 'w', encoding='utf-8') as id_file:
    for artist in sorted_artists:
        artist_id = artist.id
        id_file.write(f'{artist_id}\n')

# Tworzenie lub otwieranie pliku do zapisu z pełnymi informacjami z kodowaniem UTF-8
with open('artist_list.txt', 'w', encoding='utf-8') as full_info_file:
    for artist in sorted_artists:
        artist_id = artist.id
        artist_name = artist.name
        added_date = artist.user_date_added
        full_info_file.write(f'Artist ID: {artist_id}, Artist Name: {artist_name}, Added Date: {added_date}\n')

print('Artists saved to artist_id_list.txt and artist_list.txt')

filepath = 'artist_id_list.txt'

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

os.system("pause")
