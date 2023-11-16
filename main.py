print("loading libraries and functions...")
import pygame
import engine as gol
import random as rnd
from time import sleep
pygame.init()
field = [[rnd.randint(0,1) for _ in range(50)] for _ in range(50)]
y=len(field)
x=len(field[0])
screen_width, screen_height = 710, 710
scale_factor = screen_width / x
reverse_scale_factor = 1 / scale_factor
gridfilling = 9 / 10
speed = 1
unpaused = False
rule = gol.DAYNIGHT
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((30,30,30))
def drawframe(screen, field, updated = True, rule = gol.CONWAY):
	global scale_factor
	y=len(field)
	x=len(field[0])
	if updated:
		field = gol.nextframe(field,rule)
	for i in range(y):
		for j in range(x):
			c = field[i][j]
			pygame.draw.rect(screen, (255*c,255*c,255*c), pygame.Rect(j*scale_factor, i*scale_factor, gridfilling*scale_factor, gridfilling*scale_factor))
	return field
print("Ready.")
print("Hello! this is a game of life simulator.")
print("Keys:\n           w: speed up,\n           s: speed down")
print("           a: start simulation,\n           d: step once")
print("           c: clear,\n           r: fill with random")
print("           e: toggle between Conway's GOL and day and night gol")
drawframe(screen,field,False)
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			(mousex, mousey) = pygame.mouse.get_pos()
			clickx, clicky = int(mx*reverse_scale_factor), int(my*reverse_scale_factor)
			if clickx < x and clicky < y:
				field[clicky][clickx] = 1-field[clicky][clickx]
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
				if rule == gol.DAYNIGHT:
					rule = gol.CONWAY
				else:
					rule = gol.DAYNIGHT
			if event.key == pygame.K_r:
				field = [[rnd.randint(0,1) for _ in range(50)] for _ in range(50)]
				drawframe(screen,field,False)
				pygame.display.flip()
			if event.key == pygame.K_c:
				field = [[0 for _ in range(50)] for _ in range(50)]
				drawframe(screen,field,False)
				pygame.display.flip()
			if event.key == pygame.K_q:
				pygame.quit()
				quit()
	if unpaused:
		if speed >=1:
			for _ in range(int(speed)):
				field = drawframe(screen,field,rule=rule)
				pygame.display.flip()
		else:
			sleep(1/128/speed)
			field = drawframe(screen,field,rule=rule)
			pygame.display.flip()