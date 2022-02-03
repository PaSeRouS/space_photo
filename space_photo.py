import datetime
import os
from os.path import split, splitext

import requests
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import unquote, urlsplit


def upload_picture(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    Path("images").mkdir(parents=True, exist_ok=True)

    response = requests.get("https://api.spacexdata.com/v3/launches/67")
    response.raise_for_status()

    for url_number, url in enumerate(response.json()["links"]["flickr_images"]):
        filename = f'images/spacex{url_number}.jpg'
        upload_picture(url, filename)


def get_file_extension(url):
    return splitext(split(urlsplit(unquote(url)).path)[1])[1]


def fetch_nasa_photos(token):
    Path("nasa_photo").mkdir(parents=True, exist_ok=True)

    nasa_url = 'https://api.nasa.gov/planetary/apod'

    params = {
        'api_key' : f'{token}',
        'count' : 30
    }

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    nasa_photos = response.json()

    for number_of_photo, photo in enumerate(nasa_photos):
        file_extension = get_file_extension(photo["url"])
        filename = f'nasa_photo/nasa{number_of_photo}{file_extension}'
        upload_picture(photo["url"], filename)


def fetch_epic_photos(token):
    Path("epic_photo").mkdir(parents=True, exist_ok=True)

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    params = {
        'api_key' : f'{token}',
    }

    response = requests.get(epic_url, params=params)
    response.raise_for_status()

    epic_photos = response.json()

    for number_of_photo, photo in enumerate(epic_photos):
        date_time = datetime.datetime.fromisoformat(photo["date"])

        year = date_time.year
        month = f'{date_time.month:02d}'
        day = f'{date_time.day:02d}'

        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{photo["image"]}.png?api_key={token}'

        filename = f'epic_photo/epic{number_of_photo}.png'

        upload_picture(url, filename)


if __name__ == '__main__':
    load_dotenv()

    token = os.getenv('NASA_TOKEN')

    fetch_spacex_last_launch()
    fetch_nasa_photos(token)
    fetch_epic_photos(token)
  