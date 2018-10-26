import pygame
import time
import random

# MUSIC INITIALIZING

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

# PLAY BACKGROUND MUSIC

pygame.mixer.music.load("Low-Rider-JFA.mp3")
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(-1)


score = []

display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73
car_height = 127

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()


carImg = pygame.image.load('/Users/taylorball/Downloads/8_bit_racer.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def score_print(num):
    stime = time.localtime(time.time())[5]
    font = pygame.font.Font('freesansbold.ttf', 100)
    gameDisplay.blit(font.render(num, True, (0, 0, 0)), (80, 90))
    pygame.display.update()
    if time.localtime(time.time())[5]>stime:
        game_loop()




def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def road(roadx, roady, roadw, roadh, roadc):
    pygame.draw.rect(gameDisplay, roadc, [roadx, roady, roadw, roadh])

def road2(roadx2, roady2, roadw2, roadh2, roadc2):
    pygame.draw.rect(gameDisplay, roadc2, [roadx2, roady2, roadw2, roadh2])


def car(x, y):
    gameDisplay.blit(carImg,(x,y))


def text_objects(text,font):
    textSurface = font.render(text, True)
    return textSurface, textSurface.get_rect()


def message_display(text):
    stime=time.localtime(time.time())[5]
    font = pygame.font.Font('freesansbold.ttf', 115)
    gameDisplay.blit(font.render(text, True, (255, 0, 0)), (0, 0))
    pygame.display.update()
    if time.localtime(time.time())[5]>stime:
        game_loop()


def crash():
    message_display('You Crashed!')
    if len(score) > 0:
        score_print('You Scored ' + str(score[-1]) + '!')




def game_loop():
    x = (display_width * 0.47)
    y = (display_height * 0.7)


    x_change = 0

    road_startx = display_width/2 -100
    road_starty = -600
    road_speed = 4
    road_width = 20
    road_height = display_height * 100

    road_startx2 = display_width / 2 + 100
    road_starty2 = -600
    road_speed2 = 4
    road_width2 = 20
    road_height2 = display_height * 100

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0


    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change

        gameDisplay.fill(white)

        # road(roadx, roady, roadw, roadh, roadc)
        road(road_startx, road_starty, road_width, road_height, black)
        road_starty += road_speed

        # road2(roadx2, roady2, roadw2, roadh2, roadc2)
        road(road_startx2, road_starty2, road_width2, road_height2, black)
        road_starty2 += road_speed2


        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, red)
        thing_starty += thing_speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if road_starty2 > display_height:
            road_starty2 = 0 - road_height
            road_startx2 = display_width/2 + 100
            road_speed2 += 1

        if road_starty > display_height:
            road_starty = 0 - road_height
            road_startx = display_width/2 - 100
            road_speed += 1

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            score.append(dodged)



        if collision(x, y, car_width, car_height, thing_startx, thing_starty, thing_width, thing_height):
            crash()




        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()




