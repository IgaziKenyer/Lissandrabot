#Lissandra by IgaziKenyer

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import json
import os

bot = commands.Bot(command_prefix=">")
#api_adress = "http://api.openweathermap.org/data/2.5/appid=a677e1f4b9195e2b3437318ea0473e74&q="
#city = input("City Name:")
#url = api_adress + city
#json_data = requests.get(url).json()
#formated_data = json_data['weather'][0]['main']
#print(json_data)
print(discord.__version__)
@bot.command(pass_context=True)
async def Csitenno(ctx):
    #Cambiar la id para otra ciudad
    #Sitenno = Ciudad de Guayana, Venezuela
    #Kamikune = Hangzhou, China
    #Shinko = Chongqing, China
    #Reino del Sur = Santiago, Chile
    #Gigaran =
    #Rhyn = Facativa, Colombia
    #Krouzen = Bern
    #Roudesh = Munich, Germany
    #Jungla de las Pestes = Manaus, Brazil
    api_adress = str(os.environ(['RIOT_KEY']))
    data= requests.get(api_adress)
    read= data.json()
    
    
    #await bot.say ("Sitenno ")
   # await bot.say ("El clima actual es de {}".format(read['list'][0]['weather'][0]["description"]))
    icon = read["list"][0]["weather"][0]["icon"]
    #01d/01n Soleado
    #02d/02n algunas nubes :partly_sunny:
    #03d/03n nubes esparcidas :white_sun_cloud:
    #04d/04n nubes rotas :cloud:
    #09d/09n Llovisna :white_sun_rain_cloud: 
    #010d/10n Lluvioso :cloud_rain:
    #011d/11n Tormenta de Rayos :thunder_cloud_rain:
    #13d/13n Nieve :cloud_snow:
    #50d/50n Neblina :fog:
    if icon in ['01d', '02n']:
        icono = (":sunny:")
        await bot.say (":sunny:")
    elif icon in ['02d', '02n']:
        await bot.say (":partly_sunny:")
        icono = (":partly_sunny:")
    elif icon in ['03d', '03n']:
        await bot.say (":white_sun_cloud:")
        icono = (":white_sun_cloud:")
    elif icon in ['04d', '04n']:
        await bot.say (":cloud:")
        icono = (":cloud:")
    elif icon in ['09d', '09n']:
        await bot.say (":white_sun_rain_cloud:")
        icono = (":white_sun_rain_cloud:")
    elif icon in ['10d', '10n']:
        await bot.say (":cloud_rain: ")
        icono = (":cloud_rain: ")
    elif icon in ['11d', '11n']:
        await bot.say (":thunder_cloud_rain:")
        icono = (":thunder_cloud_rain:")
    elif icon in ['13d', '13n']:
        await bot.say (":cloud_snow:")
        icono = (":cloud_snow:")
    elif icon in ['50d', '50n']:
        await bot.say (":fog:")
        icono = (":fog")
    #await bot.say ("La temperatura actual es de {}°C".format(read['list'][0]['main']["temp"]))
    #await bot.say ("La minima y maxima para hoy seran {}°C".format(read['list'][0]["main"]["temp_min"]))
    #await bot.say ("h{}°C".format(read['list'][0]["main"]["temp_max"])) 
    #Tempamin = read['list'][0]['main']["temp_min"]
    #Tempamax = read['list'][0]['main']["temp_max"]
    #Temp_maxmin = Tempamin, "/", Tempamax
    #Humedad
    #await bot.say ("Con una humedad de {}%".format(read['list'][0]["main"]["humidity"]))
    #embed = discord.Embed(title="Clima", description= "En la ciudad de Sitenno el Clima actual es") 
    #embed.add_field(name="icon", value=(read['list'][0]['weather'][0]["description"])
    #await bot.say(embed=embed)
    embed = discord.Embed(title="Clima de Sitenno", description= "")
    embed.add_field(name="En la ciudad de Sitenno el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
    embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
    embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
    embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
    embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
    embed.set_thumbnail(url="https://i.imgur.com/heRUwq4.jpg")
    embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
    await bot.say( embed=embed)

@bot.command(pass_context=True)
async def Ckamikune(ctx):
    api_adress = str(os.environ(['RIOT_KEY']))
    data= requests.get(api_adress)
    read= data.json()
    icon = read["list"][0]["weather"][0]["icon"]
    
    if icon in ['01d', '01n']:
        icono = (":sunny:")
        await bot.say (":sunny:")
    elif icon in ['02d', '02n']:
        await bot.say (":partly_sunny:")
        icono = (":partly_sunny:")
    elif icon in ['03d', '03n']:
        await bot.say (":white_sun_cloud:")
        icono = (":white_sun_cloud:")
    elif icon in ['04d', '04n']:
        await bot.say (":cloud:")
        icono = (":cloud:")
    elif icon in ['09d', '09n']:
        await bot.say (":white_sun_rain_cloud:")
        icono = (":white_sun_rain_cloud:")
    elif icon in ['10d', '10n']:
        await bot.say (":cloud_rain: ")
        icono = (":cloud_rain: ")
    elif icon in ['11d', '11n']:
        await bot.say (":thunder_cloud_rain:")
        icono = (":thunder_cloud_rain:")
    elif icon in ['13d', '13n']:
        await bot.say (":cloud_snow:")
        icono = (":cloud_snow:")
    elif icon in ['50d', '50n']:
        await bot.say (":fog:")
        icono = (":fog")
    embed = discord.Embed(title="Clima de Kamikune", description= "")
    embed.add_field(name="En la ciudad de Kamikune el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
    embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
    embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
    embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
    embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
    embed.set_thumbnail(url="https://i.imgur.com/uHPfcbo.jpg")
    embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
    await bot.say( embed=embed)
    print (icon)
    print (icono)

@bot.command(pass_context=True)
async def Cshinko(ctx):
    api_adress = str(os.environ(['RIOT_KEY']))
    data= requests.get(api_adress)
    read= data.json()
    icon = read["list"][0]["weather"][0]["icon"]
    
    if icon in ['01d', '01n']:
        icono = (":sunny:")
        await bot.say (":sunny:")
    elif icon in ['02d', '02n']:
        await bot.say (":partly_sunny:")
        icono = (":partly_sunny:")
    elif icon in ['03d', '03n']:
        await bot.say (":white_sun_cloud:")
        icono = (":white_sun_cloud:")
    elif icon in ['04d', '04n']:
        await bot.say (":cloud:")
        icono = (":cloud:")
    elif icon in ['09d', '09n']:
        await bot.say (":white_sun_rain_cloud:")
        icono = (":white_sun_rain_cloud:")
    elif icon in ['10d', '10n']:
        await bot.say (":cloud_rain: ")
        icono = (":cloud_rain: ")
    elif icon in ['11d', '11n']:
        await bot.say (":thunder_cloud_rain:")
        icono = (":thunder_cloud_rain:")
    elif icon in ['13d', '13n']:
        await bot.say (":cloud_snow:")
        icono = (":cloud_snow:")
    elif icon in ['50d', '50n']:
        await bot.say (":fog:")
        icono = (":fog")
    embed = discord.Embed(title="Clima de Shinko", description= "")
    embed.add_field(name="En la ciudad de Shinko el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
    embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
    embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
    embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
    embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
    embed.set_thumbnail(url="https://i.imgur.com/Qg12qfs.jpg")
    embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
    await bot.say( embed=embed)
    print (icon)
    print (icono)

@bot.command(pass_context=True)
async def c(ctx,arg):
    if arg == "sitenno":
        api_adress = str(os.environ(['RIOT_KEY']))
        data= requests.get(api_adress)
        read= data.json()
        icon = read["list"][0]["weather"][0]["icon"]
        if icon in ['01d', '02n']:
            icono = (":sunny:")
            await bot.say (":sunny:")
        elif icon in ['02d', '02n']:
            await bot.say (":partly_sunny:")
            icono = (":partly_sunny:")
        elif icon in ['03d', '03n']:
            await bot.say (":white_sun_cloud:")
            icono = (":white_sun_cloud:")
        elif icon in ['04d', '04n']:
            await bot.say (":cloud:")
            icono = (":cloud:")
        elif icon in ['09d', '09n']:
            await bot.say (":white_sun_rain_cloud:")
            icono = (":white_sun_rain_cloud:")
        elif icon in ['10d', '10n']:
            await bot.say (":cloud_rain: ")
            icono = (":cloud_rain: ")
        elif icon in ['11d', '11n']:
            await bot.say (":thunder_cloud_rain:")
            icono = (":thunder_cloud_rain:")
        elif icon in ['13d', '13n']:
            await bot.say (":cloud_snow:")
            icono = (":cloud_snow:")
        elif icon in ['50d', '50n']:
            await bot.say (":fog:")
            icono = (":fog")
        embed = discord.Embed(title="Clima de Sitenno", description= "")
        embed.add_field(name="En la ciudad de Sitenno el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
        embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
        embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
        embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
        embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
        embed.set_thumbnail(url="https://i.imgur.com/heRUwq4.jpg")
        embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
        await bot.say( embed=embed)
    elif arg == "kamikune":
        api_adress = str(os.environ(['RIOT_KEY']))
        data= requests.get(api_adress)
        read= data.json()
        icon = read["list"][0]["weather"][0]["icon"]
        if icon in ['01d', '02n']:
            icono = (":sunny:")
            await bot.say (":sunny:")
        elif icon in ['02d', '02n']:
            await bot.say (":partly_sunny:")
            icono = (":partly_sunny:")
        elif icon in ['03d', '03n']:
            await bot.say (":white_sun_cloud:")
            icono = (":white_sun_cloud:")
        elif icon in ['04d', '04n']:
            await bot.say (":cloud:")
            icono = (":cloud:")
        elif icon in ['09d', '09n']:
            await bot.say (":white_sun_rain_cloud:")
            icono = (":white_sun_rain_cloud:")
        elif icon in ['10d', '10n']:
            await bot.say (":cloud_rain: ")
            icono = (":cloud_rain: ")
        elif icon in ['11d', '11n']:
            await bot.say (":thunder_cloud_rain:")
            icono = (":thunder_cloud_rain:")
        elif icon in ['13d', '13n']:
            await bot.say (":cloud_snow:")
            icono = (":cloud_snow:")
        elif icon in ['50d', '50n']:
            await bot.say (":fog:")
            icono = (":fog")
        embed = discord.Embed(title="Clima de Kamikune", description= "")
        embed.add_field(name="En la ciudad de Kamikune el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
        embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
        embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
        embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
        embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
        embed.set_thumbnail(url="https://i.imgur.com/uHPfcbo.jpg")
        embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
        await bot.say( embed=embed)
    elif arg == "shinko":
        api_adress = str(os.environ(['RIOT_KEY']))
        data= requests.get(api_adress)
        read= data.json()
        icon = read["list"][0]["weather"][0]["icon"]
        if icon in ['01d', '02n']:
            icono = (":sunny:")
            await bot.say (":sunny:")
        elif icon in ['02d', '02n']:
            await bot.say (":partly_sunny:")
            icono = (":partly_sunny:")
        elif icon in ['03d', '03n']:
            await bot.say (":white_sun_cloud:")
            icono = (":white_sun_cloud:")
        elif icon in ['04d', '04n']:
            await bot.say (":cloud:")
            icono = (":cloud:")
        elif icon in ['09d', '09n']:
            await bot.say (":white_sun_rain_cloud:")
            icono = (":white_sun_rain_cloud:")
        elif icon in ['10d', '10n']:
            await bot.say (":cloud_rain: ")
            icono = (":cloud_rain: ")
        elif icon in ['11d', '11n']:
            await bot.say (":thunder_cloud_rain:")
            icono = (":thunder_cloud_rain:")
        elif icon in ['13d', '13n']:
            await bot.say (":cloud_snow:")
            icono = (":cloud_snow:")
        elif icon in ['50d', '50n']:
            await bot.say (":fog:")
            icono = (":fog")
        embed = discord.Embed(title="Clima de Shinko", description= "")
        embed.add_field(name="En la ciudad de Shinko el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
        embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
        embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
        embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
        embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
        embed.set_thumbnail(url="https://i.imgur.com/Qg12qfs.jpg")
        embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
        await bot.say( embed=embed)
    elif arg == "krouzen":
        api_adress = str(os.environ(['RIOT_KEY']))
        data= requests.get(api_adress)
        read= data.json()
        icon = read["list"][0]["weather"][0]["icon"]
    
        if icon in ['01d', '01n']:
            icono = (":sunny:")
            await bot.say (":sunny:")
        elif icon in ['02d', '02n']:
            await bot.say (":partly_sunny:")
            icono = (":partly_sunny:")
        elif icon in ['03d', '03n']:
            await bot.say (":white_sun_cloud:")
            icono = (":white_sun_cloud:")
        elif icon in ['04d', '04n']:
            await bot.say (":cloud:")
            icono = (":cloud:")
        elif icon in ['09d', '09n']:
            await bot.say (":white_sun_rain_cloud:")
            icono = (":white_sun_rain_cloud:")
        elif icon in ['10d', '10n']:
            await bot.say (":cloud_rain: ")
            icono = (":cloud_rain: ")
        elif icon in ['11d', '11n']:
            await bot.say (":thunder_cloud_rain:")
            icono = (":thunder_cloud_rain:")
        elif icon in ['13d', '13n']:
            await bot.say (":cloud_snow:")
            icono = (":cloud_snow:")
        elif icon in ['50d', '50n']:
            await bot.say (":fog:")
            icono = (":fog")
        embed = discord.Embed(title="Clima de Krouzen", description= "")
        embed.add_field(name="En la ciudad de Krouzen el Clima actual es", value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
        embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
        embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
        embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
        embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
        embed.set_thumbnail(url="https://i.imgur.com/4Qgz6G5.jpg")
        embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
        await bot.say( embed=embed)
        print (icon)
        print (icono)
    else: # Para Ubicaciones del mundo real
        api_adress = str(os.environ(['RIOT_KEY']))
        data= requests.get(api_adress)
        read= data.json()
        icon = read["list"][0]["weather"][0]["icon"]
        if icon in ['01d', '01n']:
            icono = (":sunny:")
            await bot.say (":sunny:")
        elif icon in ['02d', '02n']:
            await bot.say (":partly_sunny:")
            icono = (":partly_sunny:")
        elif icon in ['03d', '03n']:
            await bot.say (":white_sun_cloud:")
            icono = (":white_sun_cloud:")
        elif icon in ['04d', '04n']:
            await bot.say (":cloud:")
            icono = (":cloud:")
        elif icon in ['09d', '09n']:
            await bot.say (":white_sun_rain_cloud:")
            icono = (":white_sun_rain_cloud:")
        elif icon in ['10d', '10n']:
            await bot.say (":cloud_rain: ")
            icono = (":cloud_rain: ")
        elif icon in ['11d', '11n']:
            await bot.say (":thunder_cloud_rain:")
            icono = (":thunder_cloud_rain:")
        elif icon in ['13d', '13n']:
            await bot.say (":cloud_snow:")
            icono = (":cloud_snow:")
        elif icon in ['50d', '50n']:
            await bot.say (":fog:")
            icono = (":fog")
        embed = discord.Embed(title="Clima de {}".format(arg), description= "")
        embed.add_field(name="En la ciudad de {} el Clima actual es".format(arg), value=icono + "{}".format(read['list'][0]['weather'][0]["description"]), inline=True)
        embed.add_field(name="La Temperatura actual es de", value = "{}°C :thermometer:".format(read['list'][0]['main']["temp"]), inline=True)
        embed.add_field(name="La humedad es de", value="{}%:droplet:".format(read['list'][0]["main"]["humidity"]), inline=True)
        embed.add_field(name="La maxima sera de", value="{}°C:arrow_up:".format(read['list'][0]["main"]["temp_max"]))
        embed.add_field(name="La minima sera de", value="{}°C:arrow_down_small:".format(read['list'][0]["main"]["temp_min"]))
        #embed.set_thumbnail(url="https://i.imgur.com/4Qgz6G5.jpg")
        embed.set_footer(text="Informacion recopilada por el gremio de aventureros")
        await bot.say( embed=embed)
        await bot.say(arg)
        await ctx.send(arg)


@bot.event
async def on_ready():
    print ("Bienvenido al gremio de aventureros")
    print ("i am running on" + bot.user.name)
    print("with the ID" + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping pong!")
    print ("Usuario uso ping!")
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{} info".format(user.name), description="Esta es la informacion que tenemos en nuestros archivos.", color=0x00f00)
    embed.add_field(name="Nombre", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Estado", value=user.status, inline=True)
    embed.add_field(name="Rol mas alto", value=user.top_role, inline=True)
    embed.add_field(name="Se unio el dia", value=user.joined_at, inline=True)
    imageURL = "https://imgur.com/a/XJMZLP9"
    embed.set_image(url=imageURL)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="Recepcionista del Gremio", color=0x00ff00)
    embed.set_footer(text="this is the footer")
    embed.set_author(name="Igazi Kenyer")
    embed.add_field(name="This is a field", value="no, it isnt", inline=True)
    await bot.say(embed=embed)
bot.run(os.environ['BOT_TOKEN'])
