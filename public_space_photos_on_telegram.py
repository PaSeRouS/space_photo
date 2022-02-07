import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_photos, fetch_epic_photos
from fetch_spacex import fetch_spacex_last_launch


def public_photos_to_telegram(telegram_token, publication_delay):
    directories = [ "images", "nasa_photo", "epic_photo"]

    bot = telegram.Bot(token=telegram_token)

    for directory in directories:
        public_photo_to_telegram(bot, directory, publication_delay)


def public_photos(bot, directory, publication_delay):
    photos = listdir(directory)

    for photo in photos:
        filepath = f'images/{photo}'
        bot.sendPhoto(chat_id="@paser_space_photo", photo=open(filepath, 'rb'))
        time.sleep(int(publication_delay))


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    publication_delay = 86400 if not os.getenv('PUBLICATION_DELAY') else os.getenv('PUBLICATION_DELAY')

    fetch_spacex_last_launch()
    fetch_nasa_photos(nasa_token)
    fetch_epic_photos(nasa_token)

    public_photos_to_telegram(telegram_token, publication_delay)