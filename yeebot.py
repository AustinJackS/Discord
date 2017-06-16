from random import randint
import discord
from discord.ext.commands import Bot
import ks
mods=["Anoxane#6032","EPICclanYT#4094"]
magicball=["Certainly","Unclear","Unsure","My sources say yes","My sources say no","Roll again","Definitly not","Try again"]
my_bot = Bot(command_prefix="$")
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
my_bot.run("MzI1MDY2NDAwMzg3NDMyNDQ4.DCS1MQ.F8dTx3IHqQGF2pyvSJuc-QPw8lc")
