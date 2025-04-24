# this bot uses pycord. 
# > Bot by sgtflixy, this bot is a basic version of my bot:
# >> https://bot.infiltra.xyz
import discord
from discord.ext import commands
import random
import os
import time

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
@bot.slash_command(
    description="Get ping of the server",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
async def ping(ctx):
    em = discord.Embed(description=f"**pong! (`{ctx.bot.latency * 1000:.2f}` ms)**")
    await ctx.respond(embed=em)
@bot.slash_command(
    description="Kick a user from the server",
    default_member_permissions=discord.Permissions(kick_members=True),
)
async def kick(ctx, member: discord.Member, reason: str = "No reason provided"):
    if not ctx.author.guild_permissions.kick_members:
        return await ctx.respond("❌ You don't have permission to kick members.", ephemeral=True)

    try:
        await member.kick(reason=reason)
        await ctx.respond(f"👢 {member} has been kicked. Reason: {reason}")
    except Exception as e:
        await ctx.respond(f"❌ Failed to kick member: {e}", ephemeral=True)
@bot.slash_command(
    description="Ban a user from the server",
    default_member_permissions=discord.Permissions(ban_members=True),
)
async def ban(ctx, member: discord.Member, reason: str = "No reason provided"):
    if not ctx.author.guild_permissions.ban_members:
        return await ctx.respond("❌ You don't have permission to ban members.", ephemeral=True)

    try:
        await member.ban(reason=reason)
        await ctx.respond(f"🔨 {member} has been banned. Reason: {reason}")
    except Exception as e:
        await ctx.respond(f"❌ Failed to ban member: {e}", ephemeral=True)
@bot.slash_command(
    description="Clear a number of messages",
    default_member_permissions=discord.Permissions(manage_messages=True),
)
async def clear(ctx, amount: int = 5):
    if not ctx.author.guild_permissions.manage_messages:
        return await ctx.respond("❌ You don't have permission to manage messages.", ephemeral=True)

    await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message
    await ctx.respond(f"🧹 Cleared {amount} messages.", ephemeral=True)
@bot.slash_command(
    description="Flip a coin",
)
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.respond(f"🪙 You flipped **{result}**!")
@bot.slash_command(
    description="Roll a dice (1-6)",
)
async def roll(ctx):
    result = random.randint(1, 6)
    await ctx.respond(f"🎲 You rolled a **{result}**!")
@bot.slash_command(
    description="Say something as the bot",
)
async def say(ctx, message: str):
    await ctx.respond(message)


bot.run("BOT_TOKEN") # you should def put this in an env if using anything other than your own pc.
