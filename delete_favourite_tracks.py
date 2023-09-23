import tidalapi
import tqdm # Importuj bibliotekę tqdm

session = tidalapi.Session()
session.login_oauth_simple() # Zaloguj się do konta Tidal

user = session.user # Uzyskaj obiekt użytkownika
tracks = user.favorites.tracks() # Uzyskaj listę polubionych utworów

for track in tqdm.tqdm(tracks): # Opakuj listę utworów w obiekt tqdm
    user.favorites.remove_track(track.id) # Usuń utwór z listy ulubionych

print("Usunięto wszystkie polubione utwory z konta Tidal.")

