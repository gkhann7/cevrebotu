import discord
import os

from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def cevrekirliligi(ctx):
    await ctx.send(f'Çevre kirliliği, doğal çevreye zarar veren maddelerin veya enerji türlerinin (örneğin, kimyasal maddeler, atıklar, ışık, ısı, gürültü) doğaya salınmasıyla oluşan kirlenmedir. Hızlı sanayileşme, kentleşme, nüfus artışı ve insan faaliyetleri çevre kirliliğini artırmakta ve gezegenimizin ekosistemini tehdit etmektedir. Çevre kirliliğinin farklı türleri vardır ve her biri doğayı farklı şekillerde etkiler.')

@bot.command()
async def ckturleri(ctx):
    await ctx.send(f"""Hava Kirliliği
Su Kirliliği
Toprak Kirliliği
Gürültü Kirliliği
Işık Kirliliği""")








bot.run("TOKEN")
