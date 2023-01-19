import discord
from discord import app_commands

class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        
    async def on_ready(self):
        if not self.synced:
            print("Sycning commands")
            await tree.sync(guild=discord.Object(id = 1065734665333375027))
            self.synced = True
        print(f"I am {self.user}.")

client = bot_client()
tree = app_commands.CommandTree(client)

@tree.command(name = "test", description = "Run a simple test command", guild = discord.Object(id = 1065734665333375027))
async def self(interaction: discord.Interaction, channel: discord.VoiceChannel):
    await interaction.response.send_message(f"<#{channel.id}>", ephemeral=False)
    await interaction.edit_original_response(content=f"Invalid Cron Expression")
    print(f'Current channel: {channel.name}')
    
@tree.command(name = "remindme", description = "Reminds the user of something, after a set amount of time", guild = discord.Object(id = 1065734665333375027))
async def self(interaction: discord.Interaction, time: str):
    await interaction.response.send_message(f"I will remind you in {time}", ephemeral=False)

token = open('token.txt', 'r').read()
client.run(token)