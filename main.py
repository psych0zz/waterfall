import discord 
import random
import asyncio
import webserver
from discord.ext import commands
from webserver import keep_alive
import os
import config
import socket
import json
import re
import requests
import time
import youtube_dl
from discord.utils import get
import datetime


client = commands.Bot(command_prefix = '.')
client.remove_command('help')


@client.event
async def on_ready():
  activity = discord.Activity(name='Psycho code me', type=discord.ActivityType.watching)
  await client.change_presence(activity=activity)
  print('Bot is ready to go!')


    
  



  




@client.event
async def on_member_join(member):





  embed = discord.Embed(

        colour = discord.Colour.blue()
    )

  embed.set_author(name='Waterfall')
  embed.add_field(name='Welcome!', value=f'Welcome to my server, {member.mention}')


  embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
  embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
  embed.timestamp = datetime.datetime.utcnow()

  channel = client.get_channel(676173329731944468)


  await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
  embed = discord.Embed(

        colour = discord.Colour.blue()
    )

  embed.set_author(name='Waterfall')
  embed.add_field(name='Goodbye.', value=f'{member.mention} has just left the server.')
  
    


  embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
  embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
  embed.timestamp = datetime.datetime.utcnow()

  channel = client.get_channel(676173329731944468)


  await channel.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please pass in all required arguments.')





@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member : discord.Member=None):
  if not member:
    await ctx.send("Please specify a member.")
    return
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  await member.remove_roles(role)
  await ctx.send(f"{member.mention} has been unmuted.")

  


@unmute.error
async def unmute_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("You are not allowed to unmute people.")









@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member.")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"{member.mention} has been muted.")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people.")




@client.command() 
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None): 
 await member.kick(reason=reason)

@client.command() 
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None): 
 await member.ban(reason=reason)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def spam(ctx):
    while True:
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")
        await ctx.send("@everyone\nBRUH\n@everyone\nLEAVE THIS ASS SERVER NIGGA\n")








        


       




@client.command()
async def porn(ctx):
  await ctx.send(file=discord.File('lacking.png'))









@client.command(aliases=['peepee', 'penis', 'pp'])
async def _peepee(ctx):
  responses = [
    '8=D',
    '8==D',
    '8===D',
    '8====D',
    '8=====D',
    '8======D',
    '8=======D',
    '8========D',
    '8=========D',
    '8===========================D, Nice.',]


  await ctx.send(f'\n{random.choice(responses)}')




@client.command(aliases=['showerthoughts', 'showerthought'])
async def _showerthoughts(ctx):
  responses = [
    'Nobody gave us the source code for how our bodies work so we’ve basically spent centuries reverse engineering ourselves',
    'If anyone is terrified of the idea their house is haunted- get a cat. Items will move around and disappear just the same. It gives you plausible deniability.',
    'The most unrealistic thing in GTA 5 is all the available parking',
    'If Ice Cube drowned, it would be a cruel, ironic death.',
    'In about 110 years there will be a millions of inactive social media accounts',
    'Hangman is a game about a man killing himself just because people cant read your mind.',
    'When phones become waterproof in the future, we will be able to push people into pools carelessly again.',
    '“Cousin” is the only gender neutral title on the family tree.',
    'We are closer to the ocean bottom than the moon, yet we decided to go to the moon.',
    'Mirrors reflect 85-90% of light, so we can just see a blurred, incomplete image of ourselves.',]

  await ctx.send(file=discord.File('shower.png'))
  await ctx.send(f'\n{random.choice(responses)}')





@client.command(aliases=['uselessweb', 'theuselessweb'])
async def _uselessweb(ctx):
  responses = [
    'http://heeeeeeeey.com/',
		'http://tinytuba.com/',
		'http://corndog.io/',
		'http://thatsthefinger.com/',
		'http://cant-not-tweet-this.com/',
		'http://weirdorconfusing.com/',
		'http://eelslap.com/',
		'http://www.staggeringbeauty.com/',
		'http://burymewithmymoney.com/',
		'http://endless.horse/',
		'http://www.trypap.com/',
		'http://www.republiquedesmangues.fr/',
		'http://www.movenowthinklater.com/',
		'http://www.partridgegetslucky.com/',
		'http://www.rrrgggbbb.com/',
		'http://beesbeesbees.com/',
		'http://www.koalastothemax.com/',
		'http://www.everydayim.com/',
		'http://randomcolour.com/',
		'http://cat-bounce.com/',
		'http://chrismckenzie.com/',
		'http://hasthelargehadroncolliderdestroyedtheworldyet.com/',
		'http://ninjaflex.com/',
		'http://ihasabucket.com/',
		'http://corndogoncorndog.com/',
		'http://www.hackertyper.com/',
		'https://pointerpointer.com',
		'http://imaninja.com/',
		'http://www.ismycomputeron.com/',
		'http://www.nullingthevoid.com/',
		'http://www.muchbetterthanthis.com/',
		'http://www.yesnoif.com/',
		'http://iamawesome.com/',
		'http://www.pleaselike.com/',
		'http://crouton.net/',
		'http://corgiorgy.com/',
		'http://www.wutdafuk.com/',
		'http://unicodesnowmanforyou.com/',
		'http://www.crossdivisions.com/',
		'http://tencents.info/',
		'http://www.patience-is-a-virtue.org/',
		'http://pixelsfighting.com/',
		'http://isitwhite.com/',
		'http://onemillionlols.com/',
		'http://www.omfgdogs.com/',
		'http://oct82.com/',
		'http://chihuahuaspin.com/',
		'http://www.blankwindows.com/',
		'http://dogs.are.the.most.moe/',
		'http://tunnelsnakes.com/',
		'http://www.trashloop.com/',
		'http://www.ascii-middle-finger.com/',
		'http://spaceis.cool/',
		'http://www.donothingfor2minutes.com/',
		'http://buildshruggie.com/',
		'http://buzzybuzz.biz/',
		'http://yeahlemons.com/',
		'http://burnie.com/',
		'http://wowenwilsonquiz.com',
		'https://thepigeon.org/',
		'http://notdayoftheweek.com/',
		'http://www.amialright.com/',
		'http://nooooooooooooooo.com/',
		'https://greatbignothing.com/',]


  await ctx.send(f'Enjoy,\n{random.choice(responses)}')











  

  





  
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def admin(ctx):



  embed = discord.Embed(
  colour = discord.Colour.red()
  )

  embed.set_author(name='Admin Help')
  embed.add_field(name='.kick', value='Kicks the specified member (requires admin)', inline=False)
  embed.add_field(name='.ban', value='Bans the specified member (requires admin)', inline=False)
  embed.add_field(name='.unban', value='Unbans the specified member (requires admin)', inline=False)
  embed.add_field(name='.mute', value='Mutes the specified member (requires admin)', inline=False)
  embed.add_field(name='.unmute', value='Unmutes the specified member (requires admin)', inline=False)
  embed.timestamp = datetime.datetime.utcnow()


  

  await ctx.send(embed=embed)

  

  
  





