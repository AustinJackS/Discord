import discord
import discord.ext.commands
from random import randint
import time
mods=["Anoxane#6032","EPICclanYT#4094"]
magicball=["Certainly","Unclear","Unsure","My sources say yes","My sources say no","Roll again","Definitly not","Try again"]
client=discord.Client()
#all commands are defined below!
@client.event
async def on_message(message):
    #Check if any tempbans are due to be removed
    f=open("temp.txt","r")#this is really broken
    tempbans=f.read().split('\n')
    f.close()
    try:
        tempbans.remove('')
    except:
        pass
    for tmpban in tempbans:
        if tmpban.split(',')[1]==time.strftime("%d/%m/%Y"):
            #tempban is due to be removed :)
            #debug line here 
            member_to_unban = await client.get_user_info(tmpban.split(',')[0])
            remove_member=tmpban
            await client.unban(message.server, member_to_unban)
            f.close()
            #clean the file
            f=open("temp.txt","w")
            for line in tempbans:
                if line!=tmpban:
                    f.write(line)
            await client.send_message(message.channel, "`A tempban has just been lifted :)`")
    if message.content.startswith("$hello"):
        return await client.send_message(message.channel, "Hello, world!")
    if message.content.startswith("$commands"):
        helpd="""
   ```
#    $commands - Prints this dialog.
#    $join [Channel to Join] - joins  Stream_Chat or other channels.
#    $leave [Channel to Leaves] - leaves  Stream_Chat or other channels.
#    $dice - Rolls a die
#    $EighBall - Does 8ball
#    $range [min] [max] - Generates a random integer
#    $mod [add/remove/promote/demote/tempban] [warning/(user)] (user)
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
        "322458329429573633",
        "322448115590234112",
        ]
        #same thing with names here
        if str(message.author) in mods:
            role = discord.utils.get(message.server.roles, name="The Lava Squad")
            if role in member_to_promote.roles:
                role = discord.utils.get(message.server.roles, name="Trusted Person")
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
            day=str(int(time.strftime("%d"))+5)
            day_to_remove=time.strftime(day+"/%m/%Y")#day/month/year
            member_to_tempban = discord.utils.find(lambda m: m.name == message.content.split(" ")[2], message.channel.server.members)
            f=open("temp.txt","a+")
            f.write("\n"+member_to_tempban.id+","+day_to_remove)
            f.close()
            try:
                await client.ban(member_to_tempban)
                await client.send_message(message.channel, "User tempbanned until: "+day_to_remove)
            except discord.errors.Forbidden:
                await client.send_message(message.channel, "Your privledge is two low to ban this user.")
    if message.content.startswith("$mod demote"):
        notdemoted=True
        #remember to replace with different role ids
        #below is how to get a user by name
        member_to_promote = discord.utils.find(lambda m: m.name == message.content.split(" ")[2], message.channel.server.members)
        roles=[
        "322458329429573633",
        "322448115590234112",
        ]
        #same thing with names here
        if str(message.author) in mods:
            role = discord.utils.get(message.server.roles, name="Trusted Person")
            if role in member_to_promote.roles:
                await client.remove_roles(member_to_promote, role)
                await client.send_message(message.channel, "Sucessfully demoted.")
                notdemoted=False
            role = discord.utils.get(message.server.roles, name="The Lava Squad")
            if role in member_to_promote.roles and notdemoted:
                await client.remove_roles(member_to_promote, role)
                await client.send_message(message.channel, "Sucessfully demoted.")
            elif notdemoted:
                await client.send_message(message.channel, "Cannot demote member any more.")
client.run("MzIzNDQzMDgxMTM3NjE4OTQ0.DB7NXA.tEzLxlE7NsJphl4uFlD5r_XD00g")
