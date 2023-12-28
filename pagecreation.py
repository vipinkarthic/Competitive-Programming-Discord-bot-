import requests
import json
import settings
import discord
from discord.ext import commands
import json
import discord.ext.commands

class PaginationView(discord.ui.View):
    current_page : int = 1
    sep : int = 5

    async def send(self, ctx):
        self.message = await ctx.send(view=self)
        await self.update_message(self.data[:self.sep])

    def create_embed(self, data):
        embed = discord.Embed(title=f"Problems List : {self.current_page} / {int(len(self.data) / self.sep)}")
        for i in data:
            embed.add_field(name = f'**{i[0]}** : {i[1]}', value = f'{i[2]}', inline = False)
        return embed

    async def update_message(self,data):
        self.update_buttons()
        await self.message.edit(embed=self.create_embed(data), view=self)

    def update_buttons(self):
        if self.current_page == 1:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == int(len(self.data) / self.sep):
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary

    @discord.ui.button(label="|<",
                       style=discord.ButtonStyle.green)
    async def first_page_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page = 1
        ut = self.current_page * self.sep
        ft = ut - self.sep
        await self.update_message(self.data[ft:ut])
        
    @discord.ui.button(label="<",
                       style=discord.ButtonStyle.primary)
    async def prev_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page -= 1
        ut = self.current_page * self.sep
        ft = ut - self.sep
        await self.update_message(self.data[ft:ut])
        
    @discord.ui.button(label=">",
                       style=discord.ButtonStyle.primary)
    async def next_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page += 1
        ut = self.current_page * self.sep
        ft = ut - self.sep
        await self.update_message(self.data[ft:ut])
        
    @discord.ui.button(label=">|",
                       style=discord.ButtonStyle.green)
    async def last_page_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page = int(len(self.data) / self.sep)
        ut = self.current_page * self.sep
        ft = ut - self.sep
        await self.update_message(self.data[ft:ut])