print("loading libraries and functions...")
import pygame
import engine as gol
import random as rnd
from time import sleep
render = gol.simulate
con = gol.WIREWORLD
dan = gol.DAYNIGHT
pygame.init()
field = [[0 for _ in range(20)] for _ in range(10)]
y=len(field)
x=len(field[0])
screen_width, screen_height = 710, 710
scale_factor = min(screen_width / x,screen_height / y)
reverse_scale_factor = 1 / scale_factor
states = 4
def rd(x): global states; return (x%2)*255/states
def gr(x): global states; return (x%2)*255/states
def bl(x): global states; return ((x/2)%2)*255/states
gridfilling = 9 / 10
speed = 1
unpaused = False
rule = con
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((30,30,30))
def drawframe(screen, field, updated = True, rule = gol.CONWAY):
    global scale_factor
    y=len(field)
    x=len(field[0])
    if updated:
        field = render(field,rule)
    for i in range(y):
        for j in range(x):
            c = field[i][j]
            pygame.draw.rect(screen, (rd(c),gr(c),bl(c)), pygame.Rect(j*scale_factor, i*scale_factor, gridfilling*scale_factor, gridfilling*scale_factor))
    return field
def flip(field):
    y=len(field)
    x=len(field[0])
    for i in range(y):
        for j in range(x):
            field[i][j] = not field[i][j]
    return field
print("""
Ready.
Hello! this is a game of life simulator.
Keys:\n           w: speed up,\n           s: speed down
           a: start simulation,\n           d: step once
           c: clear,\n           r: fill with random
           e: toggle between Conway's GOL and day and night gol
           f: flip colors       n: reverse rules (only rules not field,
           doesn't matter on day and night because it's symmetrical)
""")
drawframe(screen,field,False)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mousex, mousey) = pygame.mouse.get_pos()
            clickx, clicky = int(mousex*reverse_scale_factor), int(mousey*reverse_scale_factor)
            if clickx < x and clicky < y:
                field[clicky][clickx] = (field[clicky][clickx]+1)%states
                drawframe(screen,field,False)
                pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                field = drawframe(screen,field,rule=rule)
                pygame.display.flip()
            if event.key == pygame.K_a:
                unpaused = not unpaused
            if event.key == pygame.K_w:
                speed = speed * 2
            if event.key == pygame.K_s:
                speed = speed / 2
            if event.key == pygame.K_e:
                if rule in [dan,gol.revule(dan)]:
                    rule = con
                else:
                    rule = dan
            if event.key == pygame.K_r:
                field = [[rnd.randint(0,states-1) for _ in range(x)] for _ in range(y)]
                drawframe(screen,field,False)
                pygame.display.flip()
            if event.key == pygame.K_c:
                field = [[0 for _ in range(x)] for _ in range(y)]
                drawframe(screen,field,False)
                pygame.display.flip()
            if event.key == pygame.K_f:
                field = flip(field)
                rule = gol.revule(rule)
                drawframe(screen,field,False)
                pygame.display.flip()
            if event.key == pygame.K_n:
                rule = gol.revule(rule)
            if event.key == pygame.K_q:
                #pygame.quit()
                #quit()
                pygame.sfh()
    if unpaused:
        if speed >=1:
            for _ in range(int(speed)):
                field = drawframe(screen,field,rule=rule)
                pygame.display.flip()
        else:
            sleep(1/128/speed)
            field = drawframe(screen,field,rule=rule)
            pygame.display.flip()