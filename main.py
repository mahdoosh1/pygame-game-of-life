print("loading libraries and functions...")
import pygame
import engine as gol
import random as rnd
from time import sleep
pygame.init()
arr = [[rnd.randint(0,1) for _ in range(50)] for _ in range(50)]
y=len(arr)
x=len(arr[0])
sx, sy = 710, 710
sf = sx / x
rsf = 1 / sf
f = 9 / 10
spd = 1
p = False
rule = gol.DAYNIGHT
surface = pygame.display.set_mode((sx,sy))
surface.fill((30,30,30))
def drw(scrn, arr, upd = True, rule = gol.CONWAY):
	global sf
	y=len(arr)
	x=len(arr[0])
	if upd:
		arr = gol.nxt(arr,rule)
	for i in range(y):
		for j in range(x):
			c = arr[i][j]
			pygame.draw.rect(scrn, (255*c,255*c,255*c), pygame.Rect(j*sf, i*sf, f*sf, f*sf))
	return arr
print("Ready.")
print("Hello! this is a game of life simulator.")
print("Keys:\n           w: speed up,\n           s: speed down")
print("           a: start simulation,\n           d: step once")
print("           c: clear,\n           r: fill with random")
print("           e: toggle between Conway's GOL and day and night gol")
drw(surface,arr,False)
pygame.display.flip()
while True:
	for ev in pygame.event.get():
		if ev.type==pygame.QUIT:
			pygame.quit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			(mx, my) = pygame.mouse.get_pos()
			cx, cy = int(mx*rsf), int(my*rsf)
			if cx < x and cy < y:
				arr[cy][cx] = 1-arr[cy][cx]
				drw(surface,arr,False)
				pygame.display.flip()
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_d:
				arr = drw(surface,arr,rule=rule)
				pygame.display.flip()
			if ev.key == pygame.K_a:
				p = not p
			if ev.key == pygame.K_w:
				spd = spd * 2
			if ev.key == pygame.K_s:
				spd = spd / 2
			if ev.key == pygame.K_e:
				if rule == gol.DAYNIGHT:
					rule = gol.CONWAY
				else:
					rule = gol.DAYNIGHT
			if ev.key == pygame.K_r:
				arr = [[rnd.randint(0,1) for _ in range(50)] for _ in range(50)]
				drw(surface,arr,False)
				pygame.display.flip()
			if ev.key == pygame.K_c:
				arr = [[0 for _ in range(50)] for _ in range(50)]
				drw(surface,arr,False)
				pygame.display.flip()
			if ev.key == pygame.K_q:
				pygame.quit()
				quit()
	if p:
		if spd >=1:
			for _ in range(int(spd)):
				arr = drw(surface,arr,rule=rule)
				pygame.display.flip()
		else:
			sleep(1/128/spd)
			arr = drw(surface,arr,rule=rule)
			pygame.display.flip()