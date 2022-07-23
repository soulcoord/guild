import nextcord
class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Embed Marker",
        )
        self.emTitle=nextcord.ui.TextInput(label="Embed title",min_length=2,max_length=124,required=True,placeholder="Enter the embed title here!")
        self.add_item(self.emTitle)
        self.emDesc=nextcord.ui.TextInput(label="Embed Des",min_length=5,max_length=4000,required=True,placeholder="Enter the embed desciption here!",style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDesc)
    async def callback(self, interaction: nextcord.Interaction):
        title=self.emTitle.value
        desc=self.emDesc.value
        em=nextcord.Embed(title=title,description=desc)
        return await interaction.response.send_message(embed=em)
