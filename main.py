import discord
import random
import lol_champs
import tokenn
import requests
import random_images
import lol_division


class MyClient(discord.Client):
    async def on_ready(self):
        champs = lol_champs.ChampsR(self)
        champs.champs_id()
        print('Logged in')
        await client.change_presence(activity=discord.Game('!help'))

    async def on_message(self, message):
        r_images = random_images.RandomImages(self)
        lol_div = lol_division.LolDiv(self)
        champs = lol_champs.ChampsR(self)

        self.words = []
        self.message = format(message)
        message_content = message.content.split()

        for word in message_content:
            word_lower = word.lower()
            self.words.append(word_lower)

        print(self.message)

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!eune'):
            server = 'eun1'

            if len(self.words) == 5:
                summoner_name = f'{self.words[1]}%20{self.words[2]}%20{self.words[3]}%20{self.words[4]}'

            elif len(self.words) == 4:
                summoner_name = f'{self.words[1]}%20{self.words[2]}%20{self.words[3]}'

            elif len(self.words) == 3:
                summoner_name = f'{self.words[1]}%20{self.words[2]}'

            elif len(self.words) == 2:
                summoner_name = self.words[1]

            lol_div.get_user_id(summoner_name, server)

            try:
                lol_div.get_user_div_soloq()
                lol_div.get_user_div_flex()
                lol_div.get_user_mastery()

            except AttributeError:
                await lol_div.send_rank(message)

            else:
                await lol_div.send_rank(message)

        elif message.content.startswith('!euw'):
            server = 'euw1'

            if len(self.words) == 5:
                summoner_name = f'{self.words[1]}%20{self.words[2]}%20{self.words[3]}%20{self.words[4]}'

            elif len(self.words) == 4:
                summoner_name = f'{self.words[1]}%20{self.words[2]}%20{self.words[3]}'

            elif len(self.words) == 3:
                summoner_name = f'{self.words[1]}%20{self.words[2]}'
                print(summoner_name)

            elif len(self.words) == 2:
                summoner_name = self.words[1]

            lol_div.get_user_id(summoner_name, server)

            try:
                lol_div.get_user_div_soloq()
                lol_div.get_user_div_flex()

            except AttributeError:
                await lol_div.send_rank(message)

            else:
                await lol_div.send_rank(message)

        elif message.content.startswith('!rjg'):
            await champs.r_jg(message)

        elif message.content.startswith('!rsupp'):
            await champs.r_supp(message)

        elif message.content.startswith('!rmid'):
            await champs.r_mid(message)

        elif message.content.startswith('!rtop'):
            await champs.r_top(message)

        elif message.content.startswith('!radc'):
            await champs.r_adc(message)

        elif message.content.startswith('!meme'):
            await r_images.random_meme(message)

        elif message.content.startswith('!help'):
            await message.channel.send(f'Commands:\n'
                                       f'!eune (Nickname)\n'
                                       f'!euw (Nickname)\n'
                                       f'!meme\n'
                                       f'!rtop\n'
                                       f'!rjg\n'
                                       f'!rmid\n'
                                       f'!radc\n'
                                       f'!rsupp')



TOKEN = tokenn.token
client = MyClient()
client.run(TOKEN)