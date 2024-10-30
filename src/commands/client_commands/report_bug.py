"""Copyright (c) Void 2024 - Discord Bot Codebase

This module is for the help command to ensure it outputs
an interface like interaction experience for the user.
It is using a discord UI embed to ensure the user can
see the correct commands they wanted to see.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""
from asyncio import timeout

import discord
from discord import app_commands


class ReportBugView(discord.ui.View):

    group: str = ""
    description: str = ""

    async def send_message(self, interaction: discord.Interaction, owner_id: int):
        dm_channel = await interaction.client.create_dm(interaction.client.get_user(owner_id))
        embed = await self.create_embed(interaction)
        await dm_channel.send(view=self, embed=embed, delete_after=30)

    async def create_embed(self, interaction: discord.Interaction):
        embed = discord.Embed(title="", description=f"# Bug Report\n### From {interaction.user.display_name}\n\n")

        embed.set_thumbnail(url=interaction.user.avatar.url)

        embed.add_field(name=self.group, value=self.description)

        return embed

async def initialize(
        interaction: discord.Interaction,
        group: app_commands.Choice[str],
        description: str
) -> None:
    view = await set_view_options(group, description)
    await view.send_message(interaction, 1234567890) # change this to the id you want to send it to
    await interaction.response.send_message("Thank you for reporting a bug to us!", ephemeral=True)

async def set_view_options(group: app_commands.Choice[str], description: str):
    view = ReportBugView(timeout=None)
    view.group = group.value
    view.description = description
    return view