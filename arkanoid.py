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
  # <<<<< HIER >>>>>>>
  # pygame.Rect(x,y,hoogte,breedte)
  rect = pygame.Rect(paddle["x"], paddle["y"], paddle["breedte"], paddle["hoogte"])
  pygame.draw.rect(window, paddle["stroke"], rect, width=5, border_radius=2)

# Verwerk "events" (gebeurtenissen) van toetsenbord of muis
def handle_events():
  global running
  for event in pygame.event.get():
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

      # case pygame.MOUSEBUTTONDOWN:
      #   ...

def main():
  init_pygame()
  while running:
    clock.tick(60) # 60 fps
    handle_events()
    draw_graphics()
    pygame.display.update()

main()
