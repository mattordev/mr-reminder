import discord
from datetime import datetime, timedelta
from asyncio import sleep
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
async def test(interaction: discord.Interaction):
    await reminder(interaction, 5, False)
    
@tree.command(name = "reminder", description = "Reminds the user of something, after a set amount of time", guild = discord.Object(id = 1065734665333375027))
async def reminder(interaction: discord.Interaction, interval: int, recurring: bool):
    await interaction.response.send_message("Executing...", ephemeral = True)
    # Get the current timestamp 
    current_timestamp = datetime.utcnow().timestamp()

    # Create a datetime object from the timestamp
    current_time = datetime.utcfromtimestamp(current_timestamp)

    current_time += timedelta(hours=interval)

    # Get the Unix timestamp
    unix_time = int(current_time.timestamp())
    
    if(recurring == False):
        await interaction.edit_original_response(content=f"Reminder setup, reminding <t:{unix_time}:R>")
    else:
        await interaction.edit_original_response(content=f"Reminder setup, reminding you every {interval}, the next reminder is <t:{unix_time}:R>")
    


token = open('token.txt', 'r').read()
client.run(token)