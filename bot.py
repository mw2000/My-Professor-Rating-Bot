import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from bs4 import BeautifulSoup as bs

import requests
import sys


def prof(url):
    r  = requests.get("http://www.ratemyprofessors.com/search.jsp?query=" +url)

    data = r.text

    soup = bs(data, "html.parser")

    profs=soup.find_all("li",class_="listing PROFESSOR")

    l= profs[0].find_all('a')[0]['href']
    name = profs[0].find_all('span',class_="main")[0].text
    dep = profs[0].find_all('span',class_="sub")[0].text
    r  = requests.get("http://www.ratemyprofessors.com/" +l)


    data = r.text

    soup = bs(data, "html.parser")
    rat=soup.find_all("div",class_="grade")[0].text

    return {'name':name, 'dep':dep, 'rat':rat}

Client = discord.Client()
client = commands.Bot(command_prefix = "#")


@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith("!prof"):
        args = message.content.split(" ")
        prof_name = " ".join(args[1:])
        data = prof(prof_name)
        await client.send_message(message.channel, "**Name: " + data['name'] + "\nRating: " + data['rat'] + " \nDepartment: " + data['dep'] + "**")
    

client.run("NDU3ODU3MDgxNjMwOTE2NjE4.DgfNIA.MQo09XxLPSJ498XheB9oP-k4Vxs")