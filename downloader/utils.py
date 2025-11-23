import requests
import os
from urllib.parse import urlparse
from spotify_downloader_bot.settings import ENV_FILE
from .models import UserData
from asgiref.sync import sync_to_async


def api(song_url: str):
    url = ENV_FILE["API_URL"]

    querystring = {"urls": song_url}

    payload = {"key1": "value", "key2": "value"}
    headers = {
        "x-rapidapi-key": ENV_FILE["API_KEY"],
        "x-rapidapi-host": ENV_FILE["API_HOST"],
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    return response.json()


def get_song(get_path: str, get_url: str):
    try:
        response = requests.get(get_url, stream=True)
        response.raise_for_status()

        filename = os.path.basename(urlparse(get_url).path)
        if not filename:
            filename = "downloaded_file"
        save_path = os.path.join(get_path, f"{filename}.mp3")

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return save_path

    except Exception as e:
        print(f"Download failed: {e}")


def remove_song(remove_path):
    os.remove(remove_path)


@sync_to_async
def save_user_data(account_name, username, requested_url):
    UserData.objects.create(
        account_name=account_name,
        username=username,
        requested_url=requested_url,
    )
