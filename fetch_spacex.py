import requests
from pathlib import Path

from download_files import download_picture


def fetch_spacex_launch_photos(path):
    Path(path).mkdir(parents=True, exist_ok=True)

    response = requests.get("https://api.spacexdata.com/v3/launches/45")
    response.raise_for_status()

    for url_number, url in enumerate(response.json()["links"]["flickr_images"]):
        filename = f'{path}/spacex{url_number}.jpg'
        download_picture(url, filename)


if __name__ == '__main__':
    fetch_spacex_launch_photos("images")
