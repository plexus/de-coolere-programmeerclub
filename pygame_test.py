import pygame

pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False

background=(200,100,0)

while not exit:
    canvas.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas, (100,200,0),
                     pygame.Rect(30,30,60,60))

    pygame.display.update()
