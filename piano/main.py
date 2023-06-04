import pygame
import play 
pygame.init()
pygame.mixer.init()
play.set_backdrop("mediumpurple")
text1 = play.new_text(words = "Це класнепіаніно для гри" , x = 0 , y = 200)
text2 = play.new_text(words = "Створи свою мелодію напискаючи на клавіші", x = 0 , y = 150)
keys = []
sounds = []

for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color = "indigo" , width = 40 , height = 120 , x = key_x , y = 0 , border_width = 3 , border_color = "blueviolet") 
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + ".ogg")
    sounds.append(sound)


@play.when_program_starts
def start():
    pass


@play.repeat_forever
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = "purple"
            await play.timer(0.3)
            keys[j].color = "indigo"
play.start_program()