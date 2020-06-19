import pygame as pg
from button import Button
from gameplay import Gameplay

pg.init()
pg.font.init()

class GameIntro():
    
    def __init__(self):
        
        self.clock = pg.time.Clock()
        self.FPS = 15
        
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 210)
        
        self.WIDTH = self.HEIGHT = 600
        self.INTRO_BORDER_SIZE = 20
        self.BORDER_SIZE = 40
        
        self.PLAY_COORDX = self.WIDTH // 5
        self.QUIT_COORDX = (3 * self.WIDTH) // 5
        self.PLAY_COORDY = self.QUIT_COORDY = (3 * self.HEIGHT) // 4
        self.PLAY_WIDTH = self.QUIT_WIDTH = self.WIDTH // 5
        self.PLAY_HEIGHT = self.QUIT_HEIGHT = self.WIDTH // 10
        self.MESSAGES = {1: 'Play!', 2: 'Quit!'}
        
        
        
        self.display = pg.display.set_mode([self.WIDTH, self.HEIGHT])
        self.display.fill(self.WHITE)
        
        self.smallerFont = pg.font.SysFont('freesansbold.ttf', 30)
        self.largeFont = pg.font.SysFont('freesansbold.ttf', 45)
        
        
        self.BORDER_COORDINATES = {1: ((0,0), (self.WIDTH, self.BORDER_SIZE)),
                              2: ((0, self.BORDER_SIZE), (self.BORDER_SIZE,
                                                          self.HEIGHT)),
                              3: ((self.WIDTH - self.BORDER_SIZE, self.BORDER_SIZE), 
                                  (self.BORDER_SIZE, self.HEIGHT)),
                              4: ((0, self.WIDTH - self.BORDER_SIZE), 
                                  (self.WIDTH, self.BORDER_SIZE))}
        
    def text(self, surface, sizeFont, color, message, centerX, centerY):
        """
    
        Parameters
        ----------
        surface : pygame.Surface
            The Screen on which the game is played.
        sizeFont : pygame.font
            The font object that is displayed.
        color : tuple
            Global tuple object of R,G,B values.
        message : String
            Specific string to be displayed for the user.
        centerX : Integer
            x-coordinate of center of pygame.rect object.
        centerY : Integer
            y-coordinate of center of pygame.rect object.
    
        Returns
        -------
        Nothing returned; text object appears on pygame.Surface object.
    
        """
        
        text = sizeFont.render(message, True, color)
        rect = text.get_rect()
        rect.center = (centerX, centerY)
        surface.blit(text, rect)
    
    def button(self, surface, bgColor, textColor, bgnX, bgnY, 
           width, height, message, sizeFont):
        '''
        
        Parameters
        ----------
        surface : pygame.Surface
            The Screen on which the game is played.
        bgColor : tuple
            Color of the pygame.rect object.
        textColor : tuple
            Color of the pygame.font object.
        bgnX : Integer
            Top-left x-coordinate of the pygame.rect object.
        bgnY : Integer
            Top-left y-coordinate of the pygame.rect object.
        width : Integer
            Integer width (x-change in corners) of pygame.rect object.
        height : Integer
            Integer height (y-change in corners) of pygame.rect object.
        message : String
            Specific string to be displayed for the user.
        sizeFont : pygame.font
            The font object that is displayed.
    
        Returns
        -------
        Nothing returned; however, rectangle and text object are drawn 
        on the pygame.Surface object.
    
        '''
    
        pg.draw.rect(surface, bgColor, ((bgnX, bgnY), (width, height)))
        self.text(surface, sizeFont, textColor, message, 
            (bgnX + (width // 2)), (bgnY + (height // 2)))
    
    def menu(self):
        
        
        pg.draw.rect(self.display, self.BLUE, 
                     ((0,0), (self.WIDTH, self.INTRO_BORDER_SIZE)))
        pg.draw.rect(self.display, self.BLUE, 
                     ((0,0), (self.INTRO_BORDER_SIZE, self.WIDTH)))
        pg.draw.rect(self.display, self.BLUE, 
                     ((0, self.WIDTH - self.INTRO_BORDER_SIZE), 
                      (self.WIDTH, self.INTRO_BORDER_SIZE)))
        pg.draw.rect(self.display, self.BLUE, 
                     ((self.WIDTH - self.INTRO_BORDER_SIZE, 0), 
                      (self.INTRO_BORDER_SIZE, self.WIDTH)))
    
        self.text(self.display, self.largeFont, self.GREEN, 'Welcome to Snake!', 
             self.WIDTH // 2, self.HEIGHT // 3)
        self.text(self.display, self.smallerFont, self.RED, 
             'Click the below buttons to Play or Quit the game!', 
             self.WIDTH // 2, self.HEIGHT // 2)    
        
        play = Button(self.display, self.GREEN, self.WHITE,
                      self.PLAY_COORDX, self.PLAY_COORDY, self.PLAY_WIDTH,
                      self.PLAY_HEIGHT, self.MESSAGES[1], self.largeFont)
        end = Button(self.display, self.RED, self.WHITE,
                     self.QUIT_COORDX, self.QUIT_COORDY, self.QUIT_WIDTH, 
                     self.QUIT_HEIGHT, self.MESSAGES[2], self.largeFont)
        
        pg.display.flip()
        return play, end
    

def main():
    apple = pg.image.load('apple.png')
    pg.display.set_icon(apple)
    
    intro = GameIntro()
    game = Gameplay(intro.display, intro.WHITE, intro.GREEN, intro.WIDTH, intro.HEIGHT)
    play, end = intro.menu()
    
    played = False
    
    while True:
        event = pg.event.poll()
        
        if play.checkUpdates(intro.MESSAGES):
            game.setupDisplay(intro.display, intro.WHITE, 
                              [game.sky, game.side, game.side2, game.ground],
                              intro.BORDER_COORDINATES)
            played, length = game.gameLoop(intro.display, intro.WIDTH, intro.HEIGHT)
        
        elif end.checkUpdates(intro.MESSAGES):
            pg.quit()
        
        if event.type == pg.QUIT:
            pg.quit()
            
        if played: 
            
            main()
        
        intro.clock.tick(intro.FPS)
        

if __name__ == '__main__':
    main()
