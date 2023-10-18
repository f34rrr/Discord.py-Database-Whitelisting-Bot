'''

Database Whitelisting Bot
skid off this if you want lmao

'''


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive


uri = os.environ["mongo"] # make a secret named mongo
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["WLed"]
col = db["whitelist"]
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def whitelist(ctx, username):
  db = client["WLed"]
  col = db["whitelist"]
  if col.find_one({"username": username, "wl": "yes"}):
    await ctx.send("This user is already whitelisted.")
  else:
    col.insert_one({"username": username, "wl": "yes"})
    await ctx.send("Whitelisted " + username)

@bot.command()
async def check(ctx, username):
  db = client["WLed"]
  col = db["whitelist"]
  if col.find_one({"username": username, "wl": "yes"}):
    await ctx.send("User is whitelisted.")
  else:
    await ctx.send("User is not whitelisted.")

@bot.command()
async def blacklist(ctx, username):
  db = client["WLed"]
  col = db["whitelist"]
  if col.find_one({"username": username, "wl": "yes"}):
    col.update_one({"username": username, "wl": "yes"}, {"$set": {"wl": "no"}})
    await ctx.send("Blacklisted "+ username)
  else:
    await ctx.send("No one named that")



keep_alive()
bot.run(os.environ["token"]) # run the funny bot xdee!!s sadasidoj