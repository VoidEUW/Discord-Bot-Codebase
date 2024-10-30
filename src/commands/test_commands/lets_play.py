"""Copyright (c) Void 2024 - Discord Bot Codebase

This module is a play together feature to ask players for a game you
want to play - 'Work in Progress'

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import json

import discord
from discord import app_commands

from settings import LOCAL_PATH


class LetsPlayView(discord.ui.View):
    """Embed View of lets play

    In this class all methods are described for
    creating an embed and listing all players who
    activated buttons to play or decline the game
    """
    initiator: discord.Member = None
    message: discord.Message = None
    game_value: str = ""
    game: dict = {}
    mode_value: str = ""
    status_list = ["Joined", "Declined", "Not sure"]
    player_count: int = 0
    current_players: list[discord.Member] = []
    player_list: list[tuple[discord.Member, str]] = []
    channel = None

    async def send_message(self, interaction: discord.Interaction):
        """Sending the message"""
        self.player_list = [(self.initiator, "Joined")]
        initial_channel = self.initiator.voice
        embed = await self.create_embed()

        await interaction.response.send_message(view=self, embed=embed)
        if initial_channel:
            self.channel = await self.initiator.guild.create_voice_channel(f"{self.game["title"]}")
            await self.initiator.move_to(self.channel)

        self.message = await interaction.original_response()

    async def update_message(self) -> None:
        """Keeping the message up to date"""
        embed = await self.create_embed()
        await self.message.edit(view=self, embed=embed)

    async def create_embed(self) -> discord.Embed:
        """Creating the embed with its properties"""
        game = self.load_game(self.game_value)
        self.game = game

        embed = discord.Embed(title="", description=f"Lets play {game["title"]}\nJoining will instantly move you into the created Voice-Channel!")

        for status in self.status_list:
            embed.add_field(inline=True, name=status, value=self.stringify_list(status))

        embed.add_field(inline=True, name=f"{self.count_players()}/{self.player_count} Players", value="")
        embed.add_field(inline=True, name="", value="")
        embed.add_field(inline=True, name=f"Mode: {self.mode_value}", value="")

        embed.set_image(url=game["img1600x900"])

        embed.set_footer(icon_url=self.initiator.avatar.url, text=f"Called by {self.initiator.display_name}")

        return embed

    def stringify_list(self, key: str) -> str:
        string = ""
        for player in self.player_list:
            if player[1] == key:
                string += "\n" + f"<@{player[0].id}>"
        if string != "":
            return string
        return "-"

    def count_players(self) -> int:
        counter = 0
        for player in  self.player_list:
            if player[1] == "Joined":
                counter += 1
        return counter

    @staticmethod
    def load_game(game_choice) -> dict:
        with open(f"{LOCAL_PATH}/games.json") as file:
            data = json.load(file)
        return data[game_choice]

    @discord.ui.button(label="Join", style=discord.ButtonStyle.green)
    async def join_button(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button
    ) -> None:
        """The join button"""
        await interaction.response.defer()
        await self.check_player(interaction, "Joined")
        if interaction.user.voice:
            await interaction.user.move_to(self.channel)

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline_button(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button
    ) -> None:
        """The decline button"""
        await interaction.response.defer()
        await self.check_player(interaction, "Declined")
        if interaction.user.voice:
            await interaction.user.move_to(self.channel)

    @discord.ui.button(label="Not sure", style=discord.ButtonStyle.gray)
    async def not_sure_button(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button
    ) -> None:
        """The Not sure button"""
        await interaction.response.defer()
        await self.check_player(interaction, "Not sure")
        if interaction.user.voice:
            await interaction.user.move_to(self.channel)

    async def check_player(
            self,
            interaction: discord.Interaction,
            key: str
    ) -> None:
        """Checking how the player interacted with the buttons"""
        for player in self.player_list:
            if player[0] == interaction.user:
                if player[1] != key:
                    self.player_list.append((player[0], key))
                    self.player_list.remove(player)
        if (interaction.user, key) not in self.player_list:
            self.player_list.append((interaction.user, key))
        await self.update_message()


async def initialize(
        interaction: discord.Interaction,
        game: app_commands.Choice[str],
        mode: app_commands.Choice[str],
        player_count: int
) -> None:
    """Initialization of the lets play command"""
    view = await set_view_options(interaction.user, game.value, mode.value, player_count)
    await view.send_message(interaction)

async def set_view_options(
        initiator: discord.Member,
        game_value: str,
        mode_value: str,
        player_count: int
) -> LetsPlayView:
    """Setting all properties for the view"""
    view = LetsPlayView(timeout=None)
    view.initiator = initiator
    view.game_value = game_value
    view.mode_value = mode_value
    view.player_count = player_count
    return view