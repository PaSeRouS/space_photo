import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa
from fetch_spacex import fetch_spacex_last_launch


def public_photo_on_telegram():
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    publication_delay = os.getenv('PUBLICATION_DELAY')

    if not publication_delay:
        publication_delay = 86400

    photos_spacex_for_telegram = listdir("images")
    photos_nasa_for_telegram = listdir("nasa_photo")
    photos_epic_for_telegram = listdir("epic_photo")
  
    bot = telegram.Bot(token=telegram_token)

    while True:
        for photo in photos_spacex_for_telegram:
            filepath = f'images/{photo}'
            bot.sendPhoto(chat_id="@paser_space_photo", photo=open(filepath, 'rb'))
            time.sleep(int(publication_delay))

        for photo in photos_nasa_for_telegram:
            filepath = f'nasa_photo/{photo}'
            bot.sendPhoto(chat_id="@paser_space_photo", photo=open(filepath, 'rb'))
            time.sleep(int(publication_delay))

        for photo in photos_epic_for_telegram:
            filepath = f'epic_photo/{photo}'
            bot.sendPhoto(chat_id="@paser_space_photo", photo=open(filepath, 'rb'))
            time.sleep(int(publication_delay))


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os>getenv("NASA_TOKEN")

    fetch_spacex_last_launch()
    fetch_nasa_photos(nasa_token)
    fetch_epic_photos(nasa_token)

    public_photo_on_telegram()