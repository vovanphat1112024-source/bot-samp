import discord
import random
import json
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATA_FILE = "data.json"

# LOAD DATA
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        user_data = json.load(f)
else:
    user_data = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(user_data, f)

def generate_id():
    used = set(user_data.values())
    while True:
        num = str(random.randint(1000, 99999))
        if num not in used:
            return num

@bot.event
async def on_member_join(member):
    uid = str(member.id)

    if uid in user_data:
        number = user_data[uid]
    else:
        number = generate_id()
        user_data[uid] = number
        save_data()

    new_name = f"[{number}] {member.name}"
    await member.edit(nick=new_name)

bot.run(os.getenv("MTQ5ODM5MTU0NDIyMTQwMTE4MA.GIZ8f-.ZiQQnl7ZORea_EQ2yH_obr68u4LUMWoFTZdtC0"))