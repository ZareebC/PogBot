import discord
import random
from discord.ext import commands
#from keepbot import keep_alive
#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = open("token.txt", "r").read()  # I've opted to just save my token to a text file. 

client = discord.Client()  # starts the discord client.
prefix = "*"
bot = commands.Bot(command_prefix=prefix)
@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event  
async def on_command_error(ctx, error):
    await ctx.send(error)

@client.event
async def on_message(ctx):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    if str(ctx.content.lower()) == "pog":
        if str(ctx.author.id) == "447751905364541442":
            await ctx.channel.send('minimal pog levels')
        else:
            await ctx.channel.send('champ')
    if str(ctx.content.lower()) == "*pogmeter":
        count = random.randint(1,101)
        await ctx.channel.send("Pog level: " + str(count))


#keep_alive()
client.run(token)  # recall my token was saved!
