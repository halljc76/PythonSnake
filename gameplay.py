import pygame as pg
import random

class Gameplay():
    
    """
    Update (Jun 18): Cleanup Time!
    """
    
    
    def __init__(self, display, bgColor, snakeColor, width, height):
        assert width == height
        
        self.display = display
        self.bgColor = bgColor
        self.snakeColor = snakeColor
        self.width = width
        self.height = height
        
        
        
        self.sky = pg.image.load('sky.png')
        self.side = pg.image.load('side.png')
        self.side2 = pg.transform.flip(self.side, True, False)
        self.ground = pg.image.load('ground.png')
        
    def setupDisplay(self, display, bgColor, images, coordinates):
        
        display.fill(bgColor)
        
        for i in range(len(images)):
            self.drawImages(display, images[0], bgColor, coordinates[1])
            self.drawImages(display, images[1], bgColor, coordinates[2])
            self.drawImages(display, images[2], bgColor, coordinates[3])
            self.drawImages(display, images[3], bgColor, coordinates[4])
        
        pg.display.flip()
    
    def drawImages(self, surface, image, color, location):
        rect = pg.draw.rect(surface, color, location)
        surface.blit(image, rect)
    
    def randomAppleCoordinates(self, snakeBody, allPositions):
        coordinates = random.choice(allPositions)
        while coordinates in snakeBody:
            coordinates = random.choice(allPositions)
        
        return coordinates[0], coordinates[1]
    
    def makeSnake(self, display, head, snakeBody, size, direction):
        
        GREEN = (0, 255, 0)
        
        directions = {"Right": pg.transform.rotate(head, 0),
                      "Left": pg.transform.rotate(head, -180),
                      "Up": pg.transform.rotate(head, 90),
                      "Down": pg.transform.rotate(head, 270)}
        
        head = directions[direction]
        
        display.blit(head, (snakeBody[-1][0], snakeBody[-1][1]))
        
        for XnY in snakeBody[:-1]:
            pg.draw.rect(display, GREEN, ((XnY[0], XnY[1]), (size, size)))
    
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
     
    def gameLoop(self, display, width, height):
        
        """
         Parameters
        ----------
        display : pygame.Surface
            The Screen on which the game is played.
        width : Integer
            The width of the display.
        height : Integer
            The height of the display.
        """
        
        self.smallerFont = pg.font.SysFont('freesansbold.ttf', 30)
        clock = pg.time.Clock()
        FPS = 15
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        snakeAndAppleSize = 20
        
        head = pg.image.load('snakeHead.png').convert_alpha()
        apple = pg.image.load('apple.png')
        
        
        snakeHeadDirec = "Right"
        isGameOver = False
        
        bgnXCoor = width // 3
        bgnYCoor = height // 3
        deltaX = snakeAndAppleSize
        deltaY = 0
        
        borderX = borderY = 40
        
        snakeBody = []
        length = 1
        
        allPositions = []
        
        for i in range(borderX, width - borderX, snakeAndAppleSize):
            for j in range(borderY, height - borderY, snakeAndAppleSize):
                allPositions.append([i, j])
                
        
        
        appleXCoor, appleYCoor = Gameplay.randomAppleCoordinates(self, snakeBody, allPositions)
        
        while not isGameOver:
            event = pg.event.poll()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    snakeHeadDirec = "Left"
                    deltaX = -(snakeAndAppleSize)
                    deltaY = 0
                
                elif event.key == pg.K_RIGHT:
                    snakeHeadDirec = "Right"
                    deltaX = snakeAndAppleSize
                    deltaY = 0
                
                elif event.key == pg.K_UP:
                    snakeHeadDirec = "Up"
                    deltaX = 0
                    deltaY = -(snakeAndAppleSize)
                
                elif event.key == pg.K_DOWN:
                    snakeHeadDirec = "Down"
                    deltaX = 0
                    deltaY = snakeAndAppleSize
            
            if (bgnXCoor < borderX) or (bgnYCoor < borderY) or (bgnXCoor >= width - borderX) or (bgnYCoor >= height - borderY):
                    isGameOver = True
            
            bgnXCoor += deltaX
            bgnYCoor += deltaY
            
            self.drawImages(display, apple, WHITE, ((appleXCoor, appleYCoor), (snakeAndAppleSize, snakeAndAppleSize)))
            
            
            snakeHead = []
            snakeHead.append(bgnXCoor)
            snakeHead.append(bgnYCoor)
            
            snakeBody.append(snakeHead)

            if len(snakeBody) > length:
                del snakeBody[0]
            
            for piece in snakeBody[:-1]:
                if piece == snakeHead:
                    isGameOver = True
            
            self.makeSnake(display, head, snakeBody, snakeAndAppleSize, snakeHeadDirec)
            
            for position in allPositions:
                if position not in snakeBody:
                    if position != [appleXCoor, appleYCoor]:
                        pg.draw.rect(self.display, WHITE, ((position[0], position[1]), (snakeAndAppleSize, snakeAndAppleSize)))
            
            pg.display.set_caption('Score: ' + str(length - 1))
            pg.display.flip()
            
            
            if bgnXCoor == appleXCoor:
                if bgnYCoor == appleYCoor:
                    appleXCoor, appleYCoor = Gameplay.randomAppleCoordinates(self, snakeBody, allPositions)
                    self.drawImages(display, apple, WHITE, ((appleXCoor, appleYCoor), (snakeAndAppleSize, snakeAndAppleSize)))
                    length += 1
                    
            
            clock.tick(FPS)
        
        
        
        return isGameOver, length
            
            
