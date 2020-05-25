import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '.' )
# .help

@client.event

async def on_ready():
	print("Hi")

@client.command( pass_context = True )

async def hello( ctx ):
	await ctx.send( "Привет, меня разработал Евгений Павлов, по всем вопросам ему в лс" )

@client.command( pass_context = True )

async def pls( ctx ):
	await ctx.send( "Список доступных комманд .hello - приветствие .pls - помощь" )

@client.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 712620402362548315:
        for guild in client.guilds:
            if guild.id == 704937265150820455:
                mainCategory = discord.utils.get(guild.categories, id=704940793655328818)
                channel2 = await guild.create_voice_channel(name=f"{member.display_name}",category=mainCategory)
                await member.move_to(channel2)
                await channel2.set_permissions(member,manage_channels=True)
                def check(a,b,c):
                    return len(channel2.members) == 0
                await client.wait_for('voice_state_update', check=check)
                await channel2.delete()

#connect

token = open( 'token.txt', 'r' ).readline()

client.run( token )

