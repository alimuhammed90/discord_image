
import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot giriş yaptı: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(attachment.filename)

           
            result_class = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=attachment.filename
            )

            
            food_messages = {
                "fast food": " Yiyeceklerin çok kalorili, daha sağlıklı şeyler tüketmelisin.",
                "healthy food": " Evet böyle devam et! Çok sağlıklı besleniyorsun.",
                
            }

            message = food_messages.get(
                result_class.lower(),
                " Bu yiyecek hakkında net bir yorum yapamadım."
            )

            await ctx.send(f" Tespit edilen sınıf: **{result_class}**")
            await ctx.send(message)
    else:
        await ctx.send(" Lütfen bir görsel yükle.")

bot.run("TOKENİM YOK YEE")

















