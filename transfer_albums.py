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
albums = TidalUser1.albums()

# Sortowanie albumów według daty dodania (od najnowszego do najstarszego)
sorted_albums = sorted(albums, key=lambda x: x.user_date_added, reverse=False)

# Tworzenie lub otwieranie pliku do zapisu dla ID albumów z kodowaniem UTF-8
with open('album_id_list.txt', 'w', encoding='utf-8') as id_file:
    for album in sorted_albums:
        album_id = album.id
        id_file.write(f'{album_id}\n')

# Tworzenie lub otwieranie pliku do zapisu z pełnymi informacjami z kodowaniem UTF-8
with open('album_list.txt', 'w', encoding='utf-8') as full_info_file:
    for album in sorted_albums:
        album_id = album.id
        album_name = album.name
        added_date = album.user_date_added
        full_info_file.write(f'Album ID: {album_id}, Album Name: {album_name}, Added Date: {added_date}\n')

print('Albums saved to album_id_list.txt and album_list.txt')

filepath = 'album_id_list.txt'

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

os.system("pause")
