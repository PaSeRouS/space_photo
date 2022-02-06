import requests
from pathlib import Path


def upload_picture(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    Path("images").mkdir(parents=True, exist_ok=True)

    response = requests.get("https://api.spacexdata.com/v3/launches/45")
    response.raise_for_status()

    for url_number, url in enumerate(response.json()["links"]["flickr_images"]):
        filename = f'images/spacex{url_number}.jpg'
        upload_picture(url, filename)


if __name__ == '__main__':
    fetch_spacex_last_launch()
