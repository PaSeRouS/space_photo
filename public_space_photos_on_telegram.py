import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_launch_photos
from fetch_nasa import fetch_nasa_photos, fetch_epic_photos


def public_photos(telegram_token, publication_delay, telegram_channel_name):
    directories = [ "images", "nasa_photos", "epic_photos"]

    bot = telegram.Bot(token=telegram_token)

    for directory in directories:
        public_photos_to_telegram(bot, directory, publication_delay, telegram_channel_name)


def public_photos_to_telegram(bot, directory, publication_delay, telegram_channel_name):
    photos = listdir(directory)

    for photo in photos:
        filepath = f'{directory}/{photo}'

        with open(filepath, 'rb') as file:
            data = file.read()

        bot.sendPhoto(chat_id=telegram_channel_name, photo=data)
        time.sleep(int(publication_delay))


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    publication_delay = 86400 if not os.getenv('PUBLICATION_DELAY') else os.getenv('PUBLICATION_DELAY')
    telegram_channel_name = os.getenv("TELEGRAM_CHANNEL_NAME")

    fetch_spacex_launch_photos("images")
    # fetch_nasa_photos(nasa_token, "nasa_photos")
    # fetch_epic_photos(nasa_token, "epic_photos")

    public_photos(telegram_token, publication_delay, telegram_channel_name)