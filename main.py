import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # only used for local dev

TOKEN = os.getenv("tok")
MOD_IDS = os.getenv("MOD_IDS", "").split(",")  # Comma-separated user IDs

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="commands")
async def list_commands(ctx):
    command_list = [command.name for command in bot.commands]
    await ctx.send(f"Available commands:\n" + "\n".join(f"!{c}" for c in command_list))

@bot.command(name="announce")
async def announce(ctx, channel_id: int, *, message: str):
    if str(ctx.author.id) not in MOD_IDS:
        await ctx.send("🚫 You don't have permission to use this command.")
        return

    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"📢 **Announcement:** {message}")
        await ctx.send("✅ Announcement sent.")
    else:
        await ctx.send("❌ Invalid channel ID.")

bot.run(TOKEN)