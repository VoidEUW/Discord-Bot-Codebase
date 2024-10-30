"""Copyright (c) Void 2024 - Discord Bot Codebase

The "event_listener" module is made to list up all events the bot can get.
If necessary it will call necessary functions in the "events" folder. Listed events:
    - on_ready
    - on_message(. / edit / delete)
    - on_typing
    - on_reaction(add / remove)
    - on_member(join / remove / update)
    - on_user
    - on_voice_state_update
    - on_guild(role_create / role_update / role_delete)
    - on_scheduled_event(create / update/ delete / user_add / user_remove)

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import logging

import discord.ext

import settings
from src.utils.client_profile import change_presence


log = logging.getLogger("bot")

def listen(
        client: discord.ext.commands.Bot,
        debug_mode: bool=False,
        current_status="do_no_disturb",
        activity_name_value="listening",
        current_activity="Codebase"
) -> None:
    """Event listener listing all possible events

    Listening for all necessary events the discord.py library offers. Referring to other
    functions if needed. Only used for logging and function calls.

    Args:
        client: The Discord bot defined as discord.ext.commands.Bot
        debug_mode: Deciding whether the bot is launched in debug mode or not
        current_status: What status the bot gets at startup
        activity_name_value: What activity the bot has
        current_activity: The description of the activity
    """

    @client.event
    async def on_ready():
        """When bot is ready"""
        try:
            for command in settings.COMMAND_LIST:
                if (debug_mode == True and command[-1] == True) or (debug_mode == True and command[-1] == False) or (debug_mode == False and command[-1] == False):
                    log.info(f"Loading group: '{command[0]}'")
                    await client.load_extension(f"src.commands.{command[0]}")
        except Exception as err:
            log.error(f"{err}")
            log.info(f"Extensions couldn't be loaded")
        log.info(f"Logged in as '{client.user}' (ID: {client.user.id})")
        log.info(f"Connected to {len(client.guilds)} guild(s)")
        await change_presence(client, current_status, activity_name_value, current_activity)
        await client.tree.sync()

    @client.event
    async def on_message(msg):
        """When message arrives"""
        if msg.author == client.user:
            return
        log.info(f"'{msg.author}' in '{msg.channel}': {msg.content}")

    @client.event
    async def on_typing(channel, user, _):
        """When someone is typing a message"""
        log.info(f"'{user}' is typing in '{channel}'")

    @client.event
    async def on_message_edit(before, after):
        """When a message has been edited"""
        log.info(f"Message edited by '{before.author}': {before.content} -> {after.content}")

    @client.event
    async def on_message_delete(msg):
        """When a message has been deleted"""
        log.info(f"Message deleted by '{msg.author}': {msg.content}")

    @client.event
    async def on_reaction_add(reaction, user):
        """When somebody reacted to a message"""
        log.info(f"'{user}' reacted with '{reaction.emoji}'")

    @client.event
    async def on_reaction_remove(reaction, user):
        """When somebody removed a reaction from a message"""
        log.info(f"'{user}' removed reaction '{reaction.emoji}'")

    @client.event
    async def on_member_join(member):
        """When a member joins the guild"""
        log.info(f"'{member}' joined the server.")

    @client.event
    async def on_member_remove(member):
        """When a member leaves the guild"""
        log.info(f"'{member}' left the server.")

    @client.event
    async def on_member_update(before, after):
        """When a member changes their profile"""
        log.info(f"'{before}' updated to '{after}'")

    @client.event
    async def on_user_update(before, after):
        """When a user changes their profile"""
        log.info(f"'{before}' updated to '{after}'")

    @client.event
    async def on_member_ban(guild, user):
        """When a member has been banned"""
        log.info(f"'{user}' got banned from '{guild}'")

    @client.event
    async def on_member_unban(guild, user):
        """When a member has been unbanned"""
        log.info(f"'{user}' got unbanned from '{guild}'")

    @client.event
    async def on_voice_state_update(member, before, after):
        """When a member changes their voice activity in the guild"""
        pass

    @client.event
    async def on_guild_role_create(role):
        """When a role has been created"""
        pass

    @client.event
    async def on_guild_role_update(before, after):
        """When a role has been updated"""
        pass

    @client.event
    async def on_guild_role_delete(role):
        """When a role has been deleted"""
        pass

    @client.event
    async def on_scheduled_event_create(event):
        """When an event has been created"""
        pass

    @client.event
    async def on_scheduled_event_update(before, after):
        """When an event has been updated"""
        pass

    @client.event
    async def on_scheduled_event_delete(event):
        """When an event has been deleted"""
        pass

    @client.event
    async def on_scheduled_event_user_add(event, user):
        """When a user has been added to an event"""
        pass

    @client.event
    async def on_scheduled_event_user_remove(event, user):
        """When a user has been removed from an event"""
        pass