import praw
import discord
from discord.ext import commands
import random

reddit = praw.Reddit(
        client_id = "client id here",
        client_secret = "client secret here",
        username = "reddit username here",
        password = "reddit acount pass",
        user_agent= "BoltON"
    )
class redditapi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        memeChannel = self.client.get_channel(755495014154502168)
        if ctx.channel != memeChannel:
           await ctx.send("You need to request this in the <#755495014154502168> channel. <:hehe:751942630048530493>")
        else:
            submissions = []
            subreddit = reddit.subreddit("ProgrammerHumor")
            hot = subreddit.top(limit = 50)

            for submission in hot:
                submissions.append(submission)
        
            ransub = random.choice (submissions)

            ran_name = ransub.title
            ran_url = ransub.url

            emb = discord.Embed(
                title = ran_name,
                colour = discord.Colour.orange()
            )
            emb.set_image( url = ran_url)
            await ctx.send(embed = emb)
        
def setup(client):
    client.add_cog(redditapi(client))