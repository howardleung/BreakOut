import pygame, random

class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.image.load('ball.png')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.__screen = screen
        self.rect.center = (self.__screen.get_width()/2,self.__screen.get_height()-62)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.__screen = screen
        self.__dx = 0
        self.__dy = 0
        
    def reset(self):
        self.rect.center = (self.__screen.get_width()/2,self.__screen.get_height()-62)
        self.__dx = 0
        self.__dy = 0
    def dead(self):
        if self.rect.top > self.__screen.get_height():
            return True
        else:
            return False
    def start(self):
        '''Starts moving the ball'''
        self.__dx = random.randrange(-6,7)
        self.__dy = random.randrange(-6,-3)

    def change_x(self):
        '''This method causes the x direction of the ball to reverse.'''
        self.__dx = -self.__dx
   
    def change_y(self):
        '''This method causes the y direction of the ball to reverse.'''
        self.__dy = -self.__dy

    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''

        self.rect.left += self.__dx

        self.rect.top += self.__dy

class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our endzone.'''
    def __init__(self, screen, position, picture):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes of the endzone.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the endzone
        self.image = pygame.image.load(picture)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = position
        

class Brick(pygame.sprite.Sprite):
    '''This class defines the sprite for our brick.'''
    def __init__(self, screen, picture, top, left, point):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes of the brick.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the Ball
        self.image = pygame.image.load(picture)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.top = top
        self.rect.left = left
        self.__point = point
    def get_point(self):
        return self.__point
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for our player.'''
    def __init__(self, screen, picture):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and direction of the player.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the player
        self.image = pygame.image.load(picture)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (320,440)    
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.__screen = screen
        self.__dx = 0
    def half(self,once):
        # Set the image and rect attributes for the player
        if once:
            self.__init__(self.__screen,'smallbed.png')

 
        
    def reset(self):
        self.rect.center = (320,440) 
        
    def moveright(self):
        self.__dx = 7
        
    def moveleft(self):
        self.__dx = -7
        
    def stop(self):
        self.__dx = 0
            
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        if ((self.rect.left > 39) and (self.rect.right < 601)) or ((self.rect.right >= 602) and \
           (self.__dx < 0)) or ((self.rect.left <= 39) and (self.__dx > 0)):
            self.rect.left += self.__dx
      #  print self.rect.left
      #  print self.rect.right

            
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.Font("The Goldsmith_Vintage.ttf", 30)
        self.__score = 0
        self.__lives = 3
         
    def scored(self, point):
        '''This method adds one to the score for the player'''
        self.__score += point
    def died(self):
        self.__lives -= 1
    def checkalive(self):
        if self.__lives <= 0:
            return True
        else: 
            return False
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Score: " + str(self.__score) + "     Lives: " + str(self.__lives)
        self.image = self.__font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 20)