import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DEFAULT_ROLE_ID = 1443250658412335229

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Event: New member joins
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(DEFAULT_ROLE_ID)
    if role is None:
        print(f"Role with ID {DEFAULT_ROLE_ID} not found.")
        return
    
    try:
        await member.add_roles(role)
        print(f"Assigned role {role.name} to {member.name}.")
    except Exception as e:
        print(f"Failed to assign role: {e}")


# Simple command to test bot responsiveness
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable not set.")
    bot.run(TOKEN)

