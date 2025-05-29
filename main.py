import discord
from discord.ext import commands
from keep_alive import keep_alive  # solo si usas Replit

import os

# Intents para que detecte mensajes, miembros y servidores
intents = discord.Intents.default()
intents.message_content = True  # esta línea es la importante
intents.guilds = True
intents.members = True

# Configurar el bot con prefijo !
bot = commands.Bot(command_prefix='!', intents=intents)

# ID del canal de bienvenida
WELCOME_CHANNEL_ID = 1377018480024354876

# Evento cuando alguien entra al servidor
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="₍^. .^₎⟆ ¡Nuevo miembro! ᯓ★",
            description=f"Bienvenido/a {member.mention}!\nVisita el canal de normas y selecciona tus roles!",
            color=0xffc0cb
        )
        embed.set_image(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHZlaWRiNXZ3cTJxdjd0aGVxMHJ3MmVibnYzZzU4Z3N0ZDVudmM2byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/G2LT2Q9rLFzB2xxBzJ/giphy.gif")
        embed.set_footer(text="¡Disfruta tu estadía! 😸")

        await channel.send(embed=embed)

# Comando !normas
@bot.command()
async def normas(ctx):
    normas_texto = """**── .✦ NORMAS DEL SERVIDOR ᯓ★**📃
Este es un servidor en el que se valora la libertad de expresión, el humor negro, y las conversaciones sin censura.
No es un sitio para sensibles ni para gente que busca un entorno “safe space”. Aquí se habla sin filtros, pero con respeto a las reglas básicas.

📍 **⭑.ᐟ Se permiten insultos, discriminación y lenguaje ofensivo.**
Siempre que sea en confianza, entre personas con el mismo humor y no se convierta en algo serio. 
El punto es que se mantenga un ambiente divertido para todos.

📍 **⭑.ᐟ La polémica y los debates son bienvenidos.**
Pero si van a discutir, usen el canal específico para ello.

📍 **⭑.ᐟ Prohibido jugadores tóxicos.**
Si cada partida es un drama emocional para ti, este no es tu sitio.
El objetivo es que se mantenga un ambiente cómodo al jugar y pasar el rato.

📍**⭑.ᐟ FUERA MOROS .ᐟ>ᴗ<**
Si le tienes alergia al jamón, vete.

📍 **⭑.ᐟ Prohibido el contenido NSFW, gore, violento o sexual.**
No importa si es un meme, un link o una broma. Cero tolerancia.

          へ     ♡   ╱|、
     ૮  -   ՛ )      (   -  7
       /   ⁻  ៸|       |、⁻〵
 乀 (ˍ, ل ل      じしˍ,)ノ 
"""
    await ctx.send(normas_texto)

# Mantener vivo en Replit (opcional)
keep_alive()

# Iniciar el bot usando el token desde variable de entorno
bot.run(os.getenv("TOKEN"))
