import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Your credentials for the Spotify API // Ваши учетные данные от Spotify API
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''
file_path = r''

# Reading the list of artists from a file // Чтение списка артистов из файла
with open(file_path) as file:
    artists = file.readlines()
artists = [artist.strip() for artist in artists]

# Creating a SpotifyOAuth object with the required permissions (scope) // Создание объекта SpotifyOAuth с указанием требуемых прав (scope)
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope='user-follow-modify')

# User authorization // Авторизация пользователя
sp = spotipy.Spotify(auth_manager=sp_oauth)

not_found_artists = []
added_artists = {}  # Dictionary for tracking added artists // Словарь для отслеживания добавленных артистов

# Adding each artist to follows // Добавление каждого артиста в подписки
for artist in artists:
    results = sp.search(q='artist:' + artist, type='artist')
    if results['artists']['items']:
        for item in results['artists']['items']:
            artist_id = item['id']
            artist_name = item['name']
            # Checking that the found artist exactly matches the query // Проверяем, что найденный артист точно соответствует запросу
            if artist_name.lower() == artist.lower():
                if artist_id not in added_artists:
                    sp.user_follow_artists([artist_id])
                    added_artists[artist_id] = artist_name
                    print(f"Added {artist_name} to your Spotify follows.")
                break  # Breaking the loop if the artist was added // Прерываем цикл, если артист был добавлен
        else:
            # If the loop did not break, it means the artist was not added // Если цикл не прервался, значит артист не был добавлен
            print(f"Could not find {artist} on Spotify.")
            not_found_artists.append(artist)
    else:
        print(f"Could not find {artist} on Spotify.")
        not_found_artists.append(artist)
    
    # Adding a small delay between requests to avoid API limits // Добавляем небольшую задержку между запросами, чтобы не превысить лимиты API
    time.sleep(0.5)  # Delay of 0.5 seconds // Задержка в 0.5 секунды

# Writing not found artists to a file // Запись не найденных артистов в файл
if not_found_artists:
    with open('not_found.txt', 'w') as file:
        file.write('\n'.join(not_found_artists))

print("All artists added successfully!")
