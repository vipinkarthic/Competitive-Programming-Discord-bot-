import requests
import datetime
import json
import settings
import discord
from discord.ext import commands
import json
import datetime
import _strptime
import discord.ext.commands

def run():
    def sortDates(datesList):
        split_up = datesList.split('.')
        return split_up[1], split_up[0]

    prefix = "?"
    bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        print("Everything's all ready to go~")
        
        try:
            synced = await bot.tree.sync()
            print(f"Synced {synced} commands")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

    @bot.event
    async def on_message(message):
        print("The message's content was", message.content)
        await bot.process_commands(message)


    @bot.tree.command(name = 'ping')
    async def ping(interaction : discord.Interaction):
        '''
        This text will be shown in the help command
        '''
        latency = bot.latency
        await interaction.response.send_message(f"Pong! ({latency*1000}ms)")
        
    @bot.hybrid_command()
    async def codeforces(ctx):
        link = requests.get('https://clist.by:443/api/v4/contest/?username=hh17&api_key=97fef2c489b2da5496452919d49865ea74c305c3&limit=1&format_time=true&resource=codeforces.com&upcoming=true') 
        jl = link.json()
        name = 'hardhacker17'
        icon = 'https://cdn.discordapp.com/avatars/560988081747132426/8d90721491b51b8558958083d3bcb20d.webp?size=160'
        for i in jl['objects']: 
            event = i['event']
            start = i['start']
            startnew = start.replace('T',' ')
            startnew2 = start.replace('.','/')
            end = i['end']
            endnew = end.replace('T',' ')
            endnew2 = start.replace('.','/')
            duration = i['duration']
            href = i['href']
            host = i['host']
            embed = discord.Embed(title = "UPCOMING CONTEST",color=discord.Color.random())  
            embed.set_thumbnail(url = "https://res.cloudinary.com/practicaldev/image/fetch/s--mzwvoucO--/c_imagga_scale,f_auto,fl_progressive,h_1080,q_auto,w_1080/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cer3l19eex0wy900b101.jpg") 
            embed.add_field(name = "Contest Name", value = f'{event}', inline = False)
            embed.add_field(name = "Start Time", value = f'{startnew2} IST', inline = True)
            embed.add_field(name = "End Time", value = f'{endnew2} IST', inline = True)
            embed.add_field(name = "Duration", value = f'{duration}', inline = False)
            embed.add_field(name = "Link to Problem", value = f'{href}', inline = False)
            embed.set_footer(text = f'Made by {name}', icon_url = f'{icon}')
            await ctx.send(embed=embed)
            
        with open('numbers.env', 'w') as f:
            json.dump(jl,f)
        
        print(len(jl['objects']))
        
    @bot.hybrid_command()
    async def codechef(ctx):
        link = requests.get('https://clist.by:443/api/v4/contest/?username=hh17&api_key=97fef2c489b2da5496452919d49865ea74c305c3&limit=1&format_time=true&resource=codechef.com&upcoming=true') 
        jl = link.json()
        name = 'hardhacker17'
        icon = 'https://cdn.discordapp.com/avatars/560988081747132426/8d90721491b51b8558958083d3bcb20d.webp?size=160'
        for i in jl['objects']: 
            event = i['event']
            start = i['start']
            startnew = start.replace('T',' ')
            startnew2 = start.replace('.','/')
            end = i['end']
            endnew = end.replace('T',' ')
            endnew2 = start.replace('.','/')
            duration = i['duration']
            href = i['href']
            host = i['host']
            embed = discord.Embed(title = "UPCOMING CONTEST",color=discord.Color.random())  
            embed.set_thumbnail(url = "https://yt3.googleusercontent.com/Lkx3tvgHdRADC3wXQ5TfJZRTeH4nboEPA_-eJChOZ6jRkOdY35lcg014Whj36rHFXhrHY1T_4cs=s900-c-k-c0x00ffffff-no-rj") 
            embed.add_field(name = "Contest Name", value = f'{event}', inline = False)
            embed.add_field(name = "Start Time", value = f'{startnew2} IST', inline = True)
            embed.add_field(name = "End Time", value = f'{endnew2} IST', inline = True)
            embed.add_field(name = "Duration", value = f'{duration}', inline = False)
            embed.add_field(name = "Link to Problem", value = f'{href}', inline = False)
            embed.set_footer(text = f'Made by {name}', icon_url = f'{icon}')
            await ctx.send(embed=embed)
            
        with open('numbers.env', 'w') as f:
            json.dump(jl,f)
        
        print(len(jl['objects']))
        
    @bot.hybrid_command()
    async def help(ctx):
        embed = discord.Embed(title = "HELP",color=discord.Color.random())  
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1186982061169463296/1187068832469241876/image.png?ex=65958b00&is=65831600&hm=72ef81b70b998b43fdba2ec08c3cd6243ba131aee472b5393f830276835ac7f1&") 
        embed.add_field(name = "Codeforces", value = f'`?codeforces`\n **This command lists the details about the upcoming contest on codeforces**', inline = False)
        embed.add_field(name = "Codechef", value = f'`?codechef`\n **This command lists the details about the upcoming contest on codechef**', inline = False)
        embed.add_field(name = "Help", value = f'`?help`', inline = False)
        embed.set_footer(text = f'Made by hardhacker17', icon_url = f'https://cdn.discordapp.com/avatars/560988081747132426/8d90721491b51b8558958083d3bcb20d.webp?size=160')
        await ctx.send(embed=embed)
        
    @bot.hybrid_command()
    @commands.has_role('mod')
    async def _testdm(ctx):
        currentserver = ctx.author.guild
        for i in currentserver.members:
            if i.bot:
                continue
            channel = await i.create_dm()
            await channel.send("Hello, Everyone!\n This is a test message from the bot\n If you can see this message, then the bot is working fine.\nIf you are seeing this message please ping me \n by doing @hardhacker17 in the Competitive Programming server\nThank you for your time")
    
    @_testdm.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send(text)
        
    @bot.hybrid_command()
    @commands.has_role('mod')
    async def remind(ctx):
        currentserver = ctx.author.guild

        link = requests.get('https://clist.by:443/api/v4/contest/?username=hh17&api_key=97fef2c489b2da5496452919d49865ea74c305c3&upcoming=true&format_time=true&resource=codechef.com%2Ccodeforces.com&end__lt=2023-12-31T03%3A11%3A59')
        jl = link.json()
        href = None
        event = None
        start = None
        end = None
        duration = None
        dt = {}
        sorted_datetime_list = []
        sorted_datetime_dict = {}
        for i in jl['objects']:
            if 'START' in i['href'] or 'contests' in i['href']:
                splittime = i['start'].split(' ')
                appendtime = splittime[0]
                key = i['id']
                value = appendtime
                dt[key] = value
                sorted_datetime_list = sorted(dt.items(), key=lambda x: datetime.datetime.strptime(x[1] , "%d.%m"))
                sorted_datetime_dict = dict(sorted_datetime_list)  
                
        for key, value in sorted_datetime_dict.items():
                    for i in jl['objects']:
                        if i['id'] == key:
                            href = i['href']
                            event = i['event']
                            start = i['start']
                            end = i['end']
                            duration = i['duration']
                            break
                    break       
                
        embed = discord.Embed(title = "REMINDER",color=discord.Color.random())
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1186982061169463296/1187068832469241876/image.png?ex=65958b00&is=65831600&hm=72ef81b70b998b43fdba2ec08c3cd6243ba131aee472b5393f830276835ac7f1&")
        embed.add_field(name = "Contest Name", value = f'{event}', inline = False)
        embed.add_field(name = "Start Time", value = f'{start} IST', inline = True)
        embed.add_field(name = "End Time", value = f'{end} IST', inline = True)
        embed.add_field(name = "Duration", value = f'{duration}', inline = False)
        embed.add_field(name = "Link to Contest", value = f'{href}', inline = False)
        embed.set_footer(text = f'Made by hardhacker17', icon_url = f'https://cdn.discordapp.com/avatars/560988081747132426/8d90721491b51b8558958083d3bcb20d.webp?size=160')
        
        for i in currentserver.members:
            if i.bot:
                continue
            channel = await i.create_dm()
            await channel.send(embed=embed)

        await ctx.send("Reminder sent to all members of the server")
        channelnew = bot.get_channel(1185950938310131782)
        await channelnew.send("@everyone THIS IS A REMINDER TO THE CONTEST")
        await channelnew.send(embed=embed)
        
    bot.run(settings.DISCORD_API_SECRET)

        

if __name__ == "__main__":
    run()