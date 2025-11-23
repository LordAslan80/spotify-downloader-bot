from django.apps import AppConfig
import os
import threading


class DownloaderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "downloader"

    def ready(self):
        if os.environ.get("RUN_MAIN") != "true":
            return

        bot_thread = threading.Thread(target=self.start_bot, daemon=True)
        bot_thread.start()

    def start_bot(self):
        from .bot import start_bot

        start_bot()
