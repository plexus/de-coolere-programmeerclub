import pygame

# https://www.pygame.org/docs/

# Constanten
TITLE="Arkanoid"
WINDOW_SIZE=(1000,600)
BACKGROUND=(64,128,128)

# Variabelen
running = True
paddle = {"x": 100,
          "y": 500,
          "breedte": 150,
          "hoogte": 20,
          "fill": (100,0,0),     # kleur van binnenkant
          "stroke": (0,0,100)}   # kleur van lijn

ball = {"x": 200,
        "y": 200,
        "radius": 30,
        "fill": (0,100,0),
        "velocity": {"x": 5, "y": 5}}

# Initialiseer het venster, gebeurt één keer aan het begin
def init_pygame():
  global window, clock
  window = pygame.display.set_mode(WINDOW_SIZE)
  clock = pygame.time.Clock()
  pygame.display.set_caption(TITLE)
  pygame.key.set_repeat(1, 5)

# Teken het spelbord
def draw_graphics():
  window.fill(BACKGROUND)
  # Teken paddle
  rect = pygame.Rect(paddle["x"], paddle["y"], paddle["breedte"], paddle["hoogte"])
  pygame.draw.rect(window, paddle["stroke"], rect, width=5, border_radius=2)
  # Teken bal
  pygame.draw.circle(window, ball["fill"], [ball["x"], ball["y"]], ball["radius"])

def update_ball(ball):
  ball["x"] = ball["x"] + ball["velocity"]["x"]
  ball["y"] = ball["y"] + ball["velocity"]["y"]

def bots_x(ball):
  ball["velocity"]["x"]*=-1
  ball["x"]+=ball["velocity"]["x"]

def bots_y(ball):
  ball["velocity"]["y"]*=-1
  ball["y"]+=ball["velocity"]["y"]

def collission_check(ball):
  if ball["x"]-ball["radius"] <= 0 or ball["x"]+ball["radius"] >= WINDOW_SIZE[0]:
    bots_x(ball)
  elif ball["y"]-ball["radius"] <= 0:
    bots_y(ball)
  elif ball["y"]+ball["radius"] >= paddle["y"] and ball["x"] >= paddle["x"] and ball["x"] < paddle["x"]+paddle["breedte"]:
    bots_y(ball)
  elif ball["y"]+ball["radius"] >= WINDOW_SIZE[1]:
    ball["velocity"]={"x": 0, "y": 0}

# Verwerk "events" (gebeurtenissen) van toetsenbord of muis
def handle_events():
  global running,ball
  for event in pygame.event.get():
    print(event)
    match event.type:
      # venster sluiten
      case pygame.QUIT:
        running = False

      # toetsenbord
      case pygame.KEYDOWN:
        match event.key:
          case pygame.K_ESCAPE:
            running = False

          case pygame.K_LEFT:
            if paddle["x"] > 0:
              paddle["x"] = paddle["x"]-5

          case pygame.K_RIGHT:
            if paddle["x"] < WINDOW_SIZE[0]-paddle["breedte"]:
              paddle["x"] = paddle["x"]+5

          case pygame.K_x:
            bots_x(ball)
          case pygame.K_c:
            bots_y(ball)

      # case pygame.MOUSEBUTTONDOWN:
      #   ...

def main():
  global ball   #<------
  init_pygame()
  while running:
    clock.tick(60) # 60 fps
    handle_events()
    update_ball(ball)   #<--------
    collission_check(ball)
    draw_graphics()
    pygame.display.update()

main()
