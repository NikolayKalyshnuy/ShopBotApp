from aiogram import types
from main import bot

async def set_default_commands(dp):
    await bot.set_my_commands([
        types.BotCommand('start', 'Run the bot'),
        types.BotCommand('help', 'Help'),
        types.BotCommand('register', 'Registration')

    ])
