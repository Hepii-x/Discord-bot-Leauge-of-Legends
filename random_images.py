import requests

class RandomImages():
    def __init__(self, message):
        self.message = message

    async def random_meme(self, message):
        self.meme_get = requests.get('https://meme-api.herokuapp.com/gimme')
        self.meme_json = self.meme_get.json()
        self.meme_image = self.meme_json['url']
        await message.channel.send(self.meme_image)

