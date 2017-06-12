from random import randint
import discord
from discord.ext.commands import Bot
import ks
magicball=["Certainly","Unclear","Unsure","My sources say yes","My sources say no","Roll again","Definitly not","Try again"]
my_bot = Bot(command_prefix="$")
@my_bot.event
async def on_read():
    print("Client logged in")
@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")
@my_bot.command(pass_context=True)
async def id(ctx):
    return await my_bot.say(ctx.message.author.id)
@my_bot.command()
async def commands():
    helpd="""
   ```
#    $commands - Prints this dialog.
#    $join [Channel to Join] - joins  Stream_Chat or other channels. (Not yet added)
#    $id - prints author id for debugging.
#    $dice - Rolls a die
#    $EighBall - Does 8ball
#    $range [min] [max] - Generates a random integer
    ``
    """
    await my_bot.say(helpd)
@my_bot.command()
async def dice():
    await my_bot.say(randint(0,6))
@my_bot.command()
async def EightBall():
    await my_bot.say(magicball[randint(0,7)])
@my_bot.command()
async def range(*args):
    await my_bot.say(randint(int(args[0]),int(args[1])))
#https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.move_member
@my_bot.command(pass_context=True)
async def mod(ctx,*args):
    if args[0]=="warned":
        f=open("warned.txt","r")
        data=f.read()
        await my_bot.say(data)
        f.close();
    if args[0]=="add" and args[1]=="warning":
        if "Anoxane" in str(ctx.message.author) or "EPICclanYT" in str(ctx.message.author):
            f=open("warned.txt","a+")
            f.write(args[2]+"\n")
            f.close();
            await my_bot.say("User "+args[2]+" warned.")
        await my_bot.say(str(ctx.message.author))
@my_bot.command()
async def yee(*args):
    i=0
    yee=""
    while i<int(args[0]):
        yee+=args[1]+" YEE\n"
        i+=1
    try:
        await my_bot.say(yee)
    except Exception as e:
        await my_bot.say(e)
@my_bot.command()
async def yee_infinity(*args):
    i=0
    yee=""
    while i<int(args[0]):
        yee+=args[1]+" YEE\n"
        i+=1
    try:
        while True:
            await my_bot.say(yee)
    except Exception as e:
        await my_bot.say(e)
@my_bot.command()
async def yee_stop():
    await my_bot.say("Stopped deadly yee guns of death.")
    ks.restart_program()
#@my_bot.command(pass_context=True)
'''async def join(ctx, *args):
    my_bot.move_member(ctx.message.author.id,"323511932680142855")
'''

my_bot.run("MzIzNDQzMDgxMTM3NjE4OTQ0.DB7NXA.tEzLxlE7NsJphl4uFlD5r_XD00g")
