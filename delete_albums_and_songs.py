import tidalapi
import tqdm # Importuj bibliotekę tqdm
import os

session = tidalapi.Session()
session.login_oauth_simple() # Zaloguj się do konta Tidal

user = session.user # Uzyskaj obiekt użytkownika
tracks = user.favorites.tracks() # Uzyskaj listę polubionych utworów
albums = user.favorites.albums() # Uzyskaj listę polubionych albumów

for track in tqdm.tqdm(tracks): # Opakuj listę utworów w obiekt tqdm
    user.favorites.remove_track(track.id) # Usuń utwór z listy ulubionych

for album in tqdm.tqdm(albums): # Opakuj listę albumów w obiekt tqdm
    user.favorites.remove_album(album.id) # Usuń album z listy ulubionych

print("Usunięto wszystkie polubione utwory i albumy z konta Tidal.")
os.system('pause') # Dodaj pauzę na końcu skryptu
