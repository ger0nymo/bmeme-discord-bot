#color='0x062a4c'
import discord
import requests
import random
import re
from discord.ext import commands
from bs4 import BeautifulSoup

file_bme = open('meme-urls/bmeme_urls_all.txt')
file_vik = open('meme-urls/bmeme_urls_vik.txt')

memes_bme = [line.rstrip() for line in file_bme]
memes_vik = [line.rstrip() for line in file_vik]


client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def bmeme(ctx, args = None): #args lehet majd VIK vagy BME
    title, description, url = '', '', ''
    if args == None or str(args).lower() == 'bme':
        n = random.randint(0, len(memes_bme) - 1)
        url = memes_bme[n]
    elif str(args).lower() == 'vik':
        n = random.randint(0, len(memes_vik) - 1)
        url = memes_vik[n]
    else:
        await ctx.send('Ismeretlen paraméter.\n!bmeme parancs után választható kategóriák: bme (általános mémek) vagy vik (vikes mémek)')
        return

    meme_id = url[35:].split('_')[0]

    page_url = f'https://www.bmeme.hu/post/{meme_id}'
    html_doc = requests.get(page_url).content
    soup = BeautifulSoup(html_doc, 'html.parser')

    title = soup.find('div', class_='post_head').find('h2').string
    author = soup.find('div', class_='post_head').find('ul').find_all('li')[1].text

    new_embed = discord.Embed(title=title,
                          description=description,
                           color=0x062a4c)
    new_embed.set_author(name=f'Beküldő: {author}')
    new_embed.set_image(url=url)
    new_embed.set_footer(text=f'Azonosító: {meme_id}')
    await ctx.send(embed=new_embed)

client.run('token')