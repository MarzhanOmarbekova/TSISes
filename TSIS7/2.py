import pygame as pg
import os 
import random

image_library = {}
def get_image (path):
    global image_library
    image = image_library.get(path)
    if image == None :
        canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
        image = pg.image.load(path)
        image_library[canonicalized_path] = image
    return image
y=0
sound = None
sounds_library = {}
def get_sound(path):
    global sounds_library , sound 
    sound = sounds_library.get(path)
    if sound == None :
        canonicalized_path =  path.replace("\\", os.sep).replace("/", os.sep)
        sound = pg.mixer.music.load(canonicalized_path)
        sounds_library[canonicalized_path] = sound
    return sound

names = ["Another Day of Sun", "City Of Stars", "Mia & Sebastian's Theme", "Mitski", "One_of_the_girls", "Pure Imagination"] 
names_mp3 =[ song+".mp3" for song in names]
names_mp3_2 =[ song+".mp3" for song in names]

def play_song(order):
    global names_mp3 , y
    if order == -1:
        names_mp3 = [names_mp3[-1]]+ names_mp3[:5]
    elif order == 1:
        names_mp3 = names_mp3[1:] + [names_mp3[0]]
    path = names_mp3[0]
    for i in range (6):
        if path == names_mp3_2[i]:
            y = i*100
    get_sound("SOUNDS/"+names_mp3[0])
    pg.mixer.music.play()


currently_playing_song =None
def shuffle():
    global currently_playing_song , names_mp3 , y
    next_song = random.choice(names_mp3)
    while next_song == currently_playing_song:
        next_song = random.choice(names_mp3)
    currently_playing_song = next_song
    for i in range (6):
        if currently_playing_song == names_mp3_2[i]:
            y = i*100
    get_sound("SOUNDS/"+currently_playing_song)
    pg.mixer.music.play()


pg.init()
screen = pg.display.set_mode((600,600))
pg.display.set_caption("Playlist")
pg.display.set_icon(get_image("IMAGES2/icon1.jpg"))
done = False

myfont = pg.font.Font("FONTS/BebasNeue-Regular.ttf",40)
text_surfaces =[myfont.render(names[i],True,(0,0,0)) for i in range (6) ]

dancing = [get_image("IMAGES2/dance"+str(i+1)+".png") for i in range(8)]
pos = 0

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    screen.fill((0,66,66))
    
    screen.blit(pg.transform.scale(dancing[pos],(100,100)), (350,y))
    if pos == 7:
        pos=0
    else:
        pos+=1
    screen.blit(pg.transform.scale(get_image("IMAGES2/shuffling.png"), (60,60)) , (510,50) )
    screen.blit(pg.transform.scale(get_image("IMAGES2/prev_song.jpg"), (60,60)) , (480,110))
    screen.blit(pg.transform.scale(get_image("IMAGES2/next_song.jpg"), (60,60)) , (540,110))
    screen.blit(pg.transform.scale(get_image("IMAGES2/stop.jpg"), (60,60)) , (510,170))
    for i in range (6):
        if i == 0:
            screen.blit(text_surfaces[i], (10,20 ))
        else : 
            screen.blit(text_surfaces[i], (10,i*100+20 ))
    
    keys = pg.key.get_pressed()
    if keys[pg.K_k] :
        pg.mixer.music.stop()
    if keys[pg.K_j] : 
        play_song(-1)
    if keys[pg.K_l]:
        play_song(1)
    if keys[pg.K_s]:
        shuffle()

    pg.display.flip()