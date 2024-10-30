"""Copyright (c) Void 2024 - Discord Bot Codebase

Embed class to send a certain Embed. 'Work in Progress'

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

import discord.ui


class BotEmbedView(discord.ui.View):

    initiator: discord.Member = None

    async def send_message(self, interaction: discord.Interaction):
        embed = await self.create_embed()
        await interaction.response.send_message(view=self, embed=embed)

    async def edit_message(self):
        ...

    async def create_embed(self):
        """Creating the embed with its properties"""

        embed = discord.Embed(title="", description=f"")

        embed.add_field(inline=True, name="status", value="")

        embed.set_image(url="")

        embed.set_footer(icon_url=self.initiator.avatar.url, text=f"Called by {self.initiator.display_name}")

        return embed