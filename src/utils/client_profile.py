"""Copyright (c) Void 2024 - Discord Bot Codebase

The "client_profile" module is made to customize the bots profile in any given way.
The functions change the presence and the online status depending on what you want to change.
The bot can also change to a custom activity.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import logging

import discord


logger = logging.getLogger("bot")

async def change_presence(
        bot: discord.Client,
        current_status: str,
        activity_name_value: str = "",
        current_activity: str ="Codebase"
) -> None:
    """Changing the Discord clients presence

    Args:
        bot: The Discord bot defined as discord.Client
        current_status: Is the status activity the bot should get
        activity_name_value: Is the name of the activity
        current_activity: Is the Name of the activity
    """

    discord_status = discord.Status.online
    match current_status:
        case "online":
            discord_status = discord.Status.online
        case "idle":
            discord_status = discord.Status.idle
        case "do_not_disturb":
            discord_status = discord.Status.do_not_disturb
        case "invisible":
            discord_status = discord.Status.invisible

    match activity_name_value:
        case "listening":
            activity_name = discord.ActivityType.listening
            await bot.change_presence(
                status=discord_status,
                activity=discord.Activity(
                    type=activity_name,
                    name=current_activity
                ),
            )
        case "playing":
            activity_name = discord.ActivityType.playing
            await bot.change_presence(
                status=discord_status,
                activity=discord.Activity(
                    type=activity_name,
                    name=current_activity
                ),
            )
        case "streaming":
            await bot.change_presence(
                status=discord_status,
                activity=discord.Streaming(
                    name=current_activity,
                    url="https://twitch.tv/discord"
                ),
            )
        case _:
            activity_name = discord.ActivityType.listening
            await bot.change_presence(
                status=discord_status,
                activity=discord.Activity(
                    type=activity_name,
                    name=current_activity
                ),
            )

    logger.info(f"Presence changed to '{current_status}' with activity '{activity_name_value} {current_activity}'")