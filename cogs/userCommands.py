import discord
from datetime import datetime
from typing import Optional 
from discord.ext import commands
from discord import Member, User

class userCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # command to check the latency of the bot in miliseconds; ctx = context
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"I'm on! <:what:751940813222576239> My latency is {round(self.client.latency * 1000)} ms.")

    # command to display member info
    @commands.command(
        name = "userinfo",
        aliases = ["ui", "memberinfo", "mi"]
    )
    async def userinfo(self, ctx, target: Optional[Member]):
        target = target or ctx.author
        emb = discord.Embed(
            title = "Member information",
            colour = target.colour,
        )
        emb.set_thumbnail(url = "https://www.bolton.ac.uk/assets/Uploads/UoB-Logo2.jpg" )
        emb.add_field(name = "• **ID**", value = target.id, inline = False)
        emb.add_field(name = "• **Name**", value = target, inline = False)
        emb.add_field(name = "• **Nickname**", value = target.nick, inline = False)
        emb.add_field(name = "• **Bot?**", value = target.bot, inline = True)
        emb.add_field(name = "• **Top Role**", value = f"{target.top_role.mention}", inline = True)
        emb.add_field(name = "• **Status**", value = str(target.status), inline = True)
        emb.add_field(name = "• **Created on**", value = str(target.created_at.strftime("%d/%m/%Y  %H:%M:%S")), inline = True)
        emb.add_field(name = "• **Joined at**", value = str(target.joined_at.strftime("%d/%m/%Y  %H:%M:%S")), inline=True)
        emb.set_image(url = target.avatar_url)
        emb.set_footer(text = f"Requested by {ctx.author} at {datetime.utcnow()}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = emb)


    # command to display server info
    @commands.command(
        name = "serverinfo",
        aliases=["server", "si"]
    )
    async def serverinfo(self, ctx):
        em = discord.Embed(
        title = "**Server Information**",
        colour = discord.Colour.orange()
    )
        em.set_thumbnail(url = "https://www.bolton.ac.uk/assets/Uploads/UoB-Logo2.jpg")
        em.set_footer(text = f"Requested by {ctx.author} at {datetime.utcnow()}", icon_url = ctx.author.avatar_url)
        
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))), 
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
        fields = [("• **Owner**", ctx.guild.owner, False),
				  ("• **Created at**", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
				  ("• **Members**", len(ctx.guild.members), True),
				  ("• **Humans**", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
				  ("• **Bots**", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
				  ("• **Statuses**", f"🟢  {statuses[0]}  🟠  {statuses[1]}  🔴  {statuses[2]}  ⚪  {statuses[3]}", False),
				  ("• **Text Channels**", len(ctx.guild.text_channels), True),
				  ("• **Voice Channels**", len(ctx.guild.voice_channels), True),
				  ("• **Roles**", len(ctx.guild.roles), True),
				  ("• **Invites**", len(await ctx.guild.invites()), True)]
        for name, value, inline in fields:
            em.add_field(name = name, value = value, inline = inline)
        await ctx.send(embed = em)


def setup(client):
    client.add_cog(userCommands(client))
