import discord
from discord.ext import commands

class Subcommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.group()
    async def timetable(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please select a course to see timetable for: comp / se / net :grin: ")
    
    @timetable.group(aliases=["C", "c", "Comp"])
    async def comp(self, ctx):
        if ctx.invoked_subcommand is None:
            full_comp = discord.File("file path here", filename = "Computing_Full_Timetable.png")
            emb = discord.Embed(colour = discord.Colour.orange(), title = "Computing Full Timetable")
            emb.set_image(url = "attachment://Computing_Full_Timetable.png")
            await ctx.send(file = full_comp, embed = emb )
    
    @comp.command(aliases = ["tuesday", "tu", "Tu", "tue"])
    async def tue_comp(self,ctx):
        tue_comp = discord.File("file path here", filename = "Computing_Tuesday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Computing Tuesday Timetable")
        emb.set_image(url = "attachment://Computing_Tuesday_Timetable.png")
        await ctx.send(file = tue_comp, embed = emb )
    
    @comp.command(aliases = ["thursday", "Th", "th", "thu"])
    async def thu_comp(self,ctx):
        thu_comp = discord.File("file path here", filename = "Computing_Thursday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Computing Thursday Timetable")
        emb.set_image(url = "attachment://Computing_Thursday_Timetable.png")
        await ctx.send(file = thu_comp, embed = emb )

    @timetable.group(aliases = ["Soft", "soft", "Se", "SE"])
    async def se(self, ctx):
        if ctx.invoked_subcommand is None:
            full_se = discord.File("file path here", filename = "Software_Engineering_Full_Timetable.png")
            emb = discord.Embed(colour = discord.Colour.orange(), title = "Software Engineering Full Timetable")
            emb.set_image(url = "attachment://Software_Engineering_Full_Timetable.png")
            await ctx.send(file = full_se, embed = emb ) 

    @se.command(aliases=["tuesday", "tu", "Tu", "tue"])
    async def tue_se(self, ctx):
        tue_se = discord.File("file path here", filename = "Software_Engineering_Tuesday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Software Engineering Tuesday Timetable")
        emb.set_image(url = "attachment://Software_Engineering_Tuesday_Timetable.png")
        await ctx.send(file = tue_se, embed = emb )
    
    @se.command(aliases =["thursday", "Th", "th", "thu"])
    async def thu_se(self,ctx):
        thu_se = discord.File("file path here", filename = "Software_Engineering_Thursday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Software Engineering Thursday Timetable")
        emb.set_image(url = "attachment://Software_Engineering_Thursday_Timetable.png")
        await ctx.send(file = thu_se, embed = emb )

    @se.command(aliases =["friday", "F", "f", "Fri", "fri"])
    async def fri_se(self,ctx):
        fri_se = discord.File("file path here", filename = "Software_Engineering_Friday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Software Engineering Friday Timetable")
        emb.set_image(url = "attachment://Software_Engineering_Friday_Timetable.png")
        await ctx.send(file = fri_se, embed = emb )
    
    @timetable.group(aliases=["Net", "Networking"])
    async def net(self, ctx):
        if ctx.invoked_subcommand is None:
            full_net = discord.File("file path here", filename = "Networking_Full_Timetable.png")
            emb = discord.Embed(colour = discord.Colour.orange(), title = "Networking Full Timetable")
            emb.set_image(url = "attachment://Networking_Full_Timetable.png")
            await ctx.send(file = full_net, embed = emb )
    
    @net.command(aliases=["tuesday", "tu", "Tu", "tue"])
    async def tue_net(self, ctx):
        tue_net = discord.File("file path here", filename = "Networking_Tuesday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Networking Tuesday Timetable")
        emb.set_image(url = "attachment://Networking_Tuesday_Timetable.png")
        await ctx.send(file = tue_net, embed = emb )
    
    @net.command(aliases=["wednesday", "Wed", "W", "w", "wed"])
    async def wed_net(self, ctx):
        wed_net = discord.File("file path here", filename = "Networking_Wednesday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Networking Wednesday Timetable")
        emb.set_image(url = "attachment://Networking_Wednesday_Timetable.png")
        await ctx.send(file = wed_net, embed = emb )
    
    @net.command(aliases=["friday", "F", "f", "Fri", "fri"])
    async def fri_net(self, ctx):
        fri_net = discord.File("file path here", filename = "Networking_Friday_Timetable.png")
        emb = discord.Embed(colour = discord.Colour.orange(), title = "Networking Friday Timetable ")
        emb.set_image(url = "attachment://Networking_Friday_Timetable.png")
        await ctx.send(file = fri_net, embed = emb )

def setup(client):
    client.add_cog(Subcommands(client))