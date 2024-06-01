# This file must be named lambda_function.py to work properly
from os import getenv

from telebot import TeleBot
from telebot.custom_filters import SimpleCustomFilter
from telebot.types import Update, Message


# A simple filter to detect Telegram Premium
class IsPremium(SimpleCustomFilter):
    key = 'is_premium'

    @staticmethod
    def check(message: Message):
        return message.from_user.is_premium is True


def main(event):
    bot = TeleBot(getenv("BOT_TOKEN"), threaded=False)
    bot.add_custom_filter(IsPremium())

    # Handler for non-premium users

    @bot.message_handler(is_premium=False)
    def any_message_from_non_premium(message: Message):
        bot.send_message(message.chat.id, "You need Telegram Premium to use this bot.")

    # All next handlers are for premium users

    @bot.message_handler(commands=['start'])
    def cmd_start(message: Message):
        bot.send_message(message.chat.id, "Hello! Looks like you have Telegram Premium. Happy now? ;)")

    @bot.message_handler(commands=['help'])
    def cmd_help(message: Message):
        bot.send_message(
            message.chat.id,
            (
                "You thought I can do something? Lol no :D\n"
                "Well, there might be some secret (and also useless) commands here. Good luck finding them!"
            )
        )

    @bot.message_handler(commands=['durov'])
    def cmd_durov(message: Message):
        bot.send_message(
            message.chat.id,
            "Okay, you found one of my secret commands. Clap. Clap. Clap."
        )

    update = Update.de_json(event["body"])
    bot.process_new_messages([update.message])


# This is the entrypoint,
# you MUST define lambda_handler() function
def lambda_handler(event, context):
    return main(event)
