"""Copyright (c) Void 2024 - Discord Bot Codebase

The class for grouping all client commands of the bot.
Here you can find following commands:
    - ping
    - help
    - report_bug

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

from discord import app_commands
import discord.ext

import settings
from settings import GROUP_REPORT_CHOICES
from src.commands.client_commands import (
    help,
    report_bug
)


class ClientCommandGroup(app_commands.Group):
    """Command Group

    Inherits from app_commands.Group. The decorators list the commands given as
    class methods. Calling the necessary command module after recognitions.
    """

    @app_commands.command(name="ping", description="DESCRIPTION")
    async def ping(self, interaction: discord.Interaction):
        """Responding with a Pong and the latency in ms"""
        await interaction.response.send_message(f"Pong! {round(interaction.client.latency * 1000)}ms")

    @app_commands.command(name="help", description="DESCRIPTION")
    @app_commands.describe()
    async def command_help(self, interaction: discord.Interaction):
        await help.initialize(interaction)

    @app_commands.command(name="report_bug", description="DESCRIPTION")
    @app_commands.choices(group=GROUP_REPORT_CHOICES)
    @app_commands.describe(
        group="DESCRIPTION",
        bug_description="DESCRIPTION"
    )
    async def command_report_bug(self, interaction: discord.Interaction, group: app_commands.Choice[str], bug_description: str):
        await report_bug.initialize(interaction, group, bug_description)


async def setup(bot: discord.ext.commands.Bot):
    bot.tree.add_command(ClientCommandGroup(name="client", description="DESCRIPTION"))