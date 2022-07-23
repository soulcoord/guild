from discord import User
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class kick (Cog_Extension):
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,*,member,reason=None):
        c_r=member.replace('<','').replace('@','').replace('>','')
    
        c=str(c_r).split(' ')
        for c_kick in c:
            a=ctx.guild.get_member(int(c_kick))
            await a.kick(reason=reason)
    @nextcord.slash_command(name='kick',description='將成員踢出伺服器')
    async def kick(self,interaction:nextcord.Integration,message:User):
        kick_user=message.id
        guild=self.bot.get_guild(interaction.guild.id)
        guild1=guild.get_member(kick_user)
        await interaction.response.send_message(f"我超沒用踢不掉{guild1}")

def setup(bot):
    bot.add_cog(kick(bot))