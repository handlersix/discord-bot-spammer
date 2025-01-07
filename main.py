import discord
from discord.ext import commands
import asyncio
import requests


with open("token.txt", "r") as f:
    token = f.read()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

#put ur wl ids here
wl = [489358930454395347594375935473957543, 348583458348534854843843]

@bot.tree.command(name="spam", description="yo")
async def spam(interaction: discord.Interaction, message: str, count: int):
    if interaction.user.id not in wl:
        await interaction.response.send_message(
            "nope",
            ephemeral=True
        )
        return


    if count < 1 or count > 50:
        await interaction.response.send_message(
            "thats tooooooo much",
            ephemeral=True
        )
        return

    await interaction.response.send_message(f".")
    
    lsmg = await interaction.original_response()
    for i in range(min(count, 5)): 
        try:
            await asyncio.sleep(0)
            lsmg = await interaction.followup.send(f"{message}")
        except Exception as e:
            print(f"{e}")
            break

    if count > 5:
        await interaction.followup.send(
            f"reuse",
            ephemeral=True
        )


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(f"cmds didint sync {e}")

bot.run(token)
print(f"loggggged in as {bot.user}")
