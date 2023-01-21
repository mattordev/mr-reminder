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

#commands
@tree.command(name = "areyouup", description = "Run a simple command to see if the bot is up and running", guild = discord.Object(id = 1065734665333375027))
async def areyouup(interaction: discord.Interaction):
    await interaction.response.send_message("Alive and waiting...", ephemeral = True)
    
@tree.command(name = "test", description = "Run a simple command to test the bot", guild = discord.Object(id = 1065734665333375027))
async def areyouup(interaction: discord.Interaction):
    channel = await interaction.user.create_dm()
    await channel.send("Here is a DM")
    await interaction.response.send_message("DM Sent!", ephemeral = True)
    
@tree.command(name = "reminder", description = "Reminds the user of something after a set amount of time", guild = discord.Object(id = 1065734665333375027))
async def reminder(interaction: discord.Interaction, reminder: str, time: float):
    if (time <= 0):
        await interaction.response.send_message("ERROR: Please enter a postive value.", ephemeral = True)
        return
    await interaction.response.send_message("Executing...", ephemeral = True)
    # Get the current timestamp 
    current_timestamp = datetime.utcnow().timestamp()

    # Create a datetime object from the timestamp
    current_time = datetime.utcfromtimestamp(current_timestamp)

    # Add the interval
    current_time += timedelta(hours=time)
    # Get the Unix timestamp
    unix_time = int(current_time.timestamp())
    
    await interaction.edit_original_response(content=f"Reminder setup, reminding you <t:{unix_time}:R>")
    timeInSeconds = time * 3600
    await asyncio.sleep(timeInSeconds)
    channel = await interaction.user.create_dm()
    await channel.send(f"This is your reminder: {reminder}")
    await interaction.edit_original_response(content="Reminder sent!")
    
@tree.command(name = "recurringreminder", description = "Reminds the user of something after a set amount of time, but recurs every interval", guild = discord.Object(id = 1065734665333375027))
async def recurringreminder(interaction: discord.Interaction, reminder: str, interval: float):
    await interaction.response.send_message("Executing...", ephemeral = True)
    # Get the current timestamp 
    current_timestamp = datetime.utcnow().timestamp()

    # Create a datetime object from the timestamp
    current_time = datetime.utcfromtimestamp(current_timestamp)

    # Add the interval
    current_time += timedelta(hours=interval)
    # Get the Unix timestamp
    unix_time = int(current_time.timestamp())
    
    await interaction.edit_original_response(content=f"Reminder setup, reminding you every {interval}h, the next reminder is <t:{unix_time}:R>")
    # Get the interval in seconds so we can use it for the asyncio sleep call.
    timeInSeconds = interval * 3600
    
    await asyncio.sleep(timeInSeconds)
    channel = await interaction.user.create_dm()
    await channel.send(f"This is your reminder: {reminder}")
    await interaction.edit_original_response(content=f"Reminder sent! Sending another one <t:{unix_time}:R>. Run /stopreminder to cancel.")

        
@tree.command(name = "stopreminder", description = "Reminds the user of something after a set amount of time, but recurs every interval", guild = discord.Object(id = 1065734665333375027))
async def stopreminder(interaction: discord.Interaction, remindername: str):
    await interaction.response.send_message(f"Cancelling your reminder called: {remindername}", ephemeral = True)

@tree.command(name = "listreminders", description = "Lists the currently active reminders", guild = discord.Object(id = 1065734665333375027))
async def listreminders(interaction: discord.Interaction):
    await interaction.response.send_message("Getting the list of active reminders...", ephemeral=True)
    await interaction.edit_original_response(content = f"Here are all of your reminders: <REMINDERS>")
        
        

token = open('token.txt', 'r').read()
client.run(token)