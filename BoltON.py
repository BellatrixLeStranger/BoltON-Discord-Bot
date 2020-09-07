import discord
from discord.ext import commands # commands extension

# create instance of a bot(client) and set desired command prefix
client = commands.Bot(command_prefix = ".")

# event that outputs when the bot is online
@client.event
async def on_ready():
    print("BoltON bot is ON.")

# output in a specific channel when a member object joins the server
@client.event
async def on_member_join(member):
   await client.get_channel(channel ID here).send(f'Welcome {member.mention}! \n'
   'Please head over to the <#channel ID here> channel to choose your role.')

# output in a specific channel when a member object leaves the server 
@client.event
async def on_member_remove(member):
   mention_user = member.mention
   await client.get_channel(channel ID here).send(f"{mention_user} has left the server. ")

# command to check the latency of the bot in miliseconds; ctx = context
@client.command()
async def ping(ctx):
   await ctx.send(f"I'm on! My latency is {round(client.latency * 1000)} ms.")

# command to clear the messages from a channel(chat room)
@client.command()
# restrict the command to a specific role  
@commands.has_role("role name here")
async def purger(ctx, amount = 5):
   if amount > 0:
      await ctx.channel.purge(limit = amount)
   else:
      await ctx.send("Am I joke to you?")
# outputs an error message when the command is run by a different role
@purger.error
async def purger_error(ctx, error):
   if isinstance(error, commands.MissingRole):
      await ctx.send("You must be <role name here> to run this command.")

# command to kick an user
@client.command()
# restrict the command to specific role
@commands.has_role("role name here")
async def kick(ctx, member : discord.Member, *, why = None):
   await member.kick(reason = why)
# outputs an error message when the command is run by a different role
@kick.error
async def kick_error(ctx, error):
   if isinstance(error, commands.MissingRole):
      await ctx.send("You must be <role name here> to run this command.")

# command to ban an user
@client.command()
# restrict the command to specific role
@commands.has_role("role name here")
async def ban(ctx, member : discord.Member, *, why = None):
   await member.ban(reason = why)
# outputs an error message when the command is run by a different role
@ban.error
async def ban_error(ctx, error):
   if isinstance(error, commands.MissingRole):
      await ctx.send("You must be <role name here> to run this command.")




# run the bot
client.run('your own bot token here')


