from ast import Pass
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
after_channel=[]

class wndi (Cog_Extension):

    @commands.Cog.listener()
    async def on_voice_state_update(self,member, before, after):
        global creat_channel
        creat_channel={
            member:nextcord.PermissionOverwrite(manage_channels=True)
        }
        s = self.bot.get_guild(978680658740260865)
        s1=s.get_channel(1041254008762925107)
        s2=s1.category
        if after.channel == None:
            if int(before.channel.id) in after_channel:
                await before.channel.delete()
                after_channel.remove(int(before.channel.id)) 
            elif before.channel !=None:
                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))
                    print(before.id)
        if before.channel==None:      
            if after.channel.id == 1041254008762925107:
                try:
                    if int(before.channel.id) in after_channel:
    
                        await before.channel.delete()
                        after_channel.remove(int(before.channel.id))
                except:
                    nowchannel = await s.create_voice_channel(str(member).split("#")[0],overwrites=creat_channel,category=s2)
                    after_channel.append(int(nowchannel.id))
                    await member.move_to(nowchannel)
            else:
                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))
        if before.channel != None and after.channel  != None:
            if after.channel.id == 1041254008762925107:

                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))

                nowchannel = await s.create_voice_channel(str(member).split("#")[0],overwrites=creat_channel,category=s2)
                after_channel.append(int(nowchannel.id))
                await member.move_to(nowchannel)
            else:
                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))
def setup(bot):
    bot.add_cog(wndi(bot))