import discord
import os
from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_server():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run_server, daemon=True).start()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online!")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game("24/7 Online 🟢")
    )

bot.run(os.environ["BOT_TOKEN"])
