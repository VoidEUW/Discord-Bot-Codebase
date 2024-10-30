"""Copyright (c) Void 2024 - Discord Bot Codebase

This is the Shogun Bot Class that controls the
whole bot.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import discord
from discord.ext import commands

import settings
from src.controller import event_listener
from src.utils import client_profile


class CustomDiscordBot(commands.Bot):
    """Provides the whole bot with important information"""

    def listen_events(
            self,
            current_status: str,
            activity_name_value: str,
            current_activity: str
    ) -> None:
        """Activates the event listener"""
        event_listener.listen(self, settings.DEBUG, current_status, activity_name_value, current_activity)
