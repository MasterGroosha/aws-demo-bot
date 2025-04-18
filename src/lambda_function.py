# This file must be named lambda_function.py to work properly
import asyncio
from json import loads
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

dp = Dispatcher()


@dp.message(~F.from_user.is_premium)
async def any_msg_from_non_premium(message: Message):
    await message.answer("You need Telegram Premium to use this bot.")


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Hello! Looks like you have Telegram Premium. Happy now? ;)",
        message_effect_id="5104841245755180586",
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "You thought I can do something? Lol no :D\n"
        "Well, there might be some secret (and also useless) commands here. Good luck finding them!"
    )


@dp.message(Command("durov"))
async def cmd_help(message: Message):
    await message.answer(
        "Okay, you found one of my secret commands. Clap. Clap. Clap."
    )


async def main(event):
    bot = Bot(token=getenv("BOT_TOKEN"))
    await dp.feed_raw_update(bot, event)

# This is the entrypoint,
# you MUST define lambda_handler() function
def lambda_handler(event, context):
    return asyncio.run(main(loads(event["body"])))
