import pygame, random

#initialzie pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTER_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTER_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1,1])
clown_dy = random.choice([-1,1])

#set colors
BLUE = (1,175,209)
YELLOW = (248,231,28)

#set font
font = pygame.font.Font("./catch_the_clown_assets/Franxurter.ttf", 32)

#set text
title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50,10)

score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH -50, 10)

lives_text = font.render("Lives: " + str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH -50, 50)
#set sound and music

#set images

#main game loop
running = True
while running: 
    #check if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#End game
pygame.quit()