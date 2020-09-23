import discord
from discord.ext import commands

class Management(commands.Cog):
    def __init__(self, client):
        self.client = client

    # output when a member object joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(752667164397273140).send(f'Welcome {member.mention}! <:yas_homer:751941589840036001> \n'
        'Please head over to the <#751860846904344627> channel to choose your role.')

    # output when a member object leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        mention_user = member.mention
        await self.client.get_channel(752667164397273140).send(f"{mention_user} has left the server. <:sweatie:751942394731298816> ")

    # command to clear the messages from a channel(chat room)
    @commands.command()
    # restrict the command to a specific role 
    @commands.has_role("Admin")
    async def purger(self, ctx, amount=5):
        if amount > 0:
            await ctx.channel.purge(limit = amount + 1) 
        else:
            await ctx.send("Am I joke to you? <:really:751937603653075005> ")

    # command to kick an user
    @commands.command()
    # restrict the command to specific role
    @commands.has_role("Admin")
    async def kick(self, ctx, member : discord.Member, *, why = None):
        await member.kick(reason = why)
    
    # command to ban an user
    @commands.command()
    # restrict the command to specific role
    @commands.has_role("Admin")
    async def ban(self, ctx, member : discord.Member, *, why = None):
        await member.ban(reason = why)
        await self.client.get_channel(752667164397273140).send(f"{member.mention} has been banned.")

    # command to unban an user
    @commands.command()
    @commands.has_role("Admin")
    async def unban(self, ctx, *, member):
        member_name, member_discriminator = member.split('#')
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await self.client.get_channel(752667164397273140).send(f"{user.mention} has been unbanned.")

    # assign role to member based on reactions emojis
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        unroled_member = payload.member
        server = self.client.get_guild(payload.guild_id)
        comp_role = discord.utils.get(server.roles, name = "Computing")
        gam_role = discord.utils.get(server.roles, name = "Gaming")
        net_role = discord.utils.get(server.roles, name = "Networking")
        sec_role = discord.utils.get(server.roles, name = "Security")
        se_role = discord.utils.get(server.roles, name = "SoftwareEng")
        if str(payload.channel_id) == "751860846904344627" and str(payload.message_id) == "753329568370393239": 
            if payload.emoji.id == 753325638567329863:
                await unroled_member.add_roles(comp_role)
            elif payload.emoji.id == 753329320336031747:
                await unroled_member.add_roles(gam_role)
            elif payload.emoji.id == 753328497375707267:
                await unroled_member.add_roles(net_role)
            elif payload.emoji.id == 753325391283880007:
                await unroled_member.add_roles(sec_role)
            elif payload.emoji.id == 753325497664143490:
                await unroled_member.add_roles(se_role)
            else:
                return


def setup(client):
    client.add_cog(Management(client))