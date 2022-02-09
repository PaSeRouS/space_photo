import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_launch_photos
from fetch_nasa import fetch_nasa_photos, fetch_epic_photos


def send_photos_to_telegram(bot, directory, publication_delay, telegram_channel_name):
    photos = listdir(directory)

    for photo in photos:
        filepath = f'{directory}/{photo}'

        with open(filepath, 'rb') as file:
            photo_data = file.read()

        bot.sendPhoto(chat_id=telegram_channel_name, photo=photo_data)
        time.sleep(int(publication_delay))


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    publication_delay = os.getenv('PUBLICATION_DELAY', 86400)
    telegram_channel_name = os.getenv("TELEGRAM_CHANNEL_NAME")

    fetch_spacex_launch_photos("images")
    fetch_nasa_photos(nasa_token, "nasa_photos")
    fetch_epic_photos(nasa_token, "epic_photos")

    directories = [ "images", "nasa_photos", "epic_photos"]
    bot = telegram.Bot(token=telegram_token)

    while True:
        for directory in directories:
            send_photos_to_telegram(bot, directory, publication_delay, telegram_channel_name)
