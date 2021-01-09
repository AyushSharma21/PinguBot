import discord
from discord.ext import commands
from discord.ext.commands import command, has_permissions, bot_has_permissions
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_command_error(ctx, error):
    if(isinstance(error, commands.MissingRequiredArgument)):
        await ctx.send("Missing argument!")
    else:
        raise error
    
@client.command()
@bot_has_permissions(manage_messages=True)
@has_permissions(manage_messages=True)
async def clearMessage(ctx, number):
    try:
        convertNumberInt = int(number)
        if (convertNumberInt <= 0 or convertNumberInt > 100):
            await ctx.send("Must enter a number between 1 and 100 (inclusive).")
        else:
            print("triggered")
            await ctx.message.delete()
            deletedCount = await ctx.channel.purge(limit = convertNumberInt)
            await ctx.send(f"Got rid of {len(deletedCount)} messages. ", delete_after=5)
    except ValueError:
        await ctx.send("Invalid Argument")
        return



client.run('') //Add Your token here.
