import pygame as pg

class Button:
    
    def __init__(self, display, bgColor, textColor, bgnX, bgnY, 
           width, height, message, sizeFont):
        self.display = display
        self.bgColor = bgColor
        self.textColor = textColor
        self.bgnX = bgnX
        self.bgnY = bgnY
        self.width = width
        self.height = height
        self.message = message
        self.sizeFont = sizeFont
        
        self.drawButton(display, bgColor, bgnX, bgnY, width,
                   height, sizeFont, textColor, message)
    
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
            
    def drawButton(self, surface, bgColor, bgnX, bgnY, width,
                   height, sizeFont, textColor, message):
        """
        Parameters 
        ----------
        
        surface : pygame.Surface
            The Screen on which the game is played.
        sizeFont : pygame.font
            The font object that is displayed.
        bgColor : tuple
            Global tuple object of R,G,B values for background.
        textColor : tuple
            Global tuple object of R,G,B values for text.
        message : String
            Specific string to be displayed for the user.
        bgnY : Integer
            Left-most x-coordinate of pygame.rect object.
        centerY : Integer
            Top-most y-coordinate of center of pygame.rect object.
        width: Integer
            Integer width of the Button object.
            
        Returns
        -------
        None.
        """

        pg.draw.rect(surface, bgColor, ((bgnX, bgnY), (width, height)))
        self.text(surface, sizeFont, textColor, message, 
             (bgnX + (width // 2)), (bgnY + (height // 2)))
        
    def checkUpdates(self, messages):
        mouse = pg.mouse.get_pos()
        clicks = pg.mouse.get_pressed()
        
        xPos = mouse[0]
        yPos = mouse[1]
        
        if (self.bgnX <= xPos) and (xPos <= (self.bgnX + self.width)):
            if (self.bgnY <= yPos) and (yPos <= (self.bgnY + self.height)):    
                for click in clicks:
                    if click != 0:
                        return True
    