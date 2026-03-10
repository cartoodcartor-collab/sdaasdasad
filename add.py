import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Online {bot.user}')

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        new_roles = [role for role in after.roles if role not in before.roles]

        for role in new_roles:
            audit_logs = await before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update).flatten()

            if audit_logs:
                entry = audit_logs[0]

                if entry.target.id == after.id:
                    giver = entry.user
                    channel_id = 1446816191422136526
                    channel = bot.get_channel(channel_id)

                    if channel:
                        await channel.send(f'{after.mention} ได้ role [ {role.name} ] โดย {giver.mention}')

bot.run("MTQ0ODk0OTYxNTAzNzUxNzg3NQ.GGbGFZ.53Gcz5ntamqN0kBhK6G3qu_WW2z9742vjT2JbY")