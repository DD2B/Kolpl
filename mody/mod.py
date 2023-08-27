from pyrogram import Client
from pyrogram import filters

from mody.Redis import db
from mody.get_info import token, sudo_info, get_bot

Bot = Client(
    'MainBot',
    19653519,
    '186c3adb292c12bdf180ff27952e6ee1',
    bot_token=token,
    plugins=dict(root='plugins/bot')
)


sudo_client = Client(
    'MainUser',
    19653519,
    '186c3adb292c12bdf180ff27952e6ee1',
    session_string=db.get(f'{get_bot.id}:{sudo_info.id}:session'),
    plugins=dict(root='plugins/user')
)
sudo_client.login = False


def Bfilter(text):
    return filters.msg(text) & filters.private & filters.user(sudo_info.id)

