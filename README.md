# Spotify-Import-Artists
Описание (Description):
Русский:
Данный скрипт позволяет пользователю автоматически подписываться на артистов в сервисе Spotify по списку, указанному в текстовом файле. Скрипт использует библиотеку Spotipy для взаимодействия с API Spotify. После указания учетных данных и списка артистов в файле, скрипт просматривает каждого артиста в списке, выполняет поиск в Spotify и подписывается на найденных артистов. Если артист не найден, он добавляется в отдельный файл для последующей проверки.

English:
This script allows users to automatically follow artists on Spotify based on a list provided in a text file. The script utilizes the Spotipy library to interact with the Spotify API. After specifying the credentials and the list of artists in the file, the script iterates through each artist in the list, performs a search on Spotify, and follows the found artists. If an artist is not found, it is added to a separate file for further review.

Инструкция (Instructions):
Русский:

Установите библиотеку Spotipy, используя pip install spotipy.
Запустите скрипт и убедитесь, что у вас есть учетные данные для доступа к API Spotify (CLIENT_ID и CLIENT_SECRET).
Укажите путь к текстовому файлу, содержащему список артистов (file_path).
Запустите скрипт, он выполнит авторизацию в Spotify и начнет добавление артистов в подписки.
По завершении работы скрипта вы получите уведомление об успешном добавлении всех артистов или о тех, которые не были найдены.
English:

Install the Spotipy library using pip install spotipy.
Run the script and make sure you have credentials for accessing the Spotify API (CLIENT_ID and CLIENT_SECRET).
Specify the path to the text file containing the list of artists (file_path).
Run the script; it will authenticate with Spotify and begin adding artists to your follows.
Once the script finishes, you will receive a notification indicating successful addition of all artists or those that were not found.
