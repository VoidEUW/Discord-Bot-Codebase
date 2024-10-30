"""Copyright (c) Void 2024 - Discord Bot Codebase

This module is made to launch the bot and load up all
necessary functions. This module is only made to launch up
the bot, nothing else.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import discord

import settings
from src.classes.client import CustomDiscordBot


def main() -> None:
    """Preparing intents and starting bot"""
    intents: discord.Intents = set_properties()
    client = CustomDiscordBot(command_prefix="!", intents=intents)
    client.listen_events("streaming", "streaming", "Codebase")
    client.run(settings.DISCORD_TOKEN, root_logger=True)

def set_properties() -> discord.Intents:
    intents = discord.Intents.all()  # remove before release  -> discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.dm_messages = True
    return intents

if __name__ == "__main__":
    main()