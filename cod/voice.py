from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class voice (Cog_Extension):
  @commands.Cog.listener()
  async def on_voice_state_update(self,mess,be,af):
    if mess.id == 511181429376417803:
        try:
            if af.channel.id != 996214096221442078:
                lolo=self.bot.get_user(858323054744174632)
                await lolo.send(f'黑羅在<#{af.channel.id}>')
        except AttributeError:
                lolo=self.bot.get_user(858323054744174632)
                await lolo.send(f'黑羅離開了')


def setup(bot):
    bot.add_cog(voice(bot))