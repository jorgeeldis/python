import pygame
import os
import sys
from random import randrange

pygame.init()

# game setup
window_width = 900
window_height = 600
window_center = (window_width//2,window_height//2)
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Flappy bird")

fps = pygame.time.Clock()
started = False

# colors
black = (0,0,0)
white = (255,255,255)

default_font = os.path.join("Font","junegull.ttf")

#score_sound = pygame.mixer.Sound("score.wav")
#jump_sound = pygame.mixer.Sound(os.path.join("Sound","jump.wav"))
#collide_sound = pygame.mixer.Sound(os.path.join("Sound","collide.wav"))
#collide2_sound = pygame.mixer.Sound(os.path.join("Sound","collide2.wav"))

class Text:
    def __init__(self,font:str,text:str,size:int,color:tuple):
        self.font = pygame.font.Font(font,size)
        self.text = text
        self.color = color
        self.object = self.font.render(self.text,True,self.color)
        self.rect = self.object.get_rect()

    def place(self,xy:tuple=(0,0),center:bool=False):
        self.object = self.font.render(self.text,True,self.color)
        window.blit(self.object,self.rect)
        if center:
            self.rect.center = window_center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]


class Button:
    def __init__(self,image,size):
        self.image = pygame.image.load(os.path.join("HUD",image))
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect()

    def place(self,xy:tuple=(0,0),center:bool=False):
        window.blit(self.image,self.rect)
        if center:
            self.rect.center = window_center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
            if pygame.mouse.get_pressed()[0] == 1:
                return True


class Background:
    def __init__(self,sort:str,which:int):
        self.sort = sort
        self.image = pygame.image.load(os.path.join("Background",f"{self.sort}.png"))
        self.image = pygame.transform.scale(self.image,(window_width,window_height))
        self.rect = self.image.get_rect()
        self.which = which
        if self.which == 1:
            self.rect.x = window_width

    def draw(self):
        window.blit(self.image,self.rect)

        if not bird.died:
            if self.sort == "ground":
                self.rect.x -= 2
            elif self.sort == "mountain":
                self.rect.x -= 1
        if self.sort == "cloud":
            if not bird.died:
                self.rect.x -= 3
            else:
                self.rect.x -= 1

        if self.rect.right < 0:
            self.rect.x = window_width


class Wall:
    def __init__(self,which,y):
        self.image = pygame.image.load(os.path.join("Background","wall.png"))
        self.image = pygame.transform.scale(self.image,(50,int(window_height/1.5)))
        self.rect = self.image.get_rect()
        self.which = which
        self.rect.x = window_width
        if self.which == 1:
            self.rect.y = window_height//2
            self.rect.y += 130
        else:
            self.rect.y -= 130

        self.rect.y += y
        self.bird_one_point = 0

    def draw(self):
        window.blit(self.image,self.rect)

    def movement(self):
        self.rect.x -= 2
        if self.rect.right < 0:
            walls.remove(self)
            del self

    def bird_point(self):
        if self.rect.centerx-4 < bird.rect.centerx < self.rect.centerx+4 and self.bird_one_point == 0 and self.which == 0:
            bird.score += 1
            self.bird_one_point = 1
            score_sound.set_volume(0.2)
            score_sound.play()


class Player:
    def __init__(self,size):
        self.image = pygame.image.load(os.path.join("Bird","bird.png"))
        self.image = pygame.transform.scale(self.image,(size,size-8))
        self.rect = self.image.get_rect()
        self.down = 0
        self.score = 0
        self.died = False

    def place(self,xy:tuple=(0,0),center:bool=False):
        window.blit(self.image,self.rect)
        if center:
            self.rect.center = window_center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

    def draw(self):
        window.blit(self.image,self.rect)

    def gravity(self,g):
        gravity = g
        self.rect.y += int(self.down)
        self.down += gravity
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > window_height+20:
            self.rect.bottom = window_height+20

    def jump(self):
        self.down = -7
        jump_sound.set_volume(0.1)
        jump_sound.play()

    def collision(self):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.died = True
                collide2_sound.set_volume(0.1)
                collide2_sound.play()

        if self.rect.bottom > window_height:
            self.rect.bottom = window_height
            self.died = True
            collide_sound.set_volume(0.1)
            collide_sound.play()


# created objects
grounds = []
clouds = []
mountains = []
for w in range(2):
    new_ground = Background("ground",w)
    grounds.append(new_ground)

    new_cloud = Background("cloud",w)
    clouds.append(new_cloud)

    new_mountain = Background("mountain",w)
    mountains.append(new_mountain)

air = pygame.image.load(os.path.join("Background","air.png"))

play_button = Button("play.png",64)
restart_button = Button("restart.png",64)

bird = Player(48)

wall_td = 0
walls = []

# created texts
game_text = Text(default_font,"Flappy Bird",50,(255,112,0))
howtoplay_text = Text(default_font,"How to play? -> press 'SPACE' or 'MOUSE'",25,white)
score_text = Text(default_font,"Score:",30,black)
scoreNum_text = Text(default_font,str(bird.score),30,black)
youdied_text = Text(default_font,"You died",40,black)

while True:
    # game loop
    window.blit(air,(0,0))
    keys = pygame.key.get_pressed()

    for mountain in mountains:
        mountain.draw()

    for ground in grounds:
        ground.draw()

    for cloud in clouds:
        cloud.draw()

    if not started:
        game_text.place((0,-220),True)
        howtoplay_text.place((0,150),True)
        play_button.place(center=True)
        bird.place((0,-110),True)

        started = play_button.click()

    if started:
        for wall in walls:
            wall.draw()
            if not bird.died:
                wall.movement()
                wall.bird_point()
                
        bird.gravity(0.3)
        bird.draw(),
        if not bird.died:
            bird.collision()

            wall_td += 1
            if wall_td == 100:
                space_y = randrange(-110,110)
                for d in range(2):
                    new_wall = Wall(d,space_y)
                    walls.append(new_wall)
                wall_td = 0

        score_text.place((10, 10))
        scoreNum_text.place((110, 10))
        scoreNum_text.text = str(bird.score)

        if bird.died:
            youdied_text.place((0,-75),True)
            restart_button.place(center=True)

            if restart_button.click():
                bird.place((0,-110),True)
                bird.down = 0
                bird.score = 0

                for wall in walls:
                    del wall
                walls.clear()

                bird.died = False


    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if started:
            if not bird.died:
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            bird.jump()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bird.jump()


    # draw to screen
    pygame.display.update()
    fps.tick(60)