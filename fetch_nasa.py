import datetime
import os
from os.path import split, splitext

import requests
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import unquote, urlsplit

from download_files import download_picture


def get_file_extension(url):
    return splitext(split(urlsplit(unquote(url)).path)[1])[1]


def fetch_nasa_photos(token, path):
    Path(path).mkdir(parents=True, exist_ok=True)

    nasa_url = 'https://api.nasa.gov/planetary/apod'

    params = {
        'api_key' : token,
        'count' : 30
    }

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    nasa_photos = response.json()

    for number_of_photo, photo in enumerate(nasa_photos):
        file_extension = get_file_extension(photo["url"])
        filename = f'{path}/nasa{number_of_photo}{file_extension}'
        download_picture(photo["url"], filename)


def fetch_epic_photos(token, path):
    Path(path).mkdir(parents=True, exist_ok=True)

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    params = {
        'api_key' : token,
    }

    response = requests.get(epic_url, params=params)
    response.raise_for_status()

    epic_photos = response.json()

    for number_of_photo, photo in enumerate(epic_photos):
        date_time = datetime.datetime.fromisoformat(photo["date"])

        year = date_time.year
        month = f'{date_time.month:02d}'
        day = f'{date_time.day:02d}'

        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{photo["image"]}.png'

        filename = f'{path}/epic{number_of_photo}.png'

        download_picture(url, filename, params)


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os.getenv('NASA_TOKEN')

    fetch_nasa_photos(nasa_token, "nasa_photos")
    fetch_epic_photos(nasa_token, "epic_photos")