@client.command(pass_context=True)
async def help(ctx):
       


        embed = discord.Embed(
        colour = discord.Colour.blue()
        )

        embed.set_author(name='Help')
        embed.add_field(name='.dev', value='Shows the developers of Waterfall.',
        inline=False) 
        embed.add_field(name='.nuke', value='Nukes the channel you type the command in.', inline=False)
        embed.add_field(name='.gay', value ='Check how gay you are.', inline=False)
        embed.add_field(name='.porn', value=';)', inline=False)
        embed.add_field(name='.uselessweb', value='The useless web.', inline=False)
        embed.add_field(name='.peepee', value='Big or small?', inline=False)
        embed.add_field(name='.showerthoughts', value='Thoughts in the shower.', inline=False)
        embed.add_field(name='.prntscrn', value='Shows you a random prnt.sc link. (NSFW Only)', inline=False)

        

        await ctx.send(embed=embed)












        




@client.command()
async def dev(ctx):

        embed = discord.Embed(
          colour = discord.Colour.red()
        )

        embed.set_author(name='Developers')
        embed.add_field(name='Devs', value='Waterfall is developed by Psycho.', inline=False)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount=1000):
  await ctx.channel.purge(limit=amount)
  
  await ctx.send('Nuked this channel.') 
  time.sleep(2)
  await ctx.delete_messages






@client.command(aliases=['gay', 'amigay'])
async def _gay(ctx):
  responses = ['You are 1% gay. :rainbow_flag:', 
              'You are 2% gay. :rainbow_flag:',
              'You are 3% gay. :rainbow_flag:',
              'You are 4% gay. :rainbow_flag:',
              'You are 5% gay. :rainbow_flag:',
              'You are 6% gay. :rainbow_flag:',
              'You are 7% gay. :rainbow_flag:',
              'You are 8% gay. :rainbow_flag:',
              'You are 9% gay. :rainbow_flag:',
              'You are 10% gay. :rainbow_flag:',
              'You are 11% gay. :rainbow_flag:',
              'You are 12% gay. :rainbow_flag:',
              'You are 13% gay. :rainbow_flag:',
              'You are 14% gay. :rainbow_flag:',
              'You are 15% gay. :rainbow_flag:',
              'You are 16% gay. :rainbow_flag:',
              'You are 17% gay. :rainbow_flag:',
              'You are 18% gay. :rainbow_flag:',
              'You are 19% gay. :rainbow_flag:',
              'You are 20% gay. :rainbow_flag:',
              'You are 21% gay. :rainbow_flag:',
              'You are 22% gay. :rainbow_flag:',
              'You are 23% gay. :rainbow_flag:',
              'You are 24% gay. :rainbow_flag:',
              'You are 25% gay. :rainbow_flag:',
              'You are 26% gay. :rainbow_flag:',
              'You are 27% gay. :rainbow_flag:',
              'You are 28% gay. :rainbow_flag:',
              'You are 29% gay. :rainbow_flag:',
              'You are 30% gay. :rainbow_flag:',
              'You are 31% gay. :rainbow_flag:',
              'You are 32% gay. :rainbow_flag:',
              'You are 33% gay. :rainbow_flag:',
              'You are 34% gay. :rainbow_flag:',
              'You are 35% gay. :rainbow_flag:',
              'You are 36% gay. :rainbow_flag:',
              'You are 37% gay. :rainbow_flag:',
              'You are 38% gay. :rainbow_flag:',
              'You are 39% gay. :rainbow_flag:',
              'You are 40% gay. :rainbow_flag:',
              'You are 50% gay. :rainbow_flag:',
              'You are 51% gay. :rainbow_flag:',
              'You are 52% gay. :rainbow_flag:',
              'You are 53% gay. :rainbow_flag:',
              'You are 54% gay. :rainbow_flag:',
              'You are 55% gay. :rainbow_flag:',
              'You are 56% gay. :rainbow_flag:',
              'You are 57% gay. :rainbow_flag:',
              'You are 58% gay. :rainbow_flag:',
              'You are 59% gay. :rainbow_flag:',
              'You are 60% gay. :rainbow_flag:',
              'You are 61% gay. :rainbow_flag:',
              'You are 62% gay. :rainbow_flag:',
              'You are 63% gay. :rainbow_flag:',
              'You are 64% gay. :rainbow_flag:',
              'You are 65% gay. :rainbow_flag:',
              'You are 66% gay. :rainbow_flag:',
              'You are 67% gay. :rainbow_flag:',
              'You are 68% gay. :rainbow_flag:',
              'You are 69% gay. :rainbow_flag:',
              'You are 70% gay. :rainbow_flag:',
              'You are 71% gay. :rainbow_flag:',
              'You are 72% gay. :rainbow_flag:',
              'You are 73% gay. :rainbow_flag:',
              'You are 74% gay. :rainbow_flag:',
              'You are 75% gay. :rainbow_flag:',
              'You are 76% gay. :rainbow_flag:',
              'You are 77% gay. :rainbow_flag:',
              'You are 78% gay. :rainbow_flag:',
              'You are 79% gay. :rainbow_flag:',
              'You are 80% gay. :rainbow_flag:',
              'You are 81% gay. :rainbow_flag:',
              'You are 82% gay. :rainbow_flag:',
              'You are 83% gay. :rainbow_flag:',
              'You are 84% gay. :rainbow_flag:',
              'You are 85% gay. :rainbow_flag:',
              'You are 86% gay. :rainbow_flag:',
              'You are 87% gay. :rainbow_flag:',
              'You are 88% gay. :rainbow_flag:',
              'You are 89% gay. :rainbow_flag:',
              'You are 90% gay. :rainbow_flag:',
              'You are 91% gay. :rainbow_flag:',
              'You are 92% gay. :rainbow_flag:',
              'You are 93% gay. :rainbow_flag:',
              'You are 94% gay. :rainbow_flag:',
              'You are 95% gay. :rainbow_flag:',
              'You are 96% gay. :rainbow_flag:',
              'You are 97% gay. :rainbow_flag:',
              'You are 98% gay. :rainbow_flag:',
              'You are 99% gay. :rainbow_flag:',
              'You are 100% gay :rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag:',]

  await ctx.send(f'\nWow, {random.choice(responses)}')







