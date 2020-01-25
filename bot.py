import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready to go!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


@client.command()
async def help(ctx):
    author = ctx.message.author


    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.dev', value='Shows the developers of Waterfall', inline=False)

    await client.say(author, embed=embed)




@client.command()
async def dev(ctx):
    await ctx.send('Waterfall is developed by Psycho.')


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)










client.run('NDg4NDczMTQxOTE2NDY3MjM5.XivGxg.9r45k1Dv3_6MkNyI3F5VBG0s6W0')
