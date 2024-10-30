"""Copyright (c) Void 2024 - Discord Bot Codebase

This module is for loading up all necessary variables needed. The DISCORD_API_SECRET is hidden
behind an ".env" file to ensure that the token is not leaked. Any other important sensitive information
is saved inside of this ".env" file.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

from logging.config import dictConfig
import os
from tkinter.constants import COMMAND

from discord import app_commands
from dotenv import load_dotenv


DEBUG = True # DEBUG MODE

LOCAL_PATH = "data/local"
CACHE_PATH = "data/local/cache"

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

COMMAND_LIST = [
    ("client", False), # ("location", DEBUG)
    ("devtools", False),
    ("testing", True)
]

GAME_CHOICES = [
    app_commands.Choice(name="Choice", value="choice")
]

MODE_CHOICES = [
    app_commands.Choice(name="Choice", value="choice"),
]

GROUP_REPORT_CHOICES = [
    app_commands.Choice(name="Other", value="Other")
]

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "data/logs/infos.log",
            "mode": "w",
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        }
    }
}
dictConfig(LOGGING_CONFIG)