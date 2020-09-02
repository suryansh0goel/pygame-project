import pygame
import time
import random

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

car_img = pygame.image.load('output-onlinejpgtools.png')

def display_msg(text,center=(400,300),size=115,color=(255,0,0)):
    font = pygame.font.Font('freesansbold.ttf',size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.center = center
    display.blit(text_surface,text_rect)


def score(count):
    font = pygame.font.SysFont(None,30)
    text_surface = font.render('Dodged : '+str(count),True,(150,150,100))
    display.blit(text_surface,(0,0))


def game_intro():

    intro = True

    display.fill((200, 150, 50))

    display_msg('Sample Game', (400, 200), 100, (225, 250, 200))

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(display, (0, 255, 0), (200, 400, 100, 50))
        pygame.draw.rect(display, (255, 0, 0), (500, 400, 100, 50))

        if 200<mouse[0]<300 and 400<mouse[1]<450:
            pygame.draw.rect(display,(0,150,0),(200,400,100,50))
            if click[0] == 1:
                game_loop()
        if 500<mouse[0]<600 and 400<mouse[1]<450:
            pygame.draw.rect(display,(150,0,0),(500, 400, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()

        display_msg('Play',(250,425),40,(255,255,255))
        display_msg('Quit',(550,425),40,(255,255,255))


        pygame.display.update()


def game_loop():

    x = 800 * 0.1
    y = 600 * 0.4
    xc = 0
    yc = 0
    bx = 1600
    by = random.randrange(0,550)
    crashed = False
    dodged = 0

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yc = -5
                if event.key == pygame.K_DOWN:
                    yc = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yc = 0

        y += yc
        bx -= 10

        display.fill((255,255,255))
        display.blit(car_img, (x, y))
        pygame.draw.rect(display, (0, 0, 0), [bx, by, 100, 50])
        score(dodged)

        if y<0 or y>545:
            display_msg('You Crashed')
            pygame.display.update()
            time.sleep(2)
            game_loop()

        if bx == -100:
            bx = 1000
            by = random.randrange(0,550)
            dodged += 1

        if x+118 > bx+10 and x+10 < bx+100:
            if (y > by and y < by+50) or (y+55 > by and y+55 < by + 50):
                display_msg('You Crashed')
                pygame.display.update()
                time.sleep(2)
                game_loop()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
