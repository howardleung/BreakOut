# I - IMPORT AND INITIALIZE
import pygame, BreakSprites, time
pygame.init()
screen = pygame.display.set_mode((640, 480))
     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # DISPLAY
    pygame.display.set_caption("Super Break-out!")
     
    # ENTITIES
    background = pygame.image.load('dirt.png')
    background = background.convert()
    cover = pygame.image.load('cover.png')
    cover = cover.convert()
    screen.blit(background, (0, 0))
    mySystemFont = pygame.font.Font("The Goldsmith_Vintage.ttf", 50)
    labelstart = mySystemFont.render("PRESS SPACE", 1, (0, 0, 0))  
    label1 = mySystemFont.render("Good Game!", 1, (0, 0, 0)) 
    

    #pygame.mixer.music.load("music.mp3")
    #pygame.mixer.music.set_volume(0.3)
    #pygame.mixer.music.play(-1)
       
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Players
    score_keeper = BreakSprites.ScoreKeeper()
    ball = BreakSprites.Ball(screen)
    player = BreakSprites.Player(screen,'bed.png')
    left_endzone = BreakSprites.EndZone(screen,(19,240),"endzone.png")
    right_endzone = BreakSprites.EndZone(screen,(621,240),"endzone.png")
    top_endzone = BreakSprites.EndZone(screen,(320,20),"topendzone.png")
    bricks = []
    for row in range(18):
        bricks.append(BreakSprites.Brick(screen, "purple.png", 42, 42+31*row, 6))
        bricks.append(BreakSprites.Brick(screen, "red.png", 57, 42+31*row, 5))
        bricks.append(BreakSprites.Brick(screen, "yellow.png", 72, 42+31*row, 4))
        bricks.append(BreakSprites.Brick(screen, "orange.png", 87, 42+31*row, 3))
        bricks.append(BreakSprites.Brick(screen, "green.png", 102, 42+31*row, 2))
        bricks.append(BreakSprites.Brick(screen, "blue.png", 117, 42+31*row, 1))
    bricksGroup = pygame.sprite.Group(bricks)    
    allSprites = pygame.sprite.OrderedUpdates(left_endzone, \
                                     right_endzone, top_endzone, ball, player, bricks, score_keeper)

    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    gg = False
    start = False
    add = 0
    bricks_remain = 108
    once = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
    
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if start:
                    if event.key == pygame.K_LEFT:
                        player.moveleft()
                
                    if event.key == pygame.K_RIGHT:
                        player.moveright()
                if not start:
                    if event.key == pygame.K_SPACE:
                        start = True
                        labelstart = mySystemFont.render(" ", 1, (0, 0, 0))  
                        ball.start()
            elif event.type == pygame.KEYUP:
                player.stop()

 
 

 
        # Check if ball hits left or right endzone
        if ball.rect.colliderect(left_endzone) or ball.rect.colliderect(right_endzone):
            ball.change_x()
             
                     
        # Check if ball hits Player or top endzone
        if ball.rect.colliderect(player):
            ball.start()
        if ball.rect.colliderect(top_endzone):
            ball.change_y()
        if pygame.sprite.spritecollide(ball, bricksGroup, False):
            ball.change_y()

        for hitbrick in pygame.sprite.spritecollide(ball, bricksGroup, True):
            score_keeper.scored(hitbrick.get_point())
            bricks_remain -= 1  
            
        if ball.dead(): 
            start = False
            #lives - 1
            ball.reset()
            player.stop()
            player.reset()
            score_keeper.died()
        if bricks_remain <= 54:
            player.half(once)
            once = False
        if bricks_remain == 0 or score_keeper.checkalive():
            gg = True
            
        # REFRESH SCREEN
        
        if not gg:
            screen.blit(labelstart, (220,220))  
            if start:
                screen.blit(cover, (163,181))
            allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen) 
  
        if gg:
            
            screen.blit(labelstart, (220,220))  
            if start:
                screen.blit(cover, (163,181))
            allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen) 
            keepGoing = False
            screen.blit(label1, (220,220))
        pygame.display.flip()
        
         
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window
    if gg:
        time.sleep(3)    
    pygame.quit()     
     
# Call the main function
main()    