import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')
@bot.command()
async def a(ctx, ):
    await ctx.send("W Polsce zużywa się około 3,5 mln ton plastiku rocznie. " )
@bot.command()
async def b(ctx, ):
    await ctx.send("""żeby dbac o naszą platente toKorzystaj z kąpieli pod prysznicem zamiast w wannie.
W spłuczce w toalecie załóż zawór ograniczający.
Ogranicz pranie.
Oszczędzaj wodę przy zmywaniu.
Kontroluj szczelność kranów.
Kupuj sprzęty oszczędzające wodę. """ )  
bot.run("token")
