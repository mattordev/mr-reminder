import discord
from datetime import datetime, timedelta
import asyncio
from discord import app_commands

class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        
    async def on_ready(self):
        if not self.synced:
            print("Syncing commands")
            await tree.sync(guild=discord.Object(id = 1065734665333375027))
            self.synced = True
        print(f"I am {self.user}.")

client = bot_client()
tree = app_commands.CommandTree(client)

@tree.command(name = "areyouup", description = "Run a simple command to see if the bot is up and running", guild = discord.Object(id = 1065734665333375027))
async def areyouup(interaction: discord.Interaction):
    await interaction.response.send_message("Alive and waiting...", ephemeral = True)
    
@tree.command(name = "test", description = "Run a simple command to test the bot", guild = discord.Object(id = 1065734665333375027))
async def areyouup(interaction: discord.Interaction):
    channel = await interaction.user.create_dm()
    await channel.send("Here is a DM")
    await interaction.response.send_message("DM Sent!", ephemeral = True)
    
@tree.command(name = "reminder", description = "Reminds the user of something after a set amount of time", guild = discord.Object(id = 1065734665333375027))
async def reminder(interaction: discord.Interaction, interval: float):
    await interaction.response.send_message("Executing...", ephemeral = True)
    # Get the current timestamp 
    current_timestamp = datetime.utcnow().timestamp()

    # Create a datetime object from the timestamp
    current_time = datetime.utcfromtimestamp(current_timestamp)

    # Add the interval
    current_time += timedelta(hours=interval)
    # Get the Unix timestamp
    unix_time = int(current_time.timestamp())
    
    await interaction.edit_original_response(content=f"Reminder setup, reminding <t:{unix_time}:R>")
    timeInSeconds = interval * 3600
    await asyncio.sleep(timeInSeconds)
    channel = await interaction.user.create_dm()
    await channel.send("REMINDER")
    await interaction.edit_original_response(content="DM Sent!")
    
@tree.command(name = "recurringreminder", description = "Reminds the user of something after a set amount of time, but recurs every interval", guild = discord.Object(id = 1065734665333375027))
async def recurringreminder(interaction: discord.Interaction, interval: float):
    await interaction.response.send_message("Executing...", ephemeral = True)
    # Get the current timestamp 
    current_timestamp = datetime.utcnow().timestamp()

    # Create a datetime object from the timestamp
    current_time = datetime.utcfromtimestamp(current_timestamp)

    # Add the interval
    current_time += timedelta(hours=interval)
    # Get the Unix timestamp
    unix_time = int(current_time.timestamp())
    
    await interaction.edit_original_response(content=f"Reminder setup, reminding you every {interval}, the next reminder is <t:{unix_time}:R>")
    timeInSeconds = interval * 3600
    await asyncio.sleep(timeInSeconds)
    channel = await interaction.user.create_dm()
    await channel.send("REMINDER")
    await interaction.edit_original_response(content="DM Sent!")
        

token = open('token.txt', 'r').read()
client.run(token)