
import os
import discord
from discord import app_commands

TOKEN = os.environ["DISCORD_TOKEN"]

class MWEquipmentBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = MWEquipmentBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="ping", description="Check if MW Equipment History is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏓 MW Equipment History is online! Equipment database coming soon."
    )

bot.run(TOKEN)
