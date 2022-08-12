from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class role (Cog_Extension):
  @commands.Cog.listener()
  async def on_raw_reaction_add(self,role):
    if role.message_id == 996482471803752560:
      not_role=[996416756086222961,996416970314489987,996417043140182097,996417097620004975,996417176099635271,996417295834423458,996417376725762089,996417493474230282]
      a_g=self.bot.get_guild(role.guild_id)
      a_role=a_g.get_member(role.user_id)
      list_2 = []

      for users_role in a_role.roles:
        list_2.append(users_role.id)
      intersection = [x for x in not_role for y in list_2 if x == y]
      if len(intersection) != 0:
        await a_role.send(f'你已領取**{a_g.get_role(intersection[0])}**，請將身分組刪除再領取新的世界等級')
        intersection.clear
      if not intersection:
          if str(role.emoji) == ("1️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996416756086222961)#世界等級1
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("2️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996416970314489987)#世界等級2
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("3️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417043140182097)#世界等級3
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("4️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417097620004975)#世界等級4
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("5️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417176099635271)#世界等級5
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("6️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417295834423458)#世界等級6
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("7️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417376725762089)#世界等級7
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("8️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417493474230282)#世界等級8
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          intersection.clear
    elif role.message_id == 996516544274243615:
      not_role=[996470460407627786,996470641073061939,996470572475228270,996470702880346182]
      a_g=self.bot.get_guild(role.guild_id)
      a_role=a_g.get_member(role.user_id)
      list_2 = []

      for users_role in a_role.roles:
        list_2.append(users_role.id)
      intersection1 = [x for x in not_role for y in list_2 if x == y]
      if len(intersection1) != 0:
        await a_role.send(f'你已領取**{a_g.get_role(intersection1[0])}**，請將身分組刪除再領取新的伺服器')
        intersection1.clear
      if not intersection1:
          if str(role.emoji) == ("🇦"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470460407627786)#北美
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🇧"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470641073061939)#歐洲
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🇨"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470572475228270)#亞洲
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🇩"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470702880346182)#台港澳
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          intersection1.clear
    elif role.message_id == 996519987160293486:
      if str(role.emoji) == ("📢"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470792315490326)#重大告知
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
      elif str(role.emoji) == ("🎉"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996471385536860230)#活動告知
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
    elif role.message_id == 996521942859390976:
      not_role=[996295323829948556,996295478541041704,996292486546857995,996294524068429905,996295031424032820,996294699793002547,996294895528587355]
      a_g=self.bot.get_guild(role.guild_id)
      a_role=a_g.get_member(role.user_id)
      list_2 = []
      for users_role in a_role.roles:
        list_2.append(users_role.id)
      intersection2 = [x for x in not_role for y in list_2 if x == y]
      if len(intersection2) != 0:
        await a_role.send(f'你已領取**{a_g.get_role(intersection2[0])}**，請將身分組刪除再領取新的神之眼')
        intersection2.clear
      if not intersection2:
          if str(role.emoji) == ("🍏"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996295323829948556)#草
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("⛈️"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996295478541041704)#雷
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🚰"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996292486546857995)#水
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🔥"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996294524068429905)#火
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🌬️"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996295031424032820)#風
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🧊"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996294699793002547)#冰
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🪨"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996294895528587355)#岩
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          intersection2.clear
    elif role.message_id == 996527385543450695:
      if str(role.emoji) == ("🕶️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978738302482010193)#紳士
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
      elif str(role.emoji) == ("🕵️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978739129405833256)#內鬼
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self,role):
    if role.message_id == 996482471803752560:
      if str(role.emoji) == ("1️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996416756086222961)#世界等級1
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("2️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996416970314489987)#世界等級2
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("3️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417043140182097)#世界等級3
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("4️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417097620004975)#世界等級4
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("5️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417176099635271)#世界等級5
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("6️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417295834423458)#世界等級6
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("7️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417376725762089)#世界等級7
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("8️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417493474230282)#世界等級8
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996516544274243615:
      if str(role.emoji) == ("🇦"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470460407627786)#北美
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🇧"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470641073061939)#歐洲
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🇨"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470572475228270)#亞洲
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🇩"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470702880346182)#台港澳
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996519987160293486:
      if str(role.emoji) == ("📢"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470792315490326)#重大告知
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🎉"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996471385536860230)#活動告知
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996521942859390976:
      if str(role.emoji) == ("🍏"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996295323829948556)#草
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("⛈️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996295478541041704)#雷
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🚰"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996292486546857995)#水
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🔥"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996294524068429905)#火
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🌬️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996295031424032820)#風
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🧊"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996294699793002547)#冰
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🪨"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996294895528587355)#岩
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996527385543450695:
      if str(role.emoji) == ("🕶️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978738302482010193)#紳士
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🕵️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978739129405833256)#內鬼
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)

        


  @commands.command(name='testhi')
  async def sendmenu1(self,ctx):
      async def callback1(interaction):
          if  "gif2" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988408980307079218)#社長女裝
            await interaction.user.add_roles(r_role)
          if "gif3" in dropdown.values :
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(987992549807517696)#特殊性癖
            await interaction.user.add_roles(r_role)
          if "gif4" in dropdown.values :
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988409108476620920)#麻將
            await interaction.user.add_roles(r_role)
          if "gif5" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988523958934589611)#音遊討論
            await interaction.user.add_roles(r_role)
          if "gif6" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988797563643777084)#專業技術交流
            await interaction.user.add_roles(r_role)
          if "gif7" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(989102712182427679)#日文交流
            await interaction.user.add_roles(r_role)
          if "gif8" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(991066384731627570)#原神樂譜
            await interaction.user.add_roles(r_role)
          if "gif9" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(992007661212139541)#崩壞
            await interaction.user.add_roles(r_role)
          if "gif10" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(994672919131201556)#賽馬娘
            await interaction.user.add_roles(r_role)
          if "gif11" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(999366911651487784)#專業攝影
            await interaction.user.add_roles(r_role)
          if "gif12" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(994898278648905748)#準備開吉
            await interaction.user.add_roles(r_role)
          if "gif13" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(994899194236125185)#假面騎士
            await interaction.user.add_roles(r_role)
          if "gif14" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565265158021150)#傳說對決
            await interaction.user.add_roles(r_role)
          if "gif15" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565561187803187)#APEX
            await interaction.user.add_roles(r_role)
          if "gif16" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565613918593055)#絕對零
            await interaction.user.add_roles(r_role)
          if "gif17" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565615902503002)#遊戲王
            await interaction.user.add_roles(r_role)
          if "gif18" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565999580655616)#明日方舟
            await interaction.user.add_roles(r_role)
          if "gif19" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007566084435628092)#空洞騎士
            await interaction.user.add_roles(r_role)



      ts3=nextcord.SelectOption(label="特殊性向成人圖區",value="gif2",description="領取後將開啟隱藏的子頻道")
      ts4=nextcord.SelectOption(label="社長女裝",value="gif3",description="領取後將開啟隱藏的子頻道")
      ts5=nextcord.SelectOption(label="麻將專區",value="gif4",description="領取後將開啟隱藏的子頻道")
      ts6=nextcord.SelectOption(label="音遊討論區",value="gif5",description="領取後將開啟隱藏的子頻道")
      ts7=nextcord.SelectOption(label="專業技術交流區",value="gif6",description="領取後將開啟隱藏的子頻道")  
      ts8=nextcord.SelectOption(label="日文蕉流區。",value="gif7",description="領取後將開啟隱藏的子頻道")  
      ts9=nextcord.SelectOption(label="原神樂譜交流區。",value="gif8",description="領取後將開啟隱藏的子頻道")  
      ts10=nextcord.SelectOption(label="崩壞Hokai Impact。",value="gif9",description="領取後將開啟隱藏的子頻道")  
      ts11=nextcord.SelectOption(label="賽馬娘討論區。",value="gif10",description="領取後將開啟隱藏的子頻道")
      ts12=nextcord.SelectOption(label="專業攝影交流。",value="gif11",description="領取後將開啟隱藏的子頻道")    
      ts13=nextcord.SelectOption(label="準備開吉。",value="gif12",description="領取後將開啟隱藏的子頻道")
      ts14=nextcord.SelectOption(label="假面騎士。",value="gif13",description="領取後將開啟隱藏的子頻道")
      ts15=nextcord.SelectOption(label="傳說對決。",value="gif14",description="領取後將開啟隱藏的子頻道")  
      ts16=nextcord.SelectOption(label="APEX。",value="gif15",description="領取後將開啟隱藏的子頻道")  
      ts17=nextcord.SelectOption(label="絕對零。",value="gif16",description="領取後將開啟隱藏的子頻道")  
      ts18=nextcord.SelectOption(label="遊戲王。",value="gif17",description="領取後將開啟隱藏的子頻道")
      ts19=nextcord.SelectOption(label="明日方舟。",value="gif18",description="領取後將開啟隱藏的子頻道")    
      ts20=nextcord.SelectOption(label="空洞騎士。",value="gif19",description="領取後將開啟隱藏的子頻道")
      dropdown=nextcord.ui.Select(placeholder="最多可一次選擇6項身分組",options=[ts3,ts4,ts5,ts6,ts7,ts8,ts9,ts10,ts11,ts12,ts13,ts14,ts15,ts16,ts17,ts18,ts19,ts20],max_values=6)
      dropdown.callback=callback1
      value1=nextcord.ui.View()
      value1.add_item(dropdown)
      await ctx.send("領取身分組",view=value1)

  @commands.command(name='removehi')
  async def sendmenu2(self,ctx):
      async def callback1(interaction):
          if  "gif2" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988408980307079218)#社長女裝
            await interaction.user.remove_roles(r_role)
          if "gif3" in dropdown.values :
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(987992549807517696)#特殊性癖
            await interaction.user.remove_roles(r_role)
          if "gif4" in dropdown.values :
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988409108476620920)#麻將
            await interaction.user.remove_roles(r_role)
          if "gif5" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988523958934589611)#音遊討論
            await interaction.user.remove_roles(r_role)
          if "gif6" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(988797563643777084)#專業技術交流
            await interaction.user.remove_roles(r_role)
          if "gif7" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(989102712182427679)#日文交流
            await interaction.user.remove_roles(r_role)
          if "gif8" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(991066384731627570)#原神樂譜
            await interaction.user.remove_roles(r_role)
          if "gif9" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(992007661212139541)#崩壞
            await interaction.user.remove_roles(r_role)
          if "gif10" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(994672919131201556)#賽馬娘
            await interaction.user.remove_roles(r_role)
          if "gif11" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(999366911651487784)#專業攝影
            await interaction.user.remove_roles(r_role)
          if "gif12" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(994898278648905748)#準備開吉
            await interaction.user.remove_roles(r_role)
          if "gif13" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(994899194236125185)#假面騎士
            await interaction.user.remove_roles(r_role)
          if "gif14" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565265158021150)#傳說對決
            await interaction.user.remove_roles(r_role)
          if "gif15" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565561187803187)#APEX
            await interaction.user.remove_roles(r_role)
          if "gif16" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565613918593055)#絕對零
            await interaction.user.remove_roles(r_role)
          if "gif17" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565615902503002)#遊戲王
            await interaction.user.remove_roles(r_role)
          if "gif18" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007565999580655616)#明日方舟
            await interaction.user.remove_roles(r_role)
          if "gif19" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1007566084435628092)#空洞騎士
            await interaction.user.remove_roles(r_role)


      ts3=nextcord.SelectOption(label="特殊性向成人圖區",value="gif2",description="領取後將開啟隱藏的子頻道")
      ts4=nextcord.SelectOption(label="社長女裝",value="gif3",description="領取後將開啟隱藏的子頻道")
      ts5=nextcord.SelectOption(label="麻將專區",value="gif4",description="領取後將開啟隱藏的子頻道")
      ts6=nextcord.SelectOption(label="音遊討論區",value="gif5",description="領取後將開啟隱藏的子頻道")
      ts7=nextcord.SelectOption(label="專業技術交流區",value="gif6",description="領取後將開啟隱藏的子頻道")  
      ts8=nextcord.SelectOption(label="日文蕉流區。",value="gif7",description="領取後將開啟隱藏的子頻道")  
      ts9=nextcord.SelectOption(label="原神樂譜交流區。",value="gif8",description="領取後將開啟隱藏的子頻道")  
      ts10=nextcord.SelectOption(label="崩壞Hokai Impact。",value="gif9",description="領取後將開啟隱藏的子頻道")  
      ts11=nextcord.SelectOption(label="賽馬娘討論區。",value="gif10",description="領取後將開啟隱藏的子頻道")
      ts12=nextcord.SelectOption(label="專業攝影交流。",value="gif11",description="領取後將開啟隱藏的子頻道")      
      ts13=nextcord.SelectOption(label="準備開吉。",value="gif12",description="領取後將開啟隱藏的子頻道")
      ts14=nextcord.SelectOption(label="假面騎士。",value="gif13",description="領取後將開啟隱藏的子頻道")
      ts15=nextcord.SelectOption(label="傳說對決。",value="gif14",description="領取後將開啟隱藏的子頻道")  
      ts16=nextcord.SelectOption(label="APEX。",value="gif15",description="領取後將開啟隱藏的子頻道")  
      ts17=nextcord.SelectOption(label="絕對零。",value="gif16",description="領取後將開啟隱藏的子頻道")  
      ts18=nextcord.SelectOption(label="遊戲王。",value="gif17",description="領取後將開啟隱藏的子頻道")
      ts19=nextcord.SelectOption(label="明日方舟。",value="gif18",description="領取後將開啟隱藏的子頻道")    
      ts20=nextcord.SelectOption(label="空洞騎士。",value="gif19",description="領取後將開啟隱藏的子頻道")
      dropdown=nextcord.ui.Select(placeholder="最多可一次移除6個身分組",options=[ts3,ts4,ts5,ts6,ts7,ts8,ts9,ts10,ts11,ts12,ts13,ts14,ts15,ts16,ts17,ts18,ts19,ts20],max_values=6)
      dropdown.callback=callback1
      value1=nextcord.ui.View()
      value1.add_item(dropdown)
      await ctx.send("移除身分組",view=value1)



def setup(bot):
    bot.add_cog(role(bot))