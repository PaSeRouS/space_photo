import os

import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    telegram_token = os.getenv("TELEGRAM_TOKEN")

    bot = telegram.Bot(token=telegram_token)
    bot.sendPhoto(chat_id="@paser_space_photo", photo="https://vk.com/smuzi_msk?z=photo-164592450_457348371%2Falbum-164592450_00%2Frev")