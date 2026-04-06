import pygame

#initialzie pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

#main game loop
running = True
while running: 
    #check if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#End game
pygame.quit()