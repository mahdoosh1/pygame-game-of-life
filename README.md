# pygame-game-of-life
a game of life simulator using pygame

# Keys
w: speed up   s: slow down
a: pause/unpause simulation
d: step once  r: fill with random
c: clear      mouse click: toggle cell
e: toggle between Conway's gol and DayNight gol

# Field
50x50 random area (can be changed in main.py) if you increase this, performance may differ
area type: looping (if cell goes off screen, cell will appear in other side)
fps: unlimited

# Engine
custom engine by me.
rule structure:
```
myrule = {
"type" = 8        # 8 is moore and 4 is von something
"survive" = "23",  # required neighborhoods to survive
"born" = "3",      # required neighborhoods to give birth
}
```
# About code
if you want to contribute you can create an issue
or make fork to fix something and pull request it to this repo

i know my code is messy, unoptimized and doesn't have comments.
