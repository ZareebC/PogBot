import discord
import random
import youtube_dl
import pymongo
from pymongo import MongoClient
from discord.ext import commands


token = open("token.txt", "r").read() 

client = discord.Client()
prefix = "*"
bot = commands.Bot(command_prefix=prefix)

cluster = MongoClient("mongodb+srv://ZareebPogBot:mack@cluster0-qlm8l.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]

collection = db["test"]



@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(ctx): 

    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")

    if str(ctx.content.lower()) == "happens":
        await ctx.channel.send('happens.')
        searchCheck = collection.find_one({"_id": ctx.author.id})
        if(searchCheck != ctx.author.id):
            post = {"_id": ctx.author.id, "score": 1}
            collection.insert_one(post)
        else:   
            search = collection.find({"_id": ctx.author.id})
            for x in search:
                score = x["score"]
            score = score * 1.156
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})

    elif str(ctx.content.lower()) == "pog": 
        if str(ctx.author.id) == "587456398926020622":
            await ctx.channel.send('minimal pog levels احترس')
        else:
            await ctx.channel.send('champ')
            post = {"_id": ctx.author.id, "score": 1}
            collection.insert_one(post)
            
    elif str(ctx.content.lower()) == "mango":
        await ctx.channel.send('https://flipgrid.com/s/00784e451eb0')

    elif str(ctx.content.lower()) == "trapmango":
        await ctx.channel.send('https://www.youtube.com/watch?v=XupBOtI2kgY&feature=youtu.be')

    elif str(ctx.content.lower()) == "*pogmeter":
        if str(ctx.author.id) == "95694371793408000":
            count = random.randint(-50,20)
            await ctx.channel.send("Pog level: " + str(count))

        elif str(ctx.author.id) == "495354649742802955":
            await ctx.channel.send('WARNING: too much pog')

        elif str(ctx.author.id) == "587456398926020622":
            await ctx.channel.send('-97 انه ما هو عليه')

        else:
            search = collection.find({"_id": ctx.author.id})
            for x in search:
                score = x["score"]
            await ctx.channel.send("Pog level: " + str(score))


    @client.command(pass_context=True)
    async def join(ctx):
        if ctx.message.author.voice:
            channel = ctx.message.author.voice.voice_channel
            await channel.connect()

    @client.command(pass_context = True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()


    @client.command(pass_context = True)
    async def play(ctx, url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
        
client.run(token)
