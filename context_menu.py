# -*- coding: utf-8 -*-
import disnake
from disnake.ext import commands

from modals import AddTagModal


class ContextMenuCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Add as Tag")
    async def add_as_tag(self, inter: disnake.MessageCommandInteraction):
        """
        A context menu command that opens a modal for adding a tag based on the
        selected message.
        """
        selected_message_content = inter.target.content
        original_author = inter.target.author
        original_link = inter.target.jump_url
        original_date = inter.target.created_at.strftime("%Y-%m-%d %H:%M:%S")

        selected_message_content = (
            f"Original author: {original_author}\n"
            f"Original date: {original_date} [jump]({original_link}) \n\n"
            f"{selected_message_content}"
        )

        modal = AddTagModal(
            server_id=inter.guild_id, prefill_message=selected_message_content
        )
        await inter.response.send_modal(modal)
