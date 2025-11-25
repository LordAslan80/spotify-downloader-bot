# Spotify Downloader Telegram-Bot

## About
A simple Telegram bot that downloads Spotify tracks as MP3 files. Send any Spotify track URL to the bot, and it will return the audio file.

## Prerequisites
- Python 3.10+
- [Telegram Bot Token](https://core.telegram.org/bots#6-botfather) (from @BotFather)
- [RapidAPI Account](https://rapidapi.com/hub) (for Spotify Downloader API)
- Git installed

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/LordAslan80/spotify-downloader-bot.git
cd spotify-downloader-bot
```

### 2. Create a `.env` file in the project root with the following content:
```python
# Django settings
SECRET_KEY="your_django_secret_key_here"

# Telegram Bot
BOT_TOKEN="your_telegram_bot_token"

# RapidAPI Spotify Downloader
API_URL="your_spotify_downloader_rapidapi_url"
API_KEY="your_rapidapi_key"
API_HOST="your_spotify_downloader_rapidapi_host"
```

### 3. Create Telegram Bot 
   * Message [@BotFather](https://t.me/BotFather)  on Telegram 
   * Use `/newbot` command and follow the prompts 
   * Copy the token and paste it in `.env`'s `BOT_TOKEN` field 

### 4. Create virtual environment
```bash
python -m venv .venv
```

### 5. Activate virtual environment
   * Windows:
      ```bash
      .venv\Scripts\activate
      ```
   * macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

### 6. Install dependencies
```bash
pip install -r requirements.txt
```

### 7. Generate Django Secret Key
   * First use:
      ```bash
      python manage.py shell
      ```
   * Then run in Python shell:
      ```python
      from django.core.management.utils import get_random_secret_key
      print(get_random_secret_key())
      ```
   * Copy the output to `.env`'s `SECRET_KEY` field

### 8. Run database migrations
```bash
python manage.py migrate
```

### 9. Create admin user (optional)
```bash
python manage.py createsuperuser
```

### 10. Start the server
```bash
python manage.py runserver
```

## Usage 
   1. Start the server with Step 10 
   2. Send any Spotify track URL to your bot in Telegram 
   3. The bot will reply with an MP3 file 
