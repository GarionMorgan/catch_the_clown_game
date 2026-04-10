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
CLOWN_ACCELERATION = 1

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

game_over_text = font.render("GAMEOVER", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Click anywhere to play again", True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2+64)

#set sound and music
click_sound = pygame.mixer.Sound("./catch_the_clown_assets/click_sound.wav")
miss_sound = pygame.mixer.Sound("./catch_the_clown_assets/miss_sound.wav")
pygame.mixer.music.load("./catch_the_clown_assets/ctc_background_music.wav")

#set images
background_image = pygame.image.load("./catch_the_clown_assets/background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

clown_image = pygame.image.load("./catch_the_clown_assets/clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

#main game loop
pygame.mixer.music.play(-1,0.0)
running = True
while running: 
    #check if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #a click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #the clown was clicked
            if clown_rect.collidepoint(mouse_x,mouse_y):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                #move clown in new direction
                previous_dx = clown_dx
                previos_dy = clown_dy
                while(previous_dx == clown_dx and previos_dy == clown_dy):
                    clown_dx = random.choice([-1,1])
                    clown_dy = random.choice([-1,1])

            #mised the clown
            else: 
                miss_sound.play()
                player_lives -= 1

    #move the clown
    clown_rect.x += clown_dx*clown_velocity
    clown_rect.y += clown_dy*clown_velocity

    #bounce the clown off the edges of display
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx = -1*clown_dx
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1*clown_dy

    #update hud
    score_text = font.render("Score: " + str(score), True, YELLOW)
    lives_text = font.render("Lives: " + str(player_lives), True, YELLOW)

    #check for gameover
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #pause game until player clicks, then reset
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #player wants to play again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTER_LIVES

                    clown_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1,1])
                    clown_dy = random.choice([-1,1])

                    pygame.mixer.music.play(-1,0.0)
                    is_paused = False

                #player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #blit background
    display_surface.blit(background_image, background_rect)

    #blit hud
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    #blit assets
    display_surface.blit(clown_image, clown_rect)

    #update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End game
pygame.quit()