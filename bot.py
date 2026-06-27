import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True          
intents.message_content = True  

bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in successfully as: {bot.user.name} (ID: {bot.user.id})")
    print("---------------------------------------------------------------")

@bot.command(name="obc")
@commands.has_permissions(administrator=True)
async def official_broadcast(ctx, *, message: str):
    """Loops through server members and sends the broadcast message."""
    await ctx.send("Initiating broadcast sequence to all server members...")
    
    success_count = 0
    fail_count = 0

    for member in ctx.guild.members:
        
        if member.bot:
            continue

        try:
            await member.send(message)
            success_count += 1
            print(f"[SUCCESS] Sent DM to {member.name}")
        except discord.Forbidden:
            fail_count += 1
            print(f"[FAILED] Cannot DM {member.name} (DMs closed or blocked)")
        except discord.HTTPException as e:
            fail_count += 1
            print(f"[ERROR] API rate limit or error for {member.name}: {e}")

        
        await asyncio.sleep(3)

    await ctx.send(f"Broadcast concluded. Successfully sent: {success_count} | Failed: {fail_count}")

@official_broadcast.error
async def obc_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Error: You must have Administrator privileges to use this command.")


SECRET_TOKEN = "PASTE_HER_YOUR_TOKEN"

bot.run(SECRET_TOKEN)
