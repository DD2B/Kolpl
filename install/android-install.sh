#!/bin/bash

# Install Python packages using pip3
pip3 install telethon requests python-telegram-bot
# Download the Python script
curl "https://raw.githubusercontent.com/kekoDev/kolpl/main/bot.py" > "bot.py"

reset
# Run the Python script
python3 bot.py

