import discord
import discord.ext.commands
from random import randint
mods=["Anoxane#6032","EPICclanYT#4094"]
magicball=["Certainly","Unclear","Unsure","My sources say yes","My sources say no","Roll again","Definitly not","Try again"]
client=discord.Client()
@client.event
async def on_message(message):
    '''if message.content.startswith("$role"):#this works it's just a demo
        team_list = ["test1", "test2"]
        entered_team = message.content[6:].lower()
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles for the teams
            "325059740982050827",
            "200087567318646793",
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await client.send_message(message.channel, "Role doesn't exist.")
            return
        elif role in message.author.roles:
            # If they already have the role
            await client.send_message(message.channel, "You already have this role.")
        else:
            try:
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to add roles.")'''
    if message.content.startswith("$hello"):
        return await client.sned_message(message.channel, "Hello, world!")
    if message.content.startswith("$commands"):
        helpd="""
   ```
#    $commands - Prints this dialog.
#    $join [Channel to Join] - joins  Stream_Chat or other channels. (Not yet added)
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
    if message.content.startswith("$mod promote"):
        #remember to replace with different role ids
        roles=[
        "325059740982050827",
        "325060075657887745",
        ]
        #same thing with names here
        role = discord.utils.get(message.server.roles, name="test1")
        if role in message.author.roles:
            role = discord.utils.get(message.server.roles, name="test2")
            if role in message.author.roles:
                await client.send_message(message.channel, "User is the highest role promotion allows.")
            else:
                await client.add_roles(client.getmember(message.content.split(' ')[2]), role)
                await client.send_message(message.channel, "Sucessfully promoted! The user may now remove their old role.")
        else:
            await client.add_roles(client.get_member(message.content.split(' ')[2], role))
            await client.send_message(message.channel, "Sucessfully promoted! The user may now remove their old role.")
client.run("MzIzNDQzMDgxMTM3NjE4OTQ0.DB7NXA.tEzLxlE7NsJphl4uFlD5r_XD00g")
