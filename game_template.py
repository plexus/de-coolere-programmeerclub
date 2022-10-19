import pygame

# Constanten
TITLE="Cool spel"
WINDOW_SIZE=(800,600)
BACKGROUND=(64,128,128)

# Variabelen
running = True

# Initialiseer het venster, gebeurt één keer aan het begin
def init_pygame():
  global window, clock
  window = pygame.display.set_mode(WINDOW_SIZE)
  clock = pygame.time.Clock()
  pygame.display.set_caption(TITLE)

# Teken het spelbord
def draw_graphics():
  window.fill(BACKGROUND)
  # <<<<< HIER >>>>>>>
  # pygame.draw.rect(window, (64,32,0), pygame.Rect(100,100,100,20), width=1, border_radius=2)

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
          # <<<<< HIER >>>>>>>
          # case pygame.K_LEFT:
          #   ...
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