@client.command(aliases=['prntscr', 'prntscrn'])
@commands.has_permissions(send_messages=True)
async def _prntscr(ctx):
  responses = [
                'http://prnt.sc/qgn5kl',
'http://prnt.sc/qgnt6i',
'http://prnt.sc/qgnqh0',
'http://prnt.sc/qgnxcv',
'http://prnt.sc/qgniro',
'http://prnt.sc/qgnkru',
'http://prnt.sc/qgnu4o',
'http://prnt.sc/qgn9e7',
'http://prnt.sc/qgn5qh',
'http://prnt.sc/qgn72g',
'http://prnt.sc/qgn0r3',
'http://prnt.sc/qgn6vq',
'http://prnt.sc/qgnn62',
'http://prnt.sc/qgncnw',
'http://prnt.sc/qgnvm2',
'http://prnt.sc/qgnvka',
'http://prnt.sc/qgnmpl',
'http://prnt.sc/qgnji6',
'http://prnt.sc/qgncua',
'http://prnt.sc/qgntg4',
'http://prnt.sc/qgnc7h',
'http://prnt.sc/qgn59r',
'http://prnt.sc/qgnyqf',
'http://prnt.sc/qgno6x',
'http://prnt.sc/qgnryn',
'http://prnt.sc/qgnlm3',
'http://prnt.sc/qgnx5t',
'http://prnt.sc/qgna2o',
'http://prnt.sc/qgnp3t',
'http://prnt.sc/qgnyzb',
'http://prnt.sc/qgn0hc',
'http://prnt.sc/qgn8vn',
'http://prnt.sc/qgnh07',
'http://prnt.sc/qgn9gc',
'http://prnt.sc/qgnen2',
'http://prnt.sc/qgnycq',
'http://prnt.sc/qgnc7x',
'http://prnt.sc/qgnfkv',
'http://prnt.sc/qgn5al',
'http://prnt.sc/qgnpfv',
'http://prnt.sc/qgnqgw',
'http://prnt.sc/qgnnms',
'http://prnt.sc/qgn5oa',
'http://prnt.sc/qgnlbd',
'http://prnt.sc/qgn2tf',
'http://prnt.sc/qgn3c2',
'http://prnt.sc/qgn1qy',
'http://prnt.sc/qgnrmt',
'http://prnt.sc/qgnaee',
'http://prnt.sc/qgndj1',
'http://prnt.sc/qgniwm',
'http://prnt.sc/qgnmuj',
'http://prnt.sc/qgn6st',
'http://prnt.sc/qgnnga',
'http://prnt.sc/qgnkqm',
'http://prnt.sc/qgn7ug',
'http://prnt.sc/qgndbn',
'http://prnt.sc/qgnhy6',
'http://prnt.sc/qgnpua',
'http://prnt.sc/qgng5b',
'http://prnt.sc/qgng75',
'http://prnt.sc/qgnfyk',
'http://prnt.sc/qgnnr3',
'http://prnt.sc/qgnua8',
'http://prnt.sc/qgnd4g',
'http://prnt.sc/qgnkx7',
'http://prnt.sc/qgnosz',
'http://prnt.sc/qgnsuk',
'http://prnt.sc/qgnk6z',
'http://prnt.sc/qgnx5g',
'http://prnt.sc/qgndiz',
'http://prnt.sc/qgn0qi',
'http://prnt.sc/qgnevw',
'http://prnt.sc/qgnnm3',
'http://prnt.sc/qgnnjk',
'http://prnt.sc/qgnwmw',
'http://prnt.sc/qgnxvs',
'http://prnt.sc/qgnd53',
'http://prnt.sc/qgnem7',
'http://prnt.sc/qgn40t',
'http://prnt.sc/qgnmor',
'http://prnt.sc/qgnqw6',
'http://prnt.sc/qgn486',
'http://prnt.sc/qgntyo',
'http://prnt.sc/qgnc7u',
'http://prnt.sc/qgnplh',
'http://prnt.sc/qgnurs',
'http://prnt.sc/qgnuc9',
'http://prnt.sc/qgnadz',
'http://prnt.sc/qgnbp2',
'http://prnt.sc/qgngi0',
'http://prnt.sc/qgngb9',
'http://prnt.sc/qgndnz',
'http://prnt.sc/qgn6gc',
'http://prnt.sc/qgnwsv',
'http://prnt.sc/qgnv4f',
'http://prnt.sc/qgn6vo',
'http://prnt.sc/qgnld0',
'http://prnt.sc/qgny32',
'http://prnt.sc/qgnnqm',
'http://prnt.sc/qgns11',
'http://prnt.sc/qgn2p4',
'http://prnt.sc/qgn5lv',
'http://prnt.sc/qgns7q',
'http://prnt.sc/qgn35a',
'http://prnt.sc/qgn49q',
'http://prnt.sc/qgn2b9',
'http://prnt.sc/qgn1qn',
'http://prnt.sc/qgn9op',
'http://prnt.sc/qgn6fx',
'http://prnt.sc/qgn2yo',
'http://prnt.sc/qgnaeo',
'http://prnt.sc/qgnnas',
'http://prnt.sc/qgnwf4',
'http://prnt.sc/qgnvlu',
'http://prnt.sc/qgnujg',
'http://prnt.sc/qgn9mi',
'http://prnt.sc/qgnfdw',
'http://prnt.sc/qgnpne',
'http://prnt.sc/qgn2rz',
'http://prnt.sc/qgnz9o',
'http://prnt.sc/qgnhmm',
'http://prnt.sc/qgn4yv',
'http://prnt.sc/qgnjyz',
'http://prnt.sc/qgnz5b',
'http://prnt.sc/qgnher',
'http://prnt.sc/qgnlqh',
'http://prnt.sc/qgntua',
'http://prnt.sc/qgn4zc',
'http://prnt.sc/qgnfv9',
'http://prnt.sc/qgnpty',
'http://prnt.sc/qgn6wg',
'http://prnt.sc/qgn2ws',
'http://prnt.sc/qgnkzv',
'http://prnt.sc/qgnzfg',
'http://prnt.sc/qgnvtr',
'http://prnt.sc/qgn4na',
'http://prnt.sc/qgnrmn',
'http://prnt.sc/qgnhtz',
'http://prnt.sc/qgnqxh',
'http://prnt.sc/qgnqyx',
'http://prnt.sc/qgny0a',
'http://prnt.sc/qgn6dd',
'http://prnt.sc/qgnnnj',
'http://prnt.sc/qgnlsn',
'http://prnt.sc/qgnhx7',
'http://prnt.sc/qgnibc',
'http://prnt.sc/qgns4y',
'http://prnt.sc/qgnql7',
'http://prnt.sc/qgnajf',
'http://prnt.sc/qgnep8',
'http://prnt.sc/qgn2pa',
'http://prnt.sc/qgnjdx',
'http://prnt.sc/qgnt4k',
'http://prnt.sc/qgnz4b',
'http://prnt.sc/qgnofo',
'http://prnt.sc/qgns43',
'http://prnt.sc/qgnn6r',
'http://prnt.sc/qgn990',
'http://prnt.sc/qgnpzz',
'http://prnt.sc/qgnppo',
'http://prnt.sc/qgn0h4',
'http://prnt.sc/qgnqzk',
'http://prnt.sc/qgnwfj',
'http://prnt.sc/qgnm73',
'http://prnt.sc/qgnwf6',
'http://prnt.sc/qgnoxr',
'http://prnt.sc/qgnb23',
'http://prnt.sc/qgnp99',
'http://prnt.sc/qgn1s2',
'http://prnt.sc/qgnp7a',
'http://prnt.sc/qgnspu',
'http://prnt.sc/qgnoll',
'http://prnt.sc/qgn4id',
'http://prnt.sc/qgnpff',
'http://prnt.sc/qgnjy4',
'http://prnt.sc/qgnxqj',
'http://prnt.sc/qgnf5p',
'http://prnt.sc/qgnml3',
'http://prnt.sc/qgnm85',
'http://prnt.sc/qgn5mt',
'http://prnt.sc/qgne2a',
'http://prnt.sc/qgnukp',
'http://prnt.sc/qgnvg0',
'http://prnt.sc/qgnaml',
'http://prnt.sc/qgndf2',
'http://prnt.sc/qgns7a',
'http://prnt.sc/qgnjv1',
'http://prnt.sc/qgn84w',
'http://prnt.sc/qgnqy5',
'http://prnt.sc/qgn0ec',
'http://prnt.sc/qgn56f',
'http://prnt.sc/qgnwek',
'http://prnt.sc/qgntp1',
'http://prnt.sc/qgnaf8',
'http://prnt.sc/qgn52i',
'http://prnt.sc/qgnk8y',
'http://prnt.sc/qgn2nf',
'http://prnt.sc/qgnm6j',
'http://prnt.sc/qgnwnb',
'http://prnt.sc/qgnl68',
'http://prnt.sc/qgnkq9',
'http://prnt.sc/qgnae8',
'http://prnt.sc/qgn9wk',
'http://prnt.sc/qgnq97',
'http://prnt.sc/qgn2c0',
'http://prnt.sc/qgnlu5',
'http://prnt.sc/qgnohi',
'http://prnt.sc/qgntnn',
'http://prnt.sc/qgn9v9',
'http://prnt.sc/qgn9dk',
'http://prnt.sc/qgnkfn',
'http://prnt.sc/qgnlue',
'http://prnt.sc/qgnde6',
'http://prnt.sc/qgnfxw',
'http://prnt.sc/qgnqc3',
'http://prnt.sc/qgne0h',
'http://prnt.sc/qgnc9m',
'http://prnt.sc/qgnak5',
'http://prnt.sc/qgnyna',
'http://prnt.sc/qgn6lm',
'http://prnt.sc/qgnqsc',
'http://prnt.sc/qgn6lm',
'http://prnt.sc/qgnl56',
'http://prnt.sc/qgno3q',
'http://prnt.sc/qgnfch',
'http://prnt.sc/qgnoyb',
'http://prnt.sc/qgnrd9',
'http://prnt.sc/qgnu97',
'http://prnt.sc/qgndcf',
'http://prnt.sc/qgn14s',
'http://prnt.sc/qgnr7f',
'http://prnt.sc/qgnehp',
'http://prnt.sc/qgn1as',
'http://prnt.sc/qgncvh',
'http://prnt.sc/qgn1om',
'http://prnt.sc/qgn1lg',
'http://prnt.sc/qgnrt0',
'http://prnt.sc/qgnqzi',
'http://prnt.sc/qgnfed',
'http://prnt.sc/qgnuku',
'http://prnt.sc/qgnp46',
'http://prnt.sc/qgn6h1',
'http://prnt.sc/qgnzuh',
'http://prnt.sc/qgnh71',
'http://prnt.sc/qgni37',
'http://prnt.sc/qgnja6',
'http://prnt.sc/qgnodj',
'http://prnt.sc/qgn0kl',
'http://prnt.sc/qgnyfg',
'http://prnt.sc/qgng4z',
'http://prnt.sc/qgnta3',
'http://prnt.sc/qgn9r1',
'http://prnt.sc/qgnpa0',
'http://prnt.sc/qgngef',
'http://prnt.sc/qgni9d',
'http://prnt.sc/qgn78f',
'http://prnt.sc/qgnl3h',
'http://prnt.sc/qgnt3b',
'http://prnt.sc/qgnu3g',
'http://prnt.sc/qgnh0r',
'http://prnt.sc/qgnzcc',
'http://prnt.sc/qgn806',
'http://prnt.sc/qgndcy',
'http://prnt.sc/qgn81g',
'http://prnt.sc/qgnhyt',
'http://prnt.sc/qgnk5y',
'http://prnt.sc/qgnc33',
'http://prnt.sc/qgnjwa',
'http://prnt.sc/qgnllo',
'http://prnt.sc/qgn73p',
'http://prnt.sc/qgn6rl',
'http://prnt.sc/qgnkyx',
'http://prnt.sc/qgnoew',
'http://prnt.sc/qgnx4q',
'http://prnt.sc/qgnvjy',
'http://prnt.sc/qgnqzo',
'http://prnt.sc/qgnw33',
'http://prnt.sc/qgn90j',
'http://prnt.sc/qgnrvi',
'http://prnt.sc/qgnn2c',
'http://prnt.sc/qgngod',
'http://prnt.sc/qgnvps',
'http://prnt.sc/qgnx7d',
'http://prnt.sc/qgnxvv',
'http://prnt.sc/qgnwzh',
'http://prnt.sc/qgnf8j',
'http://prnt.sc/qgnmo3',
'http://prnt.sc/qgnvip',
'http://prnt.sc/qgnn5i',
'http://prnt.sc/qgnzyw',
'http://prnt.sc/qgnxyx',
'http://prnt.sc/qgnn8a',
'http://prnt.sc/qgnx5f',
'http://prnt.sc/qgne8p',
'http://prnt.sc/qgndbv',
'http://prnt.sc/qgnn8e',
'http://prnt.sc/qgnbtl',
'http://prnt.sc/qgntca',
'http://prnt.sc/qgnwk6',
'http://prnt.sc/qgn4u4',
'http://prnt.sc/qgnp4g',
'http://prnt.sc/qgnasa',
'http://prnt.sc/qgn5ae',
'http://prnt.sc/qgnhid',
'http://prnt.sc/qgnc5y',
'http://prnt.sc/qgntb8',
'http://prnt.sc/qgnaqn',
'http://prnt.sc/qgnou2',
'http://prnt.sc/qgn9a5',
'http://prnt.sc/qgn0ao',
'http://prnt.sc/qgn3lf',
'http://prnt.sc/qgn20t',
'http://prnt.sc/qgnyya',
'http://prnt.sc/qgnzfv',
'http://prnt.sc/qgn8l2',
'http://prnt.sc/qgnhnt',
'http://prnt.sc/qgn6yl',
'http://prnt.sc/qgnygo',
'http://prnt.sc/qgnb2q',
'http://prnt.sc/qgnhll',
'http://prnt.sc/qgnz6e',
'http://prnt.sc/qgny5c',
'http://prnt.sc/qgnjsp',
'http://prnt.sc/qgnjh3',
'http://prnt.sc/qgnyfr',
'http://prnt.sc/qgnb5w',
'http://prnt.sc/qgnouc',
'http://prnt.sc/qgn9uo',
'http://prnt.sc/qgn129',
'http://prnt.sc/qgn6ei',
'http://prnt.sc/qgn4hl',
'http://prnt.sc/qgnv95',
'http://prnt.sc/qgnxx9',
'http://prnt.sc/qgnvaa',
'http://prnt.sc/qgn6x8',
'http://prnt.sc/qgnhxw',
'http://prnt.sc/qgnzmb',
'http://prnt.sc/qgn9ab',
'http://prnt.sc/qgn8bl',
'http://prnt.sc/qgnjne',
'http://prnt.sc/qgnzui',
'http://prnt.sc/qgn3dh',
'http://prnt.sc/qgndx6',
'http://prnt.sc/qgnd05',
'http://prnt.sc/qgns50',
'http://prnt.sc/qgnahb',
'http://prnt.sc/qgnqgp',
'http://prnt.sc/qgns9m',
'http://prnt.sc/qgn70y',
'http://prnt.sc/qgnhs0',
'http://prnt.sc/qgnq6o',
'http://prnt.sc/qgnl5j',
'http://prnt.sc/qgn5i5',
'http://prnt.sc/qgnf95',
'http://prnt.sc/qgnslu',
'http://prnt.sc/qgnazw',
'http://prnt.sc/qgnss6',
'http://prnt.sc/qgnge0',
'http://prnt.sc/qgnkyi',
'http://prnt.sc/qgnnnr',
'http://prnt.sc/qgnan3',
'http://prnt.sc/qgnplu',
'http://prnt.sc/qgnntq',
'http://prnt.sc/qgnk7v',
'http://prnt.sc/qgnj9r',
'http://prnt.sc/qgnqxd',
'http://prnt.sc/qgnnep',
'http://prnt.sc/qgntg0',
'http://prnt.sc/qgnd68',
'http://prnt.sc/qgnf4i',
'http://prnt.sc/qgngct',
'http://prnt.sc/qgneff',
'http://prnt.sc/qgnje2',
'http://prnt.sc/qgnh1d',
'http://prnt.sc/qgn7c0',
'http://prnt.sc/qgnbq9',
'http://prnt.sc/qgn7my',
'http://prnt.sc/qgnbf3',
'http://prnt.sc/qgndct',
'http://prnt.sc/qgnf6w',
'http://prnt.sc/qgn7oo',
'http://prnt.sc/qgn396',
'http://prnt.sc/qgnwx1',
'http://prnt.sc/qgn0jq',
'http://prnt.sc/qgn9pk',
'http://prnt.sc/qgncqu',
'http://prnt.sc/qgn2r9',
'http://prnt.sc/qgnrl3',
'http://prnt.sc/qgnwod',
'http://prnt.sc/qgn3vx',
'http://prnt.sc/qgnn0s',
'http://prnt.sc/qgnurb',
'http://prnt.sc/qgnhdy',
'http://prnt.sc/qgnlgm',
'http://prnt.sc/qgn33y',
'http://prnt.sc/qgn0ny',
'http://prnt.sc/qgnapy',
'http://prnt.sc/qgnp6f',
'http://prnt.sc/qgn6g6',
'http://prnt.sc/qgnk05',
'http://prnt.sc/qgnh8h',
'http://prnt.sc/qgnbx2',
'http://prnt.sc/qgnp78',
'http://prnt.sc/qgnx4s',
'http://prnt.sc/qgnhx3',
'http://prnt.sc/qgn6fy',
'http://prnt.sc/qgnjl0',
'http://prnt.sc/qgn35i',
'http://prnt.sc/qgnxkf',
'http://prnt.sc/qgnjsk',
'http://prnt.sc/qgnpd7',
'http://prnt.sc/qgnodi',
'http://prnt.sc/qgn3e5',
'http://prnt.sc/qgnl0u',
'http://prnt.sc/qgnpa3',
'http://prnt.sc/qgn0ss',
'http://prnt.sc/qgn6hg',
'http://prnt.sc/qgnssf',
'http://prnt.sc/qgnivp',
'http://prnt.sc/qgn337',
'http://prnt.sc/qgng0g',
'http://prnt.sc/qgnabb',
'http://prnt.sc/qgnlvt',
'http://prnt.sc/qgnlaz',
'http://prnt.sc/qgnplg',
'http://prnt.sc/qgn4t6',
'http://prnt.sc/qgnt73',
'http://prnt.sc/qgn5bk',
'http://prnt.sc/qgnfby',
'http://prnt.sc/qgnp3x',
'http://prnt.sc/qgndso',
'http://prnt.sc/qgncqb',
'http://prnt.sc/qgnghs',
'http://prnt.sc/qgnxqa',
'http://prnt.sc/qgnhlh',
'http://prnt.sc/qgnz1w',
'http://prnt.sc/qgnlwt',
'http://prnt.sc/qgne5x',
'http://prnt.sc/qgni20',
'http://prnt.sc/qgnqpy',
'http://prnt.sc/qgndmx',
'http://prnt.sc/qgnbpc',
'http://prnt.sc/qgny9r',
'http://prnt.sc/qgnw7l',
'http://prnt.sc/qgnq81',
'http://prnt.sc/qgnt4q',
'http://prnt.sc/qgnd5l',
'http://prnt.sc/qgn5wb',
'http://prnt.sc/qgn6b6',
'http://prnt.sc/qgnau1',
'http://prnt.sc/qgn6jq',
'http://prnt.sc/qgn9fy',
'http://prnt.sc/qgnc72',
'http://prnt.sc/qgnde2',
'http://prnt.sc/qgn2sy',
'http://prnt.sc/qgnyvg',
'http://prnt.sc/qgn4uv',
'http://prnt.sc/qgncc6',
'http://prnt.sc/qgnjhu',
'http://prnt.sc/qgnyta',
'http://prnt.sc/qgnzr8',
'http://prnt.sc/qgnqsl',
'http://prnt.sc/qgnbmx',
'http://prnt.sc/qgn9d6',
'http://prnt.sc/qgny62',
'http://prnt.sc/qgne2v',
'http://prnt.sc/qgnyzw',
'http://prnt.sc/qgnyf3',
'http://prnt.sc/qgnqo8',
'http://prnt.sc/qgnwyq',
'http://prnt.sc/qgnsig',
'http://prnt.sc/qgn65l',
'http://prnt.sc/qgnnhj',
'http://prnt.sc/qgndpg',
'http://prnt.sc/qgn5n7',
'http://prnt.sc/qgnzoz',
'http://prnt.sc/qgnal7',
'http://prnt.sc/qgn1kk',
'http://prnt.sc/qgn9cz',
'http://prnt.sc/qgn2ea',
'http://prnt.sc/qgnm8q',
'http://prnt.sc/qgn6mu',
'http://prnt.sc/qgn0pk',
'http://prnt.sc/qgnq29',
'http://prnt.sc/qgnbuh',
'http://prnt.sc/qgnscl',
'http://prnt.sc/qgnu2b',
'http://prnt.sc/qgnu7y',
'http://prnt.sc/qgni62',
'http://prnt.sc/qgnrbt',
'http://prnt.sc/qgnz71',
'http://prnt.sc/qgnu5q',
'http://prnt.sc/qgnr0z',
'http://prnt.sc/qgn74s',
'http://prnt.sc/qgnfe5',
'http://prnt.sc/qgnaog',
'http://prnt.sc/qgn16w',
'http://prnt.sc/qgnfq8',
'http://prnt.sc/qgn94v',
'http://prnt.sc/qgno6k',
'http://prnt.sc/qgnynj',
'http://prnt.sc/qgn7pd',
'http://prnt.sc/qgno80',
'http://prnt.sc/qgna5j',
'http://prnt.sc/qgnllj',
'http://prnt.sc/qgn34p',
'http://prnt.sc/qgne5t',
'http://prnt.sc/qgny7z',
'http://prnt.sc/qgng3v',
'http://prnt.sc/qgnhvs',
'http://prnt.sc/qgnrsf',
'http://prnt.sc/qgn4e5',
'http://prnt.sc/qgnkke',
'http://prnt.sc/qgntcs',
'http://prnt.sc/qgn4gs',
'http://prnt.sc/qgnhe7',
'http://prnt.sc/qgn8mw',
'http://prnt.sc/qgn4we',
'http://prnt.sc/qgniaq',
'http://prnt.sc/qgn461',
'http://prnt.sc/qgndc4',
'http://prnt.sc/qgn717',
'http://prnt.sc/qgnj7a',
'http://prnt.sc/qgnuck',
'http://prnt.sc/qgn0iv',
'http://prnt.sc/qgn5hj',
'http://prnt.sc/qgnhcb',
'http://prnt.sc/qgnnf1',
'http://prnt.sc/qgn3no',
'http://prnt.sc/qgnhom',
'http://prnt.sc/qgnb9g',
'http://prnt.sc/qgnrw8',
'http://prnt.sc/qgnvmi',
'http://prnt.sc/qgnrgy',
'http://prnt.sc/qgn0nf',
'http://prnt.sc/qgniqg',
'http://prnt.sc/qgnlmo',
'http://prnt.sc/qgnj4b',
'http://prnt.sc/qgnoc7',
'http://prnt.sc/qgnnv0',
'http://prnt.sc/qgnvo5',
'http://prnt.sc/qgnt1k',
'http://prnt.sc/qgne1m',
'http://prnt.sc/qgnzs8',
'http://prnt.sc/qgnhf8',
'http://prnt.sc/qgnixd',
'http://prnt.sc/qgnrx5',
'http://prnt.sc/qgnzlc',
'http://prnt.sc/qgnuxk',
'http://prnt.sc/qgni79',
'http://prnt.sc/qgnl4i',
'http://prnt.sc/qgn7ig',
'http://prnt.sc/qgng2f',
'http://prnt.sc/qgn6y4',
'http://prnt.sc/qgnywg',
'http://prnt.sc/qgne69',
'http://prnt.sc/qgnpy0',
'http://prnt.sc/qgn2sh',
'http://prnt.sc/qgnejg',
'http://prnt.sc/qgn08u',
'http://prnt.sc/qgnqj1',
'http://prnt.sc/qgneoq',
'http://prnt.sc/qgncc1',
'http://prnt.sc/qgng7t',
'http://prnt.sc/qgnvt8',
'http://prnt.sc/qgn6li',
'http://prnt.sc/qgngz1',
'http://prnt.sc/qgnskv',
'http://prnt.sc/qgnt7m',
'http://prnt.sc/qgn4p8',
'http://prnt.sc/qgn4xb',
'http://prnt.sc/qgnqte',
'http://prnt.sc/qgnoh3',
'http://prnt.sc/qgna09',
'http://prnt.sc/qgntsm',
'http://prnt.sc/qgnt0d',
'http://prnt.sc/qgnrr2',
'http://prnt.sc/qgne24',
'http://prnt.sc/qgnnk5',
'http://prnt.sc/qgne0h',
'http://prnt.sc/qgnila',
'http://prnt.sc/qgnjhh',
'http://prnt.sc/qgnzbc',
'http://prnt.sc/qgnr1a',
'http://prnt.sc/qgnpr2',
'http://prnt.sc/qgng4p',
'http://prnt.sc/qgnqnx',
'http://prnt.sc/qgnxgy',
'http://prnt.sc/qgn7zu',
'http://prnt.sc/qgnejh',
'http://prnt.sc/qgnxhl',
'http://prnt.sc/qgnytx',
'http://prnt.sc/qgn0lp',
'http://prnt.sc/qgnlao',
'http://prnt.sc/qgnv6e',
'http://prnt.sc/qgnb9r',
'http://prnt.sc/qgn94e',
'http://prnt.sc/qgnm3y',
'http://prnt.sc/qgnyzm',
'http://prnt.sc/qgn0me',
'http://prnt.sc/qgn74q',
'http://prnt.sc/qgn5yf',
'http://prnt.sc/qgnd1z',
'http://prnt.sc/qgng3p',
'http://prnt.sc/qgnmdo',
'http://prnt.sc/qgn9dh',
'http://prnt.sc/qgnihc',
'http://prnt.sc/qgnhsk',
'http://prnt.sc/qgnsn4',
'http://prnt.sc/qgnwv8',
'http://prnt.sc/qgn4em',
'http://prnt.sc/qgnalp',
'http://prnt.sc/qgnsra',
'http://prnt.sc/qgn85g',
'http://prnt.sc/qgntt0',
'http://prnt.sc/qgnvuq',
'http://prnt.sc/qgn61h',
'http://prnt.sc/qgnuam',
'http://prnt.sc/qgnrxn',
'http://prnt.sc/qgntiq',
'http://prnt.sc/qgnlxx',
'http://prnt.sc/qgnf98',
'http://prnt.sc/qgnt62',
'http://prnt.sc/qgnjul',
'http://prnt.sc/qgnx4j',
'http://prnt.sc/qgnazj',
'http://prnt.sc/qgn6od',
'http://prnt.sc/qgng61',
'http://prnt.sc/qgnkpw',
'http://prnt.sc/qgnird',
'http://prnt.sc/qgnwhu',
'http://prnt.sc/qgn66l',
'http://prnt.sc/qgnbx5',
'http://prnt.sc/qgnq26',
'http://prnt.sc/qgnum9',
'http://prnt.sc/qgn7f0',
'http://prnt.sc/qgnrtd',
'http://prnt.sc/qgntco',
'http://prnt.sc/qgnteg',
'http://prnt.sc/qgnudo',
'http://prnt.sc/qgnn0f',
'http://prnt.sc/qgndos',
'http://prnt.sc/qgnyez',
'http://prnt.sc/qgnxmv',
'http://prnt.sc/qgn8px',
'http://prnt.sc/qgnmes',
'http://prnt.sc/qgndbi',
'http://prnt.sc/qgn3ea',
'http://prnt.sc/qgnmn5',
'http://prnt.sc/qgnzp9',
'http://prnt.sc/qgnl79',
'http://prnt.sc/qgnkis',
'http://prnt.sc/qgnih0',
'http://prnt.sc/qgn76p',
'http://prnt.sc/qgnp1z',
'http://prnt.sc/qgn2g6',
'http://prnt.sc/qgn5io',
'http://prnt.sc/qgnqim',
'http://prnt.sc/qgn624',
'http://prnt.sc/qgn0u0',
'http://prnt.sc/qgn1yr',
'http://prnt.sc/qgnj2o',
'http://prnt.sc/qgntos',
'http://prnt.sc/qgn7pj',
'http://prnt.sc/qgnxf1',
'http://prnt.sc/qgnt8s',
'http://prnt.sc/qgn08x',
'http://prnt.sc/qgn66e',
'http://prnt.sc/qgnj6a',
'http://prnt.sc/qgnhh4',
'http://prnt.sc/qgnb67',
'http://prnt.sc/qgn7s9',
'http://prnt.sc/qgnwci',
'http://prnt.sc/qgn8rf',
'http://prnt.sc/qgnufj',
'http://prnt.sc/qgn7aw',
'http://prnt.sc/qgnxui',
'http://prnt.sc/qgnc6d',
'http://prnt.sc/qgnny6',
'http://prnt.sc/qgnyha',
'http://prnt.sc/qgnyfs',
'http://prnt.sc/qgn3yy',
'http://prnt.sc/qgnb8n',
'http://prnt.sc/qgnozp',
'http://prnt.sc/qgnskb',
'http://prnt.sc/qgnbya',
'http://prnt.sc/qgn6xb',
'http://prnt.sc/qgnf62',
'http://prnt.sc/qgn2ad',
'http://prnt.sc/qgnu8f',
'http://prnt.sc/qgneq6',
'http://prnt.sc/qgngg6',
'http://prnt.sc/qgnzz4',
'http://prnt.sc/qgn7jc',
'http://prnt.sc/qgn339',
'http://prnt.sc/qgn6cy',
'http://prnt.sc/qgngp8',
'http://prnt.sc/qgnqas',
'http://prnt.sc/qgniwy',
'http://prnt.sc/qgnxkb',
'http://prnt.sc/qgnb72',
'http://prnt.sc/qgnak3',
'http://prnt.sc/qgnsgp',
'http://prnt.sc/qgnqfo',
'http://prnt.sc/qgnako',
'http://prnt.sc/qgn65u',
'http://prnt.sc/qgn6rf',
'http://prnt.sc/qgntjn',
'http://prnt.sc/qgnbu8',
'http://prnt.sc/qgn6jf',
'http://prnt.sc/qgnzms',
'http://prnt.sc/qgnf3f',
'http://prnt.sc/qgn3we',
'http://prnt.sc/qgnfk0',
'http://prnt.sc/qgnew5',
'http://prnt.sc/qgnn1z',
'http://prnt.sc/qgnhpt',
'http://prnt.sc/qgnt0m',
'http://prnt.sc/qgn2rc',
'http://prnt.sc/qgn18w',
'http://prnt.sc/qgnu6t',
'http://prnt.sc/qgnkms',
'http://prnt.sc/qgntrf',
'http://prnt.sc/qgnwyl',
'http://prnt.sc/qgn4bg',
'http://prnt.sc/qgnhhn',
'http://prnt.sc/qgnh7u',
'http://prnt.sc/qgnjyt',
'http://prnt.sc/qgnups',
'http://prnt.sc/qgnpzp',
'http://prnt.sc/qgn1hd',
'http://prnt.sc/qgno3o',
'http://prnt.sc/qgn0sh',
'http://prnt.sc/qgnk9f',
'http://prnt.sc/qgnfjb',
'http://prnt.sc/qgnp8z',
'http://prnt.sc/qgnnaq',
'http://prnt.sc/qgnhtr',
'http://prnt.sc/qgn916',
'http://prnt.sc/qgnn13',
'http://prnt.sc/qgndvd',
'http://prnt.sc/qgne8q',
'http://prnt.sc/qgn7f5',
'http://prnt.sc/qgnn9g',
'http://prnt.sc/qgnwdb',
'http://prnt.sc/qgn27c',
'http://prnt.sc/qgnrfd',
'http://prnt.sc/qgn4w3', ]
 
  if ctx.channel.is_nsfw():
   await ctx.send(f'\n{random.choice(responses)}')
  
  else:
   await ctx.send('Please use this command in an NSFW channel.')

    


 













  









  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)












