"""Copyright (c) Void 2024 - Discord Bot Codebase

This module is made as a playground for testing new commands.
Later in Production this extension won't be loaded into the program,
so there won't be any issues in case of bugs.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

from discord import app_commands
import discord.ext

from settings import (
    GAME_CHOICES,
    MODE_CHOICES
)
from src.commands.test_commands import lets_play


class TestFeaturesCommandGroup(app_commands.Group):
    """Command Group

    Inherits from app_commands.Group. The decorators list the commands given as
    class methods. Calling the necessary command module after recognitions.
    """

    @app_commands.command(name="lets_play", description="DESCRIPTION")
    @app_commands.choices(game=GAME_CHOICES)
    @app_commands.choices(mode=MODE_CHOICES)
    @app_commands.describe(
        game="DESCRIPTION",
        player_count="DESCRIPTION"
    )
    async def command_lets_play(
            self,
            interaction: discord.Interaction,
            game: app_commands.Choice[str],
            mode: app_commands.Choice[str],
            player_count: int,
    ):
        """Calls the lets play function"""
        await lets_play.initialize(interaction, game, mode, player_count)

    @app_commands.command(name="avatar", description="DESCRIPTION")
    @app_commands.describe(user="DESCRIPTION")
    async def command_avatar(
            self,
            interaction:
            discord.Interaction,
            user: discord.Member
    ):
        """Returns the avatar as an embed"""
        embed = discord.Embed(title=f"Avatar of '{user.display_name}'", description="")
        embed.set_image(url=user.avatar.url)
        embed.set_footer(
            text=f"Called by {interaction.user.display_name}",
            icon_url=f"{interaction.user.avatar.url}"
        )
        await interaction.response.send_message(embed=embed)
        

# TODO: change description
async def setup(bot: discord.ext.commands.Bot):
    bot.tree.add_command(TestFeaturesCommandGroup(name="testing", description="DESCRIPTION"))