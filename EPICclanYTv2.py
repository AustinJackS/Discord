import discord
import discord.ext.commands
from random import randint
import time
mods=["Anoxane#6032","EPICclanYT#4094"]
magicball=["Certainly","Unclear","Unsure","My sources say yes","My sources say no","Roll again","Definitly not","Try again"]
client=discord.Client()
@client.event
async def on_message(message):
    #Check if any tempbans are due to be removed
    if message.content.startswith("$hello"):
        return await client.sned_message(message.channel, "Hello, world!")
    if message.content.startswith("$commands"):
        helpd="""
   ```
#    $commands - Prints this dialog.
#    $join [Channel to Join] - joins  Stream_Chat or other channels.
#    $leave [Channel to Leaves] - leaves  Stream_Chat or other channels.
#    $dice - Rolls a die
#    $EighBall - Does 8ball
#    $range [min] [max] - Generates a random integer
    ``
    """
        await client.send_message(message.channel, helpd)
    if message.content.startswith("$dice"):
        await client.send_message(message.channel,randint(0,6))
    if message.content.startswith("$EightBall"):
        await client.send_message(message.channel,magicball[randint(0,7)])
    if message.content.startswith("$range"):
        await client.send_message(message.channel,randint(int(message.content.split(' ')[1]),int(message.content.split(' ')[2])))
    if message.content.startswith("$mod add warning"):
        if str(message.author) in mods:
            f=open("warned.txt","a+")
            f.write(message.content.split(' ')[3]+'\n')
            f.close()
            await client.send_message(message.channel, "User: "+message.content.split(' ')[3]+" warned.")
        else:
            await client.send_message(message.channel,str(message.author))
    if message.content.startswith("$mod warned"):
        f=open("warned.txt","r")
        data=f.read()
        f.close()
        await client.send_message(message.channel,data)
    #After here you may need to change role ids/names
    #
    #
    if message.content.startswith("$mod promote"):
        #remember to replace with different role ids
        #below is how to get a user by name
        member_to_promote = discord.utils.find(lambda m: m.name == message.content.split(" ")[2], message.channel.server.members)
        roles=[
        "325059740982050827",
        "325060075657887745",
        ]
        #same thing with names here
        if str(message.author) in mods:
            role = discord.utils.get(message.server.roles, name="test1")
            if role in member_to_promote.roles:
                role = discord.utils.get(message.server.roles, name="test2")
                if role in member_to_promote.roles:
                    await client.send_message(message.channel, "User is the highest role promotion allows.")
                else:
                    await client.add_roles(member_to_promote, role)
                    await client.send_message(message.channel, "Sucessfully promoted!")
            else:
                await client.add_roles(member_to_promote, role)
                await client.send_message(message.channel, "Sucessfully promoted!")
    if message.content.startswith("$join"):
        team_list = ["Stream_Chat"]#remeber to change this
        entered_team = message.content.split(' ')[1]
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles for the teams
            "325244074024108032",#and this
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await client.send_message(message.channel, "Channel doesn't exist.")
            return
        elif role in message.author.roles:
            # If they already have the role
            await client.send_message(message.channel, "You already have acess to this channel.")
        else:
            try:
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully allowed acess to Stream_Chat")
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to add roles.")
    if message.content.startswith("$leave"):
        team_list = ["Stream_Chat"]#remeber to change this
        entered_team = message.content.split(' ')[1]
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles for the teams
            "325244074024108032",#and this
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await client.send_message(message.channel, "Channel doesn't exist.")
            return
        else:
            try:
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, "Successfully removed Stream_Chat.")
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to remove roles.")  
    if message.content.startswith("$mod tempban"):
        if str(message.author) in mods:
            day_to_remove=time.strftime("%d/%m/%Y")#need to add +5
            member_to_tempban = discord.utils.find(lambda m: m.name == message.content.split(" ")[2], message.channel.server.members)
            f=open("temp.txt","a+")
            f.write(message.content.split(" ")[2])
            f.close()
            await client.ban(member_to_tempban)
        
client.run("MzIzNDQzMDgxMTM3NjE4OTQ0.DB7NXA.tEzLxlE7NsJphl4uFlD5r_XD00g")
