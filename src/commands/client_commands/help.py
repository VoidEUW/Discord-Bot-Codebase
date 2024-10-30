"""Copyright (c) Void 2024 - Discord Bot Codebase

This module is for the help command to ensure it outputs
an interface like interaction experience for the user.
It is using a discord UI embed to ensure the user can
see the correct commands they wanted to see.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import discord
from discord import app_commands


class HelpView(discord.ui.View):
    """Help View of the Command

    In this Class we declare all methods necessary to page
    through the commands like a manual book
    """
    initiator: discord.User = None
    message: discord.Message = None
    current_page: str = ""

    async def send_message(self, interaction: discord.Interaction):
        """Sending the message"""
        embed = await self.create_embed()

        await interaction.response.send_message(view=self, embed=embed)

        self.message = await interaction.original_response()

    async def update_message(self) -> None:
        """Keeping the message up to date"""
        embed = await self.create_embed()
        await self.message.edit(view=self, embed=embed)

    async def create_embed(self) -> discord.Embed:
        """Creating the embed with its properties"""
        embed = discord.Embed(title="", description="")

        embed.add_field(inline=True, name="", value="")
        embed.add_field(inline=True, name="", value="")
        embed.add_field(inline=True, name="", value="")

        embed.set_image(url="https://cdn.discordapp.com/attachments/1297997051690352700/1297997098599579698/Help_Banner.png?ex=6717f57f&is=6716a3ff&hm=8290d2af1eb347c9d4da3cd9f5fe6f3037a4d881a223044f9fed0771070c50ae&")

        embed.set_footer(icon_url=self.initiator.avatar.url, text=f"Called by {self.initiator.display_name}")

        return embed

    @discord.ui.button(label="", style=discord.ButtonStyle.gray)
    async def not_sure_button(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button
    ) -> None:
        """The Not sure button"""
        await interaction.response.defer()
        # TODO some code

    @discord.ui.button(label="", style=discord.ButtonStyle.gray)
    async def not_sure_button(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button
    ) -> None:
        """The Not sure button"""
        await interaction.response.defer()
        # TODO some code


async def initialize(
        interaction: discord.Interaction
) -> None:
    """Initialization of the lets play command"""
    view = await set_view_options(interaction.user, current_page="home")
    await view.send_message(interaction)

async def set_view_options(
        initiator: discord.Member,
        current_page: str
) -> HelpView:
    """Setting all properties for the view"""
    view = HelpView(timeout=None)
    view.initiator = initiator
    return view