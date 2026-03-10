import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        new_roles = [role for role in after.roles if role not in before.roles]

        for role in new_roles:
            async for entry in before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):

                if entry.target.id == after.id:
                    giver = entry.user
                    channel = bot.get_channel()

                    if channel:
                        await channel.send(f'{after.mention} ได้ role [ {role.name} ] โดย {giver.mention}')

bot.run('')