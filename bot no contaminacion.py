import random, os
import discord
from model import get_class

# La variable intents almacena los privilegios del bot

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')


    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def tips(ctx):
    await ctx.send(f'Tips para evitar la contaminacion: ')
    T=['reciclar','no tirar basura','colaborar con centros comunitarios de reciclaje','utiliza el transporte publico','reduce el consumo de plásticos']
    tip = random.choice(T)
    await ctx.send(tip)

@bot.command()
async def mem(ctx):

    image = random.choice(os.listdir("images"))

    with open(f'images/{image}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Imagen guardada en ./{file_url}")
            try: 
                clase = get_class(model_path = "keras_model.h5", labels_path = "labels.txt", image_path = f"./{file_name}"  )
                if clase[0] == "Palomas":
                    await ctx.send("Es posiblemente una paloma paloma, pueden comer todo tipo de granos como trigo")
                elif clase[0] == "Gorriones":
                    await ctx.send("Es posiblemente un gorrión, pueden comer todo tipo de granos como arroz")
            
            except:
                await ctx.send("Ha ocurrido un error, intentalo de nuevo please :C")
    else:
        await ctx.send("No subiste una imagen :(")
        

bot.run("Token")
