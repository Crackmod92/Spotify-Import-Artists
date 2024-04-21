# Spotify-Import-Artists

Русский:
---
Данный скрипт позволяет пользователю автоматически подписываться на артистов в сервисе Spotify по списку, указанному в текстовом файле.
Скрипт использует библиотеку Spotipy для взаимодействия с API Spotify.
После указания учетных данных и списка артистов в файле, скрипт просматривает каждого артиста в списке, выполняет поиск в Spotify и подписывается на найденных артистов.
Если артист не найден, он добавляется в отдельный файл для последующей проверки. 

Для начала работ, у вас должен быть установлен Python. Все действия выполняются в любом текстовом редакторе (например, Notepad++) и командной строке CMD.

English:
---
This script allows users to automatically follow artists on Spotify based on a list provided in a text file. 
The script utilizes the Spotipy library to interact with the Spotify API. After specifying the credentials and the list of artists in the file, the script iterates through each artist in the list, performs a search on Spotify, and follows the found artists. 
If an artist is not found, it is added to a separate file for further review.

All actions are performed in any text editor (for example, Notepad++) and CMD.

# Инструкция (Instructions):

Русский:
---
1. Установите библиотеку Spotipy, используя ***`pip install spotipy`***.
2. Запустите скрипт и убедитесь, что у вас есть учетные данные для доступа к API Spotify.
3. Получите свой CLIENT_ID и CLIENT_SECRET на панели управления разработчика Spotify (https://developer.spotify.com/dashboard).
4. Укажите путь к текстовому файлу, содержащему список артистов (file_path).
5. Укажите REDIRECT_URI в скрипте. REDIRECT_URI - это URL, на который Spotify перенаправит пользователя после авторизации. Вы можете установить его на любой допустимый URL. Для локальной разработки вы можете использовать 'http://localhost:8080/login'.
6. Запустите скрипт `py spotify_import.py`; он выполнит аутентификацию в Spotify и начнет добавление артистов в ваши подписки.
7. По завершении работы скрипта вы получите уведомление об успешном добавлении всех артистов или о тех, которые не были найдены.

English:
---
1. Install the Spotipy library using ***`pip install spotipy`***.
2. Run the script and make sure you have credentials for accessing the Spotify API.
3. Obtain your CLIENT_ID and CLIENT_SECRET from the Spotify Developer Dashboard (https://developer.spotify.com/dashboard).
4. Specify the path to the text file containing the list of artists (file_path).
5. Specify the REDIRECT_URI in the script. REDIRECT_URI is the URL where Spotify will redirect the user after authorization. You can set it to any valid URL. For local development, you can use 'http://localhost:8080/login'.
6. Run the script `py spotify_import.py`; it will authenticate with Spotify and begin adding artists to your follows.
7. Once the script finishes, you will receive a notification indicating successful addition of all artists or those that were not found.
