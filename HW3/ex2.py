
class English:  
    def greeting(self):
        print("Hello friend")

class Spanish:
    def greeting(self):
        print("Hola amigos")


speaker_english = English()
speaker_spanish = Spanish()

def hello_friend(english, spanish):
    for lenguage in (english, spanish):
        lenguage.greeting()

hello_friend(speaker_english, speaker_spanish)


    