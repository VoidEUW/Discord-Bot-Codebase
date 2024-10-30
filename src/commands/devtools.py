"""Copyright (c) Void 2024 - Discord Bot Codebase

Here there are all necessary devtools the bot needs in order to
be maintained on runtime. These features are restricted to Developers
of this bot! There is no way of using them as a normal user.

Author: Void (Lukas Kreuz)

Since: v1.0.0
"""

from discord import app_commands
import discord.ext


class DevtoolsCommandGroup(app_commands.Group):
    """Command Group

    Inherits from app_commands.Group. The decorators list the commands given as
    class methods. Calling the necessary command module after recognitions.
    """

    @app_commands.command(name="delete_personal_message", description="DESCRIPTION")
    @app_commands.describe(message_id="DESCRIPTION")
    async def command_delete_personal_message(
            self,
            interaction: discord.Interaction,
            message_id: str
    ):
        """Deleting a message based on the id in the channel you call it"""
        channel = await interaction.client.fetch_channel(1298730577536487486)
        message = await channel.fetch_message(int(message_id))
        await message.delete()
        await interaction.response.send_message("MESSAGE_DELETED", ephemeral=True, delete_after=10)

    @app_commands.command(name="join_channel", description="DESCRIPTION")
    async def command_join_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await channel.connect(reconnect=True, self_mute=True, self_deaf=True)
        await interaction.response.send_message("Joined successfully")


async def setup(bot: discord.ext.commands.Bot):
    bot.tree.add_command(DevtoolsCommandGroup(name="devtools", description="DESCRIPTION"))