import discord
from discord.ext import commands
import requests
import json


TOKEN = 'Your Bot Token Here'


client = commands.Bot(command_prefix='#')


@client.event
async def on_ready():
    print('Bot Is Ready!')


def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    json_data = json.loads(response.text)
    adv = json_data['slip']['advice']
    return (adv)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.command()
async def advice(ctx):
    adv = get_advice()
    await ctx.send(adv)


@client.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

client.run(TOKEN)
