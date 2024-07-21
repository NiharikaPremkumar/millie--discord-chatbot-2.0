
import discord
from discord.ext import commands
import google.generativeai as genai
DISCORD_TOKEN= ‘your token’
GEMINI_API_KEY= ‘your key’
genai.configure(api_key=GEMINI_API_KEY)
intents= discord.Intents.default()
intents.message_content=True
bot= commands.Bot(command_prefix='!', intents=intents)
@bot.command(name='query')
async def query(ctx,*,question):
    if not question:
        await ctx.send('pealse ask me something!')
        return
    try:
        model=genai.GenerativeModel('gemini-1.5-flash')
        response=model.generate_content(question)
        if response and hasattr(response, 'text'):
            response_text= response.text
            for chunk in[response_text[i:i + 1900]for i in range(0,len(response_text),1900)]:
                await ctx.send(chunk)
    except Exception as e:
        await ctx.send(f'an error occured while processing:{e}')
bot.run(DISCORD_TOKEN)
