import discord
from discord.ext import commands # commands extension

# create instance of a bot(client) and set command prefix
client = commands.Bot(command_prefix = ".")

# event that outputs when the bot is online
@client.event
async def on_ready():
    print("BoltON bot is ON.")

# output when a member object joins the server
@client.event
async def on_member_join(member):
   print(f'{member} has joined the server. :yas_homer:')

# output when a member object leaves the server
@client.event
async def on_member_remove(member):
   print(f'{member} has left the server. :wee:')

# command to check the latency of the bot in miliseconds; ctx = context
@client.command()
async def ping(ctx):
   await ctx.send(f'I"m on! :hehe: {round(client.latency * 1000)}')

# command to clear the messages from a channel(chat room)
@client.command()
async def purger(ctx, amount=5):
   if amount > 0:
      await ctx.channel.purge(limit=amount)
   else:
      await ctx.send("Am I joke to you? :really: ")

# run the bot
client.run('NzUxOTIwNjUwOTIyMjI5ODU0.X1QGrQ.3REOq_LiRoA4gMGJiH3IYCG4_I0')


