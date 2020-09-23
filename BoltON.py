from os import listdir, name, path

import discord
from discord.ext import commands  # commands extension

# create instance of a bot(client) and set command prefix
client = commands.Bot(command_prefix = ".", description = "In-House Management Bot")

# remove the default help command
client.remove_command("help")

# event that outputs when the bot is online
@client.event
async def on_ready():
   await client.change_presence(status = discord.Status.dnd, activity = discord.Game(name = "Being conscientious.."))
   print("BoltON bot is ON.")

@client.event
# Ignore DMs
async def on_message(message):
   if not message.guild:
      return
   # Ignore other bots
   if message.author.bot:
      return
   await client.process_commands(message)
 
# load an extension(cog)
@client.command()
@commands.has_role("Admin")
async def load(ctx, extension):
   client.load_extension(f"cogs.{extension}")

# unload an extension(cog)
@client.command()
@commands.has_role("Admin")
async def unload(ctx, extension):
   client.unload_extension(f"cogs.{extension}")

# reload an extension(cog) - equivalent to unload and load again
@client.command()
@commands.has_role("Admin")
async def reload(ctx, extension):
   client.reload_extension(f"cogs.{extension}")

# load all extensions/cogs on startup
for file in listdir(path.join(path.dirname(__file__), 'cogs/')):
   filename, ext = path.splitext(file)
   if '.py' in ext:
      try:
         client.load_extension(f"cogs.{filename}")
      except Exception as e:
         print(f"Failed to load extension {e}")

@client.command()
async def helpme(ctx):
   emb = discord.Embed(
      colour = discord.Colour.orange(),
      title = "Bot Commands",
      description = "These commands can be run by users using the bot prefix."
   )
   emb.set_author(name = "Bot prefix = .", icon_url = client.user.avatar_url)
   emb.add_field(name = "*ping*", value = "• Check if the bot is responsive, displays latency in miliseconds.", inline = False)
   emb.add_field(name = "*userinfo / ui / memberinfo / mi*  <member name>", value = "• Displays information about a member of the server. ", inline = False)
   emb.add_field(name = "*serverinfo / server / si *", value = "• Display information about the server.", inline = False)
   emb.add_field(name = "*meme*", value = "• Fetch a meme from ProgrammerHumor subreddit.")
   emb.add_field(name = "*helpmanage*", value = "• Show management commands for Admins.", inline = False)
   emb.set_thumbnail(url = "https://www.bolton.ac.uk/assets/Uploads/UoB-Logo2.jpg" )
   await ctx.send(embed = emb)

@client.command()
async def helpmanage(ctx):
   emb = discord.Embed(
      colour = discord.Colour.orange(),
      title = "Bot Commands for Admins",
      description = "These commands can only be run by users with an Admin role."
   )
   emb.set_author(name = "Bot prefix = .", icon_url = client.user.avatar_url)
   emb.add_field(name = "*load*  <filename>", value = "• Load an extension/cog. Takes the file name without extension as an argument.", inline=False)
   emb.add_field(name = "*unload*  <filename>", value = "• Unload an extension/cog. Takes the file name without extension as an argument.", inline=False)
   emb.add_field(name = "*reload*  <filename>", value = "• Reload a cog that has been updated/modified. Takes the file name without extension as an argument. ", inline=False)
   emb.add_field(name = "*purger*  <number of messages>", value = "• Deletes messages; takes an int as argument; default is 5.", inline=False)
   emb.add_field(name = "*kick*  <@member>", value = "• Kick a member. Takes the member name as argument.", inline=False)
   emb.add_field(name = "*ban*  <@member>", value = "• Ban a member. Takes the member name as argument.", inline=False)
   emb.add_field(name = "*unban*  <username>", value = "• Unban an user. Takes the username as argument i.e user#1234", inline=False)
   emb.set_thumbnail(url = "https://www.bolton.ac.uk/assets/Uploads/UoB-Logo2.jpg" )
   await ctx.send(embed=emb)


# common error handler
@client.event
async def on_command_error(ctx, error):
   if isinstance(error, commands.errors.CommandNotFound):
      return await ctx.send(':exclamation:  Invalid command  :exclamation:\n ' 
      'Type .helpme to see a list of User Commands.')
   if isinstance(error, commands.errors.MissingRole):
      return await ctx.send("You must be Admin to run this command <:none_of_my_business:751932765146185739> .")
   raise error

# run the bot
client.run('your own bot token here')


