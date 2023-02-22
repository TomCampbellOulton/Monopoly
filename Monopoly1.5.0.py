import pygame
pygame.init()
# Last number means monitor 0 (On the left, in my case ;P)
screen = pygame.display.set_mode((1920, 1010),0,32,1)
clock = pygame.time.Clock()
running = True
input_boxes = []
bgColour = (25,25,25)
boardColour = (255,255,255)
COLOUR_INACTIVE = pygame.Color('lightskyblue3')
COLOUR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)




# properties = [ [Colour, Cost, Owner, NumberOfHouses, [Rent] , CostOfHouses, mortgageValue, mortgaged] ]
# Properties Data
pd =[
    ['GO', 0, 'Bank', 0, [], 0, False],
    ['Brown', 60, 'Bank', 0, [2, 10, 30, 90, 160, 250], 50, 30, False] ,
    ['Community Chest', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Brown', 60, 'Bank', 0, [4, 20, 60, 180, 320, 350], 50, 30, False] ,
    ['income tax', 0, 'Bank', 0, [200], 0, 0, False] ,
    ['transport', 200, 'Bank', 0, [25, 50, 100, 200, 200], 0, 100, False] ,
    ['Light Blue', 100, 'Bank', 0, [6, 30, 90, 270, 400, 550], 50, 50, False] ,
    ['chance', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Light Blue', 100, 'Bank', 0, [6, 30, 90, 270, 400, 550], 50, 50, False] ,
    ['Light Blue', 120, 'Bank', 0, [8, 40, 100, 300, 450, 600], 50, 60, False] ,
    ['Jail', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Pink', 140, 'Bank', 0, [10, 50, 150, 450, 625, 750], 100, 70, False] ,
    ['Pink', 140, 'Bank', 0, [10, 50, 150, 450, 625, 750], 100, 70, False] ,
    ['Utility', 150, 'Bank', 0, [4, 10], 0, 75, False] ,
    ['Pink', 160, 'Bank', 0, [12, 60, 180, 500, 700, 900], 100, 80, False] ,
    ['transport', 200, 'Bank', 0, [25, 50, 100, 200, 200], 0, 100, False] ,
    ['Orange', 180, 'Bank', 0, [14, 70, 200, 550, 750, 950], 100, 90, False] ,
    ['community chest', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Orange', 180, 'Bank', 0, [14, 70, 200, 550, 750, 950], 100, 90, False] ,
    ['Orange', 200, 'Bank', 0, [16, 80, 200, 600, 800, 1000], 100, 100, False] ,
    ['Free Parking', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Red', 220, 'Bank', 0, [18, 90, 250, 700, 875, 1050], 150, 110, False] ,
    ['chance', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Red', 220, 'Bank', 0, [18, 90, 250, 700, 875, 1050], 150, 110, False] ,
    ['Red', 240, 'Bank', 0, [20, 100, 300, 750, 925, 1100], 150, 120, False] ,
    ['transport', 200, 'Bank', 0, [25, 50, 100, 200, 200], 0, 100, False] ,
    ['Yellow', 260, 'Bank', 0, [22, 110, 330, 800, 975, 1150], 150, 130, False] ,
    ['Yellow', 260, 'Bank', 0, [22, 110, 330, 800, 975, 1150], 150, 130, False] ,
    ['Utility', 150, 'Bank', 0, [4, 10], 0, 75, False] ,
    ['Yellow', 280, 'Bank', 0, [24, 120, 360, 850, 1025, 1200], 150, 140, False] ,
    ['Go To Jail', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Green', 300, 'Bank', 0, [26, 130, 390, 900, 1100, 1275], 200, 150, False] ,
    ['Green', 300, 'Bank', 0, [26, 130, 390, 900, 1100, 1275], 200, 150, False] ,
    ['community chest', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Green', 320, 'Bank', 0, [28, 150, 450, 1000, 1200, 1400], 200, 160, False] ,
    ['transport', 200, 'Bank', 0, [25, 50, 100, 200, 200], 0, 100, False] ,
    ['chance', 0, 'Bank', 0, [], 0, 0, False] ,
    ['Dark Blue', 350, 'Bank', 0, [35, 175, 500, 1100, 1300, 1500], 200, 175, False] ,
    ['income tax', 0, 'Bank', 0, [100], 0, 0, False] ,
    ['Dark Blue', 400, 'Bank', 0, [50, 200, 600, 1400, 1700, 2000], 200, 200, False]]

# Simple Base Plate to add new players
basePlateForNewPlayers = [1500, 0, [0,0], False, True]
# List of all possible Player Names
#playersNames = ["Cat", "Dog", "Ship", "Car", "Boot", "Hat"]
playerCoords={"Purple":[1336, 893], "Red":[1366, 893], "Orange":[1336, 923], "Blue":[1366, 923]}
playersNames = ["Bank", "Purple", "Red", "Orange", "Blue", "Free  Parking"]






def displayMainMenu():
    # Make a green box
    surface = pygame.Surface((1920,1010))
    surface.fill(COLOUR_ACTIVE)  
    screen.blit(surface, (0,0))
    # Write the message
    writeText("Main Menu", 770,210, fontSize=90)
    

    surface = pygame.Surface((125,40))
    surface.fill((250,0,250))  
    screen.blit(surface, (770, 410))
    newGameButton = Button("New Game", (770, 410), (125,40), buttonType="NewGame")
    newGameButton.show()

    return newGameButton

class InputBox:

    def __init__(self, x, y, w, h, bgColour, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.colour = bgColour
        self.text = text
        self.pos = (x,y,w,h)
        self.txt_surface = FONT.render(text, True, self.colour)
        self.active = False
        self.name = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.colour = COLOUR_ACTIVE if self.active else COLOUR_INACTIVE
        if event.type == pygame.KEYDOWN:
            entered = False
            if self.active:
                if event.key == pygame.K_RETURN:
                    t = self.text
                    self.text = ''
                    surface = pygame.Surface((self.rect.w, self.pos[3]))
                    surface.fill((0,250,250))  
                    screen.blit(surface, (self.pos[0], self.pos[1]))  
                    entered = True
                    try:
                        t = int(t)
                    except:
                        pass
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    t = self.text
                else:
                    self.text += event.unicode
                    t = self.text
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.colour)

            if entered:
                return t
            else:
                return ""
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Clean the window
        surface = pygame.Surface((self.rect.w, self.pos[3]))
        surface.fill((0,250,250))  
        screen.blit(surface, (self.pos[0], self.pos[1]))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, 2)
        pygame.display.update()

    def getName(self):
        return self.name

def response(message):
    print(message)

def showTextBox(message):
    # Make a green box
    surface2 = pygame.Surface((400,300))
    surface2.fill((0,250,0))  
    screen.blit(surface2, (760,400))
    # Write the message
    writeText(message, 770,410)
    buttons = []
    # Accept Button
    b1 = Button("Accept :(", (760,650), (400,50), buttonType="AcceptButton")

    # Add the close button
    surface2 = pygame.Surface((20,20))
    surface2.fill((250,0,0))  
    screen.blit(surface2, (1140,400))
    # Write the X
    writeText("X", 1143,401, fontSize=30)
    b2 = Button("", (1140,400), (20,20), buttonType="CloseButton")

    b1.show()
    b2.show()
    buttons.append(b1)
    buttons.append(b2)
    closed = False
    while not closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for b in buttons:
                wants = b.click(event)
                if wants == "CloseButton" or wants == "AcceptButton":
                    # Close the window
                    clearScreen(561,110, 755,755,(255,255,255))
                    pygame.display.update()
                    closed = True

def writeText(text, x, y, fontSize=30, fontColour="White", fontName = None):
    # Need to format the text to a manageable size so it doens't 
    # flow over, past the edge of the textbox
    message = splitMessageToManageableSizeChunks(text)
    ychange = fontSize+5
    for i in range(len(message)):
        font = pygame.font.SysFont(fontName,fontSize)
        img = font.render(message[i], True, fontColour)
        screen.blit(img,(x,y+ychange*i))

def splitMessageToManageableSizeChunks(message, limit=35):
    listOfChunks = []
    messageCopy = message
    if len(message) > limit:
        while len(messageCopy) > limit:
            i=0
            while messageCopy[limit+i] != " ":
                i-=1
            
            if messageCopy[0] == " ":
                littleChunk = messageCopy[1:limit+i]
            else:
                littleChunk = messageCopy[:limit+i]
            messageCopy = messageCopy[limit+i:]
            listOfChunks.append(littleChunk)
    listOfChunks.append(messageCopy)

    return listOfChunks

class Button:
    def __init__(self, text, pos, size, buttonType = "",fontSize=30, textColour = (255,255,255), tileName="",tileNum=0):
        self.x, self.y = pos
        self.upperBoundX, self.upperBoundY = self.x + size[0], self.y + size[1]
        self.font = pygame.font.SysFont("Arial", fontSize)
        self.buttonName = buttonType
        self.text = self.font.render(text, 1, textColour)
        self.size = size
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.text, (pos))
        self.tileName=tileName
        self.tileNum = tileNum
        self.position = pos

        if buttonType == "AddOrRemove1":
            self.addOrRemove = "NotSet1"
        elif buttonType == "AddOrRemove2":
            self.addOrRemove = "NotSet2"
        else:
            self.addOrRemove = "NA"

    def getPosition(self):
        return self.position

    def getTileName(self):
        return self.tileName

    def getTileNum(self):
        return self.tileNum

    def show(self):
        screen.blit(self.text, (self.x, self.y))
        pygame.display.update()

    def getAddOrRemove(self):
        return self.addOrRemove

    def changeAddOrRemove(self):
        if self.getAddOrRemove() == "NotSet1" or self.getAddOrRemove() == "Remove1":
            self.addOrRemove = "Add1"
        elif self.getAddOrRemove() == "Add1":
            self.addOrRemove = "Remove1"
        elif self.getAddOrRemove() == "NotSet2" or self.getAddOrRemove() == "Remove2":
            self.addOrRemove = "Add2"
        elif self.getAddOrRemove() == "Add2":
            self.addOrRemove = "Remove2"
        else:
            print("What? Error on line 261 :c")

    def click(self, event):
        # If the mouse clicks the button
        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() and event.button == 1:
                if (self.x <= x and self.upperBoundX >= x) and (self.y <= y and self.upperBoundY >= y):
                    if self.addOrRemove != "NA":
                        self.changeAddOrRemove()
                    
                    return self.buttonName
                        

def removeWindow(window=""):
    #if window == "TextBox":
     #   blankScreen = pygame.Surface((400,300))
      #'  blankScreen.fill((0,0,0))
       # screen.blit(blankScreen, (760,400))
        #pygame.display.update()
    buttons = displayMainBoard([])
    return buttons

def showInfoBox(tileNum, propertiesData):
    tileData = propertiesData[tileNum]
    colour, cost, rentPrices, houseCost, mortgageValue = tileData[0], tileData[1], tileData[4], tileData[5], tileData[6]

    # Define Colours rq
    if True:
        brown = (150,77,0)  #1,3
        lightBlue = (0,170,254) # 6,8,9
        pink = (221,66,168) # 12,14,15
        orange = (255,145,0) # 17,19,20
        red = (255,0,0) # 22,24,25
        yellow = (255,255,0) # 27,28,30
        green = (0,100,31) # 32,33,35
        darkBlue = (0,0,145) # 38,40

        if colour == "Brown":
            colourForBox = brown
        elif colour == "Light Blue":
            colourForBox = lightBlue
        elif colour == "Pink":
            colourForBox = pink
        elif colour == "Orange":
            colourForBox = orange
        elif colour == "Red":
            colourForBox = red
        elif colour == "Yellow":
            colourForBox = yellow
        elif colour == "Green":
            colourForBox = green
        elif colour == "Dark Blue":
            colourForBox = darkBlue
        else: # e.g. transport, utility
            colourForBox = (255,255,255)


    # Clear the inside  box
    clearScreen(561,110, 755,755,(255,255,255))
    # Show the Card Bit
    if True:
        # Top - 300 down and 400 wide
        # Create Screen
        surface = pygame.Surface((755,755))
        # Make it white
        surface.fill((255,255,255))
        # Top Of Info Card
        pygame.draw.rect(surface, (255,145,0), (252,177, 250,3))

        # Bottom Of INfo Card
        pygame.draw.rect(surface, (255,145,0), (252,577, 250,3))

        # Left of Info Card
        pygame.draw.rect(surface, (255,145,155), (252,177, 3,400))
        # Right of Info Card
        pygame.draw.rect(surface, (255,145,155), (502,177, 3,403))
        
        # Inner Border Of Info Card
        pygame.draw.rect(surface, (255,170,0), (252,219, 250,3))
        # Colour of Info Card
        pygame.draw.rect(surface, colourForBox, (255,180, 247,39))

        # Red Box for the X Button
        pygame.draw.rect(surface, (255,0,0), (463,180, 39,39))

    screen.blit(surface,(561,110))

    # Write the data
    #cost, rentPrices, houseCost, mortgageValue
    x= 820
    writeText(f"Cost: {cost}", x,389, fontColour="Red")
    
    if len(rentPrices) == 6: # If it's a normal tile basically
        writeText(f"Base Rent: {rentPrices[0]}", x,419, fontColour="Red")
        writeText(f"1 House: {rentPrices[1]}", x,449, fontColour="Red")
        writeText(f"2 Houses: {rentPrices[2]}", x,479, fontColour="Red")
        writeText(f"3 Houses: {rentPrices[3]}", x,509, fontColour="Red")
        writeText(f"4 Houses: {rentPrices[4]}", x,539, fontColour="Red")
        writeText(f"1 Hotel: {rentPrices[5]}", x,569, fontColour="Red")
        writeText(f"Cost Of Each House: {houseCost}", x,599, fontColour="Red")
        writeText(f"Mortgage Value: {mortgageValue}", x,629, fontColour="Red")

    elif len(rentPrices) == 2: # Utility
        writeText(f"1 Owned: {rentPrices[0]}x Dice Roll", x,419, fontColour="Red")
        writeText(f"2 Owned: {rentPrices[1]}x Dice Roll", x,449, fontColour="Red")
        writeText(f"Mortgage Value: {mortgageValue}", x,479, fontColour="Red")

    elif len(rentPrices) == 5: # Transport
        writeText(f"1 Owned: {rentPrices[0]}", x,419, fontColour="Red")
        writeText(f"2 Owned: {rentPrices[1]}", x,449, fontColour="Red")
        writeText(f"3 Owned: {rentPrices[2]}", x,479, fontColour="Red")
        writeText(f"4 Owned: {rentPrices[3]}", x,509, fontColour="Red")
        writeText(f"Mortgage Value: {mortgageValue}", x,539, fontColour="Red")


    pygame.display.update()
  













def displayMainBoard(allHousesList, properties=[], colours=["Red", "Orange", "Blue", "Purple"], playerCoords={"Purple":[1336, 893], "Red":[1366, 893], "Orange":[1336, 923], "Blue":[1366, 923]}, buttons=[]):
    # Main Menu Button
    mainMenuButton = Button("Main Menu", (1780,0), (80,40), buttonType="MainMenu")
    buttons.append(mainMenuButton)


    # Background Colouring
    if True:
        # Make whole screen BG Colour
        surface = pygame.Surface((1920, 1010))
        surface.fill((0,0,200))  
        screen.blit(surface, (0,0))
    
        # Make Board Background White
        pygame.draw.rect(surface, (255,255,255), (471,20, 935,935))
        # Make Jail Background Orange
        pygame.draw.rect(surface, (255,145,0), (500,873, 56,55))



    # Display the grid
    # Vertical Line
    x,y = 471,20
    colourOfBorder = (0,0,0)
    colourOfInnerBorder = (0,0,0)

    # Main Grid (Outer and Inner, no boxes in between only four corners :( )
    if True:
        pygame.draw.rect(surface, colourOfBorder, (x + 85,y,3,935))
        pygame.draw.rect(surface, colourOfBorder, (x,y + 85,935,3))
        pygame.draw.rect(surface, colourOfBorder, (x,y,3,935))
        pygame.draw.rect(surface, colourOfBorder, (x,y,935,3))
        pygame.draw.rect(surface, colourOfBorder, (x + 850,y,3,935))
        pygame.draw.rect(surface, colourOfBorder, (x,y + 850,935,3))
        pygame.draw.rect(surface, colourOfBorder, (x+935,y,3,935))
        pygame.draw.rect(surface, colourOfBorder, (x,y+935,935,3))

    # Draw the inner grids (Only for the tiles, not seperating for colours yet )
    for i in range(10):
        pygame.draw.rect(surface, colourOfInnerBorder, (x + 85*(i+1),y,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (x,y + 85*(i+1),85,3))
        
        pygame.draw.rect(surface, colourOfInnerBorder, (x + 85*(i+1),y+850,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (x+850,y + 85*(i+1),85,3))


    # Draw the Coloured Boxes
    if True:
        #pygame.draw.rect(surface, (0,255,0), (x,y+935,935,3))

        # Colours for the Tiles
        brown = (150,77,0)  #1,3
        lightBlue = (0,170,254) # 6,8,9
        pink = (221,66,168) # 12,14,15
        orange = (255,145,0) # 17,19,20
        red = (255,0,0) # 22,24,25
        yellow = (255,255,0) # 27,28,30
        green = (0,100,31) # 32,33,35
        darkBlue = (0,0,145) # 38,40


        # Draw the rectangles to identify which tile belongs to which colour
        # Top Left Corner = 471,20
        # 531,460

        # Brown
        pygame.draw.rect(surface, brown, (1239,873  ,82,25))   
        pygame.draw.rect(surface, brown, (1069,873  ,82,25))   

        # Light Blue
        pygame.draw.rect(surface, lightBlue, (559,873  ,82,25))   
        pygame.draw.rect(surface, lightBlue, (644,873  ,82,25))   
        pygame.draw.rect(surface, lightBlue, (814,873  ,82,25))   

        # Pink
        pygame.draw.rect(surface, pink, (531,788  ,25,82))   
        pygame.draw.rect(surface, pink, (531,703  ,25,82))   
        pygame.draw.rect(surface, pink, (531,533  ,25,82))   

        # Orange
        pygame.draw.rect(surface, orange, (531,363  ,25,82))   
        pygame.draw.rect(surface, orange, (531,193  ,25,82))   
        pygame.draw.rect(surface, orange, (531,108  ,25,82))   

        # Red
        pygame.draw.rect(surface, red, (559,80  ,82,25))   
        pygame.draw.rect(surface, red, (729,80  ,82,25))   
        pygame.draw.rect(surface, red, (814,80  ,82,25))   

        # Yellow
        pygame.draw.rect(surface, yellow, (984,80  ,82,25))   
        pygame.draw.rect(surface, yellow, (1069,80  ,82,25))   
        pygame.draw.rect(surface, yellow, (1239,80  ,82,25))   

        # Green
        pygame.draw.rect(surface, green, (1324,108  ,25,82))   
        pygame.draw.rect(surface, green, (1324,193  ,25,82))   
        pygame.draw.rect(surface, green, (1324,363  ,25,82))   
    
        # Dark Blue
        pygame.draw.rect(surface, darkBlue, (1324,618  ,25,82))   
        pygame.draw.rect(surface, darkBlue, (1324,788  ,25,82))   


        # Add seperators on the coloured blocks

        # Brown
        pygame.draw.rect(surface, colourOfInnerBorder, (1239,898,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (1069,898,85,3))

        # Light Blue
        pygame.draw.rect(surface, colourOfInnerBorder, (559,898,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (644,898,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (814,898,85,3))

        # Pink
        pygame.draw.rect(surface, colourOfInnerBorder, (531,788,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (531,703,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (531,533,3,85))

        # Orange
        pygame.draw.rect(surface, colourOfInnerBorder, (531,363,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (531,193,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (531,108,3,85))

        # Red
        pygame.draw.rect(surface, colourOfInnerBorder, (559,80,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (729,80,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (814,80,85,3))

        # Yellow
        pygame.draw.rect(surface, colourOfInnerBorder, (984,80,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (1069,80,85,3))
        pygame.draw.rect(surface, colourOfInnerBorder, (1239,80,85,3))

        # Green
        pygame.draw.rect(surface, colourOfInnerBorder, (1349,108,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (1349,193,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (1349,363,3,85))

        # Dark Blue
        pygame.draw.rect(surface, colourOfInnerBorder, (1349,618,3,85))
        pygame.draw.rect(surface, colourOfInnerBorder, (1349,788,3,85))

        # Jail
        pygame.draw.rect(surface, colourOfInnerBorder, (500,873,3,55))
        pygame.draw.rect(surface, colourOfInnerBorder, (500,927,56,3))
    screen.blit(surface,(0,0))
    infoButtons, mortgageButtons = [], []

    # Display Player Owned Properties
    if True:
        # Top                               10,10,width,3
        pygame.draw.rect(surface, (0,0,0), (10,10,400,3))

        originalDepth=50
        width=400
        seperator=30
        x=0
        counter = 0
        tempList = []
        for tile in properties:
            owner = tile[2]
            if owner == "Purple": # If User Owns This Tile
                tempList.append(tile)
                finalDepth = 10 + originalDepth + seperator*x
                pygame.draw.rect(surface, (101,73,73), (10, finalDepth, width, 3))
                count = str(counter)
                if len(count) < 2:
                    count = "0"+count
                infoButtons.append(Button("?", (360, finalDepth), (80,30), buttonType=f"Info{count}"))
                mortgageButtons.append(Button("Mortgage", (260, finalDepth+5), (80,30), buttonType=f"Mortgage{count}", fontSize=17))
                mortgageButtons.append(Button("Unmortgage", (150, finalDepth+5), (80,30), buttonType=f"Unmortgage{count}", fontSize=17))
                x+=1 
            counter += 1

        finalDepth = 10 + originalDepth + seperator*x

        # Left
        pygame.draw.rect(surface, (100,0,0), (10, 10, 3, finalDepth-10))
        # RIght
        pygame.draw.rect(surface, (100,0,0), (10+width-3, 10, 3, finalDepth-10))
        # Bottom
        pygame.draw.rect(surface, (0,0,250), (10, finalDepth, width, 3))
        screen.blit(surface,(0,0))
        x=0

        # Mortgage Button
        # Tile Info Button

    # Display Non Player Owned Properties

    if True:
        # Top                               1510,110,width,3
        pygame.draw.rect(surface, (0,0,0), (1510,110,400,3))
        listOfProperties = ["Brown", "Light Blue", "Pink", "Orange", "Red", "Yellow", "Green", "Dark Blue", "transport", "Utility"]
        originalDepth2=140
        width=400
        seperator=30
        x2=0
        counter = 0
        tempList2 = []
        for tile in properties:
            owner = tile[2]
            if owner != "Purple" and tile[0] in listOfProperties:
                tempList2.append(tile)
                finalDepth = 10 + originalDepth2 + seperator*x2
                pygame.draw.rect(surface, (101,73,73), (1510, finalDepth, width, 3))
                count = str(counter)
                if len(count) < 2:
                    count = "0"+count
                infoButtons.append(Button("?", (1830, finalDepth), (80,30), buttonType=f"Info{count}"))
                x2+=1
            counter += 1
        finalDepth = 10 + originalDepth2 + seperator*x2

        # Left
        pygame.draw.rect(surface, (100,0,0), (1510, 110, 3, finalDepth-110))
        # Right
        pygame.draw.rect(surface, (100,0,0), (1510+width-3, 110, 3, finalDepth-110))
        # Bottom
        pygame.draw.rect(surface, (0,0,250), (1510, finalDepth, width, 3))

        # Mortgage Button
        # Tile Info Button
        x2=0
        for tile in tempList2:
            # Draw The Coloured Box For The Owner
            playersColour = (0,0,0)
            if tile[2] != "Bank":
                if tile[2] == "Blue":
                    playersColour = (0,0,255)
                elif tile[2] == "Red":
                    playersColour = (255,0,0)
                elif tile[3] == "Orange":
                    playersColour = (255,145,0)
                pygame.draw.rect(surface, playersColour, (1715, 17+originalDepth2+seperator*x2, 15, 15))
            x2 += 1
        screen.blit(surface,(0,0))
        x2=0
        writeText("Your Properties:", 35, 21, fontSize=42)
        writeText("Banks Properties:", 1515, 118, fontSize=42)

        for tile in tempList2:
            writeText(str(tile[0]), 1515, 17+originalDepth2+seperator*x2)
            x2 += 1
        for tile in tempList:
            writeText(str(tile[0]), 15, 17+originalDepth+seperator*x)
            x += 1

    # add Trading Button
    tradeButton = Button("Trade", (1700,0), (80,40), buttonType="Trade")
    buttons.append(tradeButton)



    pygame.display.update()


    playersCoords = displayAllPlayers(colours, playerCoords)

    # Bottom Row: Y=900
    # Top Row: Y=50 
    # Left Row: X=475
    # Right Row: X=1330
    # Draw text for tiles eg Chance, Tax, etc
    if True:
        # Have to write the text at the end :c
        writeText("Chance", 730,900, fontColour="Orange")
        writeText("Chance", 648,50, fontColour="Orange")
        writeText("Chance", 1328,560, fontColour="Orange")

        writeText("Community", 1154,900, fontColour="Cyan", fontSize=21)
        writeText("Chest", 1174,924, fontColour="Cyan", fontSize=22)
        writeText("Community", 474,290, fontColour="Cyan", fontSize=21)
        writeText("Chest",  474,314, fontColour="Cyan", fontSize=22)
        writeText("Community", 1324,290, fontColour="Cyan", fontSize=21)
        writeText("Chest", 1326,314, fontColour="Cyan", fontSize=22)

        writeText("Travel 1", 903,900, fontColour="Black")
        writeText("Travel 2", 477,480, fontColour="Black")
        writeText("Travel 3", 903,50, fontColour="Black")
        writeText("Travel 4", 1326,480, fontColour="Black")

        writeText("  Free", 478,45, fontColour="Purple")
        writeText("Parking", 478,67, fontColour="Purple")
    
        writeText("Tax 100", 1328,735, fontColour="Black")
        writeText("Tax 200", 988,900, fontColour="Black")

        writeText("Electric", 478,640, fontColour="Grey",fontSize=26)
        writeText("Company", 478,660, fontColour="Grey",fontSize=26)
        writeText("Water", 1162,50, fontColour="Grey")
        writeText("Works", 1160,70, fontColour="Grey")

        writeText("Go To", 1329,50, fontColour="Blue")
        writeText("Jail", 1337,70, fontColour="Blue")

    # Show all houses and hotels
    showHouse(allHousesList)

    for b in buttons:
        b.show()



    return buttons, playersCoords,  infoButtons, mortgageButtons

def updatePropertiesList(properties):
    # Display Player Owned Properties
    infoButtons = []
    mortgageButtons = []
    surfaceLeft = pygame.Surface((460, 1010))
    surfaceLeft.fill((0,0,200))  
    screen.blit(surfaceLeft, (0,0))
    surfaceRight = pygame.Surface((460, 910))
    surfaceRight.fill((0,0,200))  
    screen.blit(surfaceRight, (1460,100))

    
    if True:
        # Top                               10,10,width,3
        pygame.draw.rect(surfaceLeft, (0,0,0), (10,10,400,3))

        originalDepth=50
        width=400
        seperator=30
        x=0
        counter = 0
        tempList = []
        for tile in properties:
            owner = tile[2]
            if owner == "Purple": # If User Owns This Tile
                tempList.append(tile)
                finalDepth = 10 + originalDepth + seperator*x
                pygame.draw.rect(surfaceLeft, (101,73,73), (10, finalDepth, width, 3))
                count = str(counter)
                if len(count) < 2:
                    count = "0"+count
                infoButtons.append(Button("?", (360, finalDepth), (80,30), buttonType=f"Info{count}"))
                mortgageButtons.append(Button("Mortgage", (260, finalDepth+5), (80,30), buttonType=f"Mortgage{count}", fontSize=17))
                mortgageButtons.append(Button("Unmortgage", (150, finalDepth+5), (80,30), buttonType=f"Unmortgage{count}", fontSize=17))
                x+=1 
            counter += 1

        finalDepth = 10 + originalDepth + seperator*x

        # Left
        pygame.draw.rect(surfaceLeft, (100,0,0), (10, 10, 3, finalDepth-10))
        # RIght
        pygame.draw.rect(surfaceLeft, (100,0,0), (10+width-3, 10, 3, finalDepth-10))
        # Bottom
        pygame.draw.rect(surfaceLeft, (0,0,250), (10, finalDepth, width, 3))
        screen.blit(surfaceLeft,(0,0))
        x=0

        # Mortgage Button
        # Tile Info Button

    # Display Non Player Owned Properties

    if True:
        # Top                               1510,110,width,3
        pygame.draw.rect(surfaceRight, (0,0,0), (0, 0,400,3))
        listOfProperties = ["Brown", "Light Blue", "Pink", "Orange", "Red", "Yellow", "Green", "Dark Blue", "transport", "Utility"]
        originalDepth2=30
        width=400
        seperator=30
        x2=0
        counter = 0
        tempList2 = []
        for tile in properties:
            owner = tile[2]
            if owner != "Purple" and tile[0] in listOfProperties:
                tempList2.append(tile)
                finalDepth = 10 + originalDepth2 + seperator*x2
                pygame.draw.rect(surfaceRight, (101,73,73), (0, finalDepth, width, 3))
                count = str(counter)
                if len(count) < 2:
                    count = "0"+count
                infoButtons.append(Button("?", (320, finalDepth), (80,30), buttonType=f"Info{count}"))
                x2+=1
            counter += 1
        finalDepth = 10 + originalDepth2 + seperator*x2

        # Left
        pygame.draw.rect(surfaceRight, (100,0,0), (0, 0, 3, finalDepth))
        # Right
        pygame.draw.rect(surfaceRight, (100,0,0), (0+width-3, 0, 3, finalDepth))
        # Bottom
        pygame.draw.rect(surfaceRight, (0,0,250), (0, finalDepth, width, 3))

        # Mortgage Button
        # Tile Info Button
        x2=0
        for tile in tempList2:
            # Draw The Coloured Box For The Owner
            playersColour = (0,0,0)
            if tile[2] != "Bank":
                if tile[2] == "Blue":
                    playersColour = (0,0,255)
                elif tile[2] == "Red":
                    playersColour = (255,0,0)
                elif tile[3] == "Orange":
                    playersColour = (255,145,0)
                pygame.draw.rect(surfaceRight, playersColour, (1715, 17+originalDepth2+seperator*x2, 15, 15))
            x2 += 1
        screen.blit(surfaceRight,(1510,110))
        x2=0
        writeText("Your Properties:", 35, 21, fontSize=42)
        writeText("Banks Properties:", 1515, 118, fontSize=42)

        for tile in tempList2:
            writeText(str(tile[0]), 1515, 17+originalDepth2+110+seperator*x2)
            x2 += 1
        for tile in tempList:
            writeText(str(tile[0]), 15, 17+originalDepth+seperator*x)
            x += 1

    pygame.display.update()

    return mortgageButtons, infoButtons

def showHouse(allHousesList):
    for house in allHousesList:
        x,y,w,h,colour = house[0],house[1],house[2],house[3],house[4]
        surface = pygame.Surface((w, h))
        surface.fill(colour)  
        pygame.draw.rect(surface, colour, (x, y,w,h))  
        screen.blit(surface, (x,y))

def displayHouses(tile, allHousesList, num=0):
    # Tile will be coordinates
    # type is house or hotel
    # if hotel, only one can show

    if num == 5:
        type = "Hotel"
    else:
        type = "House"

    # Tile Colours ;P
    brown = (150,77,0)  #1,3
    lightBlue = (0,170,254) # 6,8,9
    pink = (221,66,168) # 12,14,15
    orange = (255,145,0) # 17,19,20
    red = (255,0,0) # 22,24,25
    yellow = (255,255,0) # 27,28,30
    green = (0,100,31) # 32,33,35
    darkBlue = (0,0,145) # 38,40

    # Acceptable Tiles
    acceptableTiles = [1,3,6,8,9,11,12,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39]
    if tile in acceptableTiles:
        if tile < 10:
            y = 876
            if tile ==1:
                x=1245
                colour = brown
            elif tile ==3:
                x=1075
                colour = brown
            elif tile == 6:
                x=820
                colour = lightBlue
            elif tile == 8:
                x=650
                colour = lightBlue
            elif tile == 9:
                x=565
                colour = lightBlue
        elif tile < 20:
            x = 537
            if tile == 11:
                y=794
                colour = pink
            elif tile == 12:
                y=709
                colour = pink
            elif tile == 14:
                y=539
                colour = pink
            elif tile == 16:
                y=369
                colour = orange
            elif tile == 18:
                y=199
                colour = orange
            elif tile == 19:
                y=114
                colour = orange

        elif tile<30:
            y = 86
            if tile ==21:
                x=565
                colour = red
            elif tile ==23:
                x=735
                colour = red
            elif tile == 24:
                x=820
                colour = red
            elif tile == 26:
                x=990
                colour = yellow
            elif tile == 27:
                x=1075
                colour = yellow
            elif tile == 29:
                x=1245
                colour = yellow
        elif tile <= 40:
            x = 1330
            if tile == 31:
                y=111
                colour = green
            elif tile == 32:
                y=196
                colour = green
            elif tile == 34:
                y=366
                colour = green
            elif tile == 37:
                y=621
                colour = darkBlue
            elif tile == 39:
                y=791
                colour = darkBlue
        tileCoords = (x,y)


        # Alter base coordinates to fit nicely ;)
        coords = []
        if type == "Hotel":
            print("Too much work :(")
        
        else: # IF Houses
            for i in range(num): # For Each House
                xChange, yChange = i*18, i*18
                if tile < 10: # Increase X Value
                    coords.append( (tileCoords[0] + xChange, tileCoords[1]) )
                elif tile < 20: # Increase Y Value
                    coords.append( (tileCoords[0], tileCoords[1] + yChange) )
                elif tile < 30: # Decrease X Value
                    coords.append( (tileCoords[0] + xChange, tileCoords[1]) )
                else: # Decrease Y Value
                    coords.append( (tileCoords[0], tileCoords[1] + yChange) )


        if type == "Hotel": # I want it centred 🥺
            buildingColour = (220,20,60) # Cool pink kinda colour
            surface = pygame.Surface((15, 15))
            surface.fill(buildingColour)  

            if tile < 10 or (tile < 30 and tile > 20):
                
                pygame.draw.rect(surface, colour, (tileCoords[0] + 28, tileCoords[1]  ,82,25))   
                x,y = tileCoords[0] + 28, tileCoords[1]

            else:
                pygame.draw.rect(surface, colour, (tileCoords[0] + 28, tileCoords[1]  ,82,25))  
                x,y = tileCoords[0], tileCoords[1] + 28

            # Get rid of all houses on that tile
            tempList = []
            for building in allHousesList:
                # Checks x and y are not more than 80 from the corner :/
                x1,y1=building[0], building[1]

                if ((y1 == tileCoords[1] and x1>=tileCoords[0] and x1 < tileCoords[0]+82) or (x1 == tileCoords[0] and y1>=tileCoords[1] and y1 < tileCoords[1]+82)) == False:
                    tempList.append(building)

            allHousesList = tempList
            allHousesList.append( [x,y,15,15,buildingColour ] )
            screen.blit(surface, (x,y))

        else: # Is a house
            buildingColour = (102,51,153) # Purple :D
            surface = pygame.Surface((15, 15))
            surface.fill(buildingColour)  
            pygame.draw.rect(surface, colour, (tileCoords[0] + 28, tileCoords[1]  ,82,25))  
            

            for i in range(num):
                surface = pygame.Surface((15, 15))
                surface.fill(buildingColour)  
                screen.blit(surface, coords[i])
                x,y = coords[i][0], coords[i][1]
                allHousesList.append( [x,y,15,15, buildingColour ] )

    pygame.display.update() 
    return allHousesList


def convertTileNumToCoordinates(tile, player, inJail=False):
    # 0 = GO
    # 11 = JAIL     # Extra Work Needed :(
    # 21 = Free Parking
    # 31 = GO TO JAIL
    # 41 == 0

    # Player Numbers start at 1
    # Tile Numbers start at 0

    # X Change
    if player % 2 == 1: # If the player number is odd
        xBasedChange = 0
    else: # If the player number is even
        xBasedChange = 30

    # Y Change
    if player == 0 or player == 1: # If the player is first or second
        yBasedChange = 0
    else: # The player is third or fourth
        yBasedChange = 30


    if tile < 10: # Bottom Row
        baseY = 893 + yBasedChange
        baseX = 1336  + xBasedChange
        x = baseX - (tile*85)
        coordinate = (x, baseY)
    
    elif tile == 10: # Jail Tile (Complicated)
        if inJail: # If the player is in jail
            # They get put in Jail :(
            if player == 1:
                coordinate = (503,875)
            elif player == 2:
                coordinate = (530,875)
            elif player == 3:
                coordinate = (503,902)
            elif player == 4:
                coordinate = (530,902)
        else: # The player is just visiting Jail
            if player == 1:
                coordinate = (474,875)
            elif player == 2:
                coordinate = (474,902)
            elif player == 3:
                coordinate = (503,930)
            elif player == 4:
                coordinate = (530,930)           

    elif tile <= 20: # Left Column
        baseX = 476 + xBasedChange
        baseY = 893 + yBasedChange    #(At tile 11 aka Jail)
        y = baseY - (tile-10)*85
        coordinate = (baseX, y)
 
    elif tile <= 30: # Top Row
        baseX = 476 + xBasedChange
        baseY = 33 + yBasedChange
        x = baseX + (tile-20)*85
        coordinate = (x, baseY)

    else: # Right Column
        baseX = 1346 + xBasedChange
        baseY = 43 + yBasedChange
        y = baseY + (tile-30)*85
        coordinate = (baseX, y)

    return coordinate

def hidePlayer(tile, player, inJail=False):
    x,y = convertTileNumToCoordinates(tile, player, inJail)
    clearScreen(x,y,25,25,bgColour)

def displayTradingScreen():
    clearScreen(561,110, 755,755,(255,255,255))
    pygame.display.update()



def displayUsersMoney(money=200, y=30,name="Your"):

    writeText(f"{name} money: {money}", 1480,y, fontColour="Red")
    pygame.display.update()

def displayAllPlayers(colours, coordinates):
    playersCoords = {}
    for i in range(len(colours)):
        colour = colours[i]
        x,y = coordinates[colour][0], coordinates[colour][1]
        surface = pygame.Surface((25, 25))
        surface.fill(colour)  
        screen.blit(surface, (x,y))
        playersCoords[colour] = [x,y]
    pygame.display.update()
    return playersCoords

def movePlayer(colour, coordinates, playersCoords):
    # Display Players New Position
    x,y = coordinates[0], coordinates[1]
    surface = pygame.Surface((25, 25))
    surface.fill(colour)  
    screen.blit(surface, (x,y))

    # Remove Players Old Position
    playersCoords[colour] = coordinates


    pygame.display.update()
    return playersCoords

def clearScreen(x,y,w,h, colour):
    pygame.draw.rect(screen, colour, pygame.Rect(x,y,w,h))





def checkTile(tile, player, playersData, properties, reallyPlaying, playersName, allHousesList):
    
    
    # Checking if tile is pass go
    if tile == 0 and reallyPlaying == True:
        print(player, "just landed on GO!!")

    # Checking if tile is Free Parking
    elif tile == 20:
        # Player getting all the money from Free Parking
        playersData[player][1] += playersData[-1][1]
        # Free Parking losing all it's money
        playersData[-1][1] = 0

    # Checking if tile is Go To Jail
    elif tile == 30:
        # Sends the player to jail :(
        playersData = goToJailProtocol(playersData, player)

    # Checking if the tile is Community Chest
    elif tile == 2 or tile == 17 or tile == 33:
        file = open("CommunityChest.txt", "r")
        communityChestPack = file.readlines()
        file.close()
        sizeOfPack = len(communityChestPack) -1
        number = randomNumberGenerator(1, sizeOfPack)
        card = cardDrawer(communityChestPack, number)
        playersData = communityChestChanceProtocol(card, playersData, player, reallyPlaying)

    # Checking if the tile is Chance
    elif tile == 7 or tile == 22 or tile == 36:
        file = open("Chance.txt", "r")
        chancePack = file.readlines()
        file.close()
        sizeOfPack = len(chancePack) -1
        number = randomNumberGenerator(1, sizeOfPack)
        card = cardDrawer(chancePack, number)
        playersData = communityChestChanceProtocol(card, playersData, player, reallyPlaying)

    # Checking if the tile is Tax 200
    elif tile == 4:
        # Charge the player
        playersData[player][1] -= 200
        # Give the money to Free Parking
        playersData[-1][1] += 200

    # Checking if the tile is Tax 100
    elif tile == 38:
        # Charge the player
        playersData[player][1] -= 100
        # Give the money to Free Parking
        playersData[-1][1] += 100
    
    # Checking if tile is Jail
    elif tile == 10 and reallyPlaying == True:
        print(player, "just landed on jail!!")
        
    # Otherwise the tile is a property ;)
    
    else:
        print(f"Tile is owned by {properties[tile][2]} and player is {playersName}")
        # Check who the owner is
        owner = properties[tile][2]
        # If the bank owns the property and
        # the player can afford it
        if owner == "Bank" and playersData[player][1]>properties[tile][1]:
            price = properties[tile][1]
            # Tile Name
            t = properties[tile][0]
            # Gets the user's choice on if they want the property
            playersBalance = playersData[player][1]
            choice =  checkIfTheUserWantsTheProperty(price,t, reallyPlaying, playersBalance, playersName)
            if choice == "yes":
                # Buys the property if they do
                properties, playersData = purchasePropery(properties, playersData, player)

        elif owner == playersName or (owner=="Purple" and playersName == "User"):
            
            # Check if they own the full set of that colour
            ownFullSet = checkIfPlayerOwnsTheFullSet(properties, tile)
            if ownFullSet == True:
                # Check if the user wants to build
                properties, playersData, allHousesList = validateBuildingRequests(properties, player, playersData, allHousesList)
                clearScreen(1480,0,200,80,(0,0,200))
                # Show money for ALL players
                displayUsersMoney(playersData[1][1],name="Purple")

        # The property is owned by another player
        else:
            
            # Find the owners index
            ownersIndex = 0
            x=0
            for p in playersData:
                if p[0] == owner:
                    ownersIndex = x
                x += 1

            # Check if the owner is in jail
            if playersData[ownersIndex][4] == True and reallyPlaying == True:
                print("You're lucky! The owner is in jail so you don't owe anything. :)")
            
            # Check if the property is mortgaged
            elif properties[tile+1][7] == True and reallyPlaying == True:
                print("You're lucky! The property is mortgaged so you don't owe anything. :)")

            # If the owner isn't in jail and the property isn't mortgaged then the player has to pay
            else:
                rent = rentCalculator(properties, playersData, player)
                ownersIndex = 0
                x=0
                for p in playersData:
                    if p[0] == owner:
                        ownersIndex = x
                    x += 1
                print(f"Player charged: {player}")
                print(f"Owner = {owner}")
                print(f"Player paid: {ownersIndex}")
                playersData = chargeTenantsPayLandlords(player, ownersIndex, rent, playersData)

    return playersData, properties, allHousesList

def checkIfPlayerOwnsTheFullSet(properties, tile):
    colour = properties[tile][0]
    sameOwner = False

    # If the colour is Brown
    if colour == "Brown":
        if properties[2][2] == properties[4][2]:
            sameOwner = True

    # If the colour is Light Blue
    elif colour == "Light Blue":
        if properties[7][2] == properties[9][2] and properties[9][2] == properties[10][2]:
            sameOwner = True

    # If the colour is Pink
    elif colour == "Pink":
        if properties[12][2] == properties[14][2] and properties[14][2] == properties[15][2]:
            sameOwner = True

    # If the colour is Orange
    elif colour == "Orange":
        if properties[17][2] == properties[19][2] and properties[19][2] == properties[20][2]:
            sameOwner = True

    # If the colour is Red
    elif colour == "Red":
        if properties[22][2] == properties[24][2] and properties[24][2] == properties[25][2]:
            sameOwner = True

    # If the colour is Yellow
    elif colour == "Yellow":
        if properties[27][2] == properties[19][2] and properties[29][2] == properties[30][2]:
            sameOwner = True

    # If the colour is Green
    elif colour == "Green":
        if properties[32][2] == properties[33][2] and properties[33][2] == properties[35][2]:
            sameOwner = True

    # If the colour is Dark Blue
    elif colour == "Dark Blue":
        if properties[38][2] == properties[40][2]:
            sameOwner = True

    return sameOwner

def buyOrNot(tile, price, playersBalance):
    buttons = []
    buyButton = Button("Buy", (840,500), (80,40), buttonType="Buy", textColour=(200,0,0))
    buttons.append(buyButton)
    leaveButton = Button("Leave", (930,500), (80,40), buttonType="Leave", textColour=(200,0,0))
    buttons.append(leaveButton)
    decided = False


    displayMessageToUser(f"For tile {tile} it would cost M${price}. You have M${playersBalance}")
    # Draw coloured boxes 🥺
    # Red Box
    surface = pygame.Surface((80,40))
    surface.fill(((255,0,0)))
    screen.blit(surface, (840, 500))
    # Green Box
    surface = pygame.Surface((80,40))
    surface.fill(((0,255,0)))
    screen.blit(surface, (930, 500))
    pygame.display.update()
    for b in buttons:
        b.show()

    while not decided:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                for b in buttons:
                    wants = b.click(event)
                    
                    if wants == "Buy":
                        buy = True
                        decided = True
                    elif wants == "Leave":
                        buy = False
                        decided = True
    
    return buy


def checkIfTheUserWantsTheProperty(price, tile, reallyPlaying, playersBalance, playersName):
    print(playersName)
    playersName = playersName.lower()
    # Creates a loop to check if the user's input is valid
    validResponse = False
    if reallyPlaying:
        while validResponse == False:

            if playersName == "user":
                # Receives the user's input
                
                response = buyOrNot(tile, price, playersBalance)
                if response:
                    response = "yes"
                else:
                    response = "no"

            elif playersName == "tom":
                # Tom Always Buys
                response = "yes"
            elif playersName == "jeff":
                response = "yes"
            elif playersName == "tim":
                response = "yes"
            elif playersName == "richard":
                response = "yes"
            elif playersName == "jeremy":
                response = "yes"
            else:
                print(f"User = {playersName}")



            clearScreen(561,110, 755,755,(255,255,255))




            #offer, bankBalance, player="user"


            # Checks validity of choice
            if response == "yes" or response == "no":
                # Breaks the loop
                validResponse = True
    else:
        # If the player isn't playing
        response = "no"


    return response

def randomNumberGenerator(smallest, highest):
    from random import randint
    # Generates a random number from x to y
    num = randint(smallest, highest)
    
    return num

def diceRoller():
    from random import randint
    # Generates a random number from 1 to 6
    num = randint(1, 6)
    
    return num

def cardDrawer(cardPack, randomNumber):
    # Selects a random card and returns it
    card = cardPack[randomNumber-1]

    # The card will need to be formatted
    # The line will be in the form Message, Instruction
    # so the instruction and message will be seperated by the semi colon

    # This creates a list
    card = card.split(";")

    # The message is the first element in the list
    message = card[0]
    # The instruction is the second element in the list
    instruction = card[1]

    # The message and instruction need to be cleaned
    message = message.replace('"', '')
    message = message.replace('[', '')
    message = message.replace(']', '')
    message = message.replace('\n', '')
    message = message.replace(',', '')

    instruction = instruction.replace('"', '')
    instruction = instruction.replace('[', '')
    instruction = instruction.replace(']', '')
    instruction = instruction.replace('\n', '')
    instruction = instruction.replace(',', '')
    
    # The card is a list of the message and the instruction
    card = [message, instruction]

    return card

def chargeTenantsPayLandlords(tenant, landlord, sumOfMoney, playersList):
    # Reduce the tenant's bank balance by the sumOfMoney
    playersList[tenant][1] -= sumOfMoney
    # Increase the landlord's bank balance by the sumOfMoney
    playersList[landlord][1] += sumOfMoney

    return playersList

def rentCalculator(properties, players, tenant):
    # Find the tile
    tile = players[tenant][2]

    # Check if the owner is in prison O_O
    owner = properties[tile][2]
    ownersIndex = 0
    x=0
    for p in players:
        if p[0] == owner:
            ownersIndex = x
        x += 1
    prisonStatus = players[ownersIndex][4]

    #Check if the property is mortgaged
    mortgageStatus = properties[tile][7]

    # If the owner is not in jail and the property is not mortgaged
    if prisonStatus == False and mortgageStatus == False:
        # If the tile is a station 
        if tile == 6 or tile == 16 or tile == 26 or tile == 36:
            # The owner of the property is the landlord
            landlord = properties[tile][2]
            # Counts the number of stations the landlord owns
            numOwnedByLandlord = 0
            if properties[6][2] == landlord:
                numOwnedByLandlord += 1
            if properties[16][2] == landlord:
                numOwnedByLandlord += 1
            if properties[26][2] == landlord:
                numOwnedByLandlord += 1
            if properties[36][2] == landlord:
                numOwnedByLandlord += 1
            # The rent is altered depending on the number of stations owned by the player
            rent = properties[tile][4][numOwnedByLandlord -1]
        
        # If the tile is a utility
        elif tile == 13 or tile == 29:
            # The owner of the property is the landlord
            landlord = properties[tile][2]
            # Counts the number of utilities the landlord owns
            numOwnedByLandlord = 0
            if properties[13][2] == landlord:
                numOwnedByLandlord += 1
            if properties[29][2] == landlord:
                numOwnedByLandlord += 1

            # If the landlord owns 1 utility then the rent is 4 times that on the dice       
            if numOwnedByLandlord == 1:
                diceRoll = diceRoller()
                rent = diceRoll * 4
            # If the landlord owns both utilities then the rent is 10 that on the dice
            else:
                diceRoll = diceRoller()
                rent = diceRoll * 10           

        # Otherwise the tile is a normal property
        else:
            # Find the number of houses
            numberOfHouses = properties[tile][3]
            # Find the rent
            rent = properties[tile][4][numberOfHouses]
    else:
        rent=0
    return rent
    
def purchasePropery(properties, playersData, tenant):
    # Find the tile
    tile = playersData[tenant][2]
    # Find the cost of the property
    cost = properties[tile][1]
    # Charge the player the cost of the property
    playersData[tenant][1] -= cost
    # Pay the cost of the property to the bank
    playersData[0][1] += cost

    # Change the owner to the player
    properties[tile][2] = playersData[tenant][0]
    print(f"Tile = {tile}")
    print(f"tenant={tenant}")

    return properties, playersData

def movePlayerTo(playersData, player, newPosition):
    # Sets the player a new position
    playersData[player][2] = newPosition

    return playersData

def getUsersInput(acceptableOutputs, want=""):
    found = False

    # If want="X" or want="Y", the acceptable outputs are parameters


    input_box = InputBox(900, 500, 140, 32, bgColour)
    input_boxes = [input_box]
    while not found:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            for box in input_boxes:
                if found == False:
                    t = box.handle_event(event)
                    if t != None:

                        if want != "X" and want != "Y":
                            if str(t) in acceptableOutputs:
                                acceptedOutput = t
                                # Delete the button so it's not there anymore :D
                                input_boxes.clear()
                                found = True
                                break
                        elif want == "X" or want == "Y":

                            if isinstance(t,int) and t >= acceptableOutputs[0] and t <= acceptableOutputs[1]:
                                acceptedOutput = t
                                # Delete the button so it's not there anymore :D
                                input_boxes.clear()
                                found = True     
                                break                       
                    


        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
        

    return acceptedOutput

def validateBuildingRequests(properties, player, playersData, allHousesList):
    # Creates a loop to validate building request
    built = False
    while built == False:
        # The number of houses the user wants
        writeText("How many houses would you like?", 700,400,fontColour="Red")
        #numberOfHousesDesired = int(input("How many houses would you like?"))
        #                                           house player can afford,                                        house bank owns,    houses remaining to build
        numberOfHousesDesired = getUsersInput([0,min(playersData[player][1]//properties[playersData[player][2]][5], playersData[0][3][0], 5-properties[playersData[player][2]][3])],"X")
        

        # The tile the player is on
        tile = playersData[player][2]
        # The number of houses on that tile already
        numberOfHousesOwned = properties[tile][3]
        # The amount of money the player has
        balance =  playersData[player][1]
        # The cost of each house for that tile
        costOfHouses = properties[tile][5]

        # Houses owned by the bank
        housesOwnedByBank = playersData[0][3][0]
        # Hotels owned by the bank
        hotelsOwnedByBank = playersData[0][3][1]
        print(f"balance = {balance}")
        # If the user can afford the houses and they're allowed to build them, then this proceeds,
        # otherwise, the loop continues until the user inputs a valid number of houses
        # Also checks if there are enough hotels/houses left for the request
        
        if (numberOfHousesOwned + numberOfHousesDesired) < 5 and balance - (costOfHouses*numberOfHousesDesired) > 0 and numberOfHousesDesired <= housesOwnedByBank:
            # Changes the number of houses on the tile
            properties[tile][3] += numberOfHousesDesired
            # The number of houses owned is increase
            playersData[player][3][0] += numberOfHousesDesired
            # Changes the player's balance to account for the cost of the buildings
            playersData[player][1] -= costOfHouses*numberOfHousesDesired
            # Gives the bank the money from the user
            playersData[0][1] += costOfHouses*numberOfHousesDesired
            built = True
        # Changes the number of houses and hotels owned by the player
        elif (numberOfHousesOwned + numberOfHousesDesired) == 5 and balance - (costOfHouses*numberOfHousesDesired) > 0 and numberOfHousesDesired <= hotelsOwnedByBank:
            # The number of houses owned is decreased
            playersData[player][3][0] -= numberOfHousesOwned
            # The number of hotels is increased
            playersData[player][3][1] += 1
            # Takes away a hotel from the Bank
            playersData[0][3][1] -= 1
            # Adds Houses to the Bank
            playersData[0][3][0] += numberOfHousesOwned
            # Changes the number of houses on the tile
            properties[tile][3] = 5
            # Changes the player's balance to account for the cost of the buildings
            playersData[player][1] -= costOfHouses*numberOfHousesDesired
            # Gives the bank the money from the user
            playersData[0][1] += costOfHouses*numberOfHousesDesired
             




            # Terminates the loop
            built = True
    allHousesList = displayHouses(tile, allHousesList, properties[tile][3])
    # Hide message after
    clearScreen(561,110, 755,755,(255,255,255))
    return properties, playersData, allHousesList

def buildingRepairsProtocol(playersData, player, amountForHotels, amountForHouses, numOfHouses, numOfHotels):
    # Variable for runnning total
    total = 0
    # Increase the total for the cost of the houses
    total += int(numOfHouses) * int(amountForHouses)
    # Increase the total for the cost of the hotels
    total += int(numOfHotels) * int(amountForHotels)

    # Charge the player
    playersData[player][1] -= total
    # Give the money to Free Parking
    playersData[-1][1] += total

    return playersData

def goToJailProtocol(playersData, player):
    # Set player position to jail
    playersData[player][2] = 11
    # Set player status to prisoner
    playersData[player][4] == True

    return playersData

def payEachPlayerProtocol(playersData, amount, player):
    # Finds the bank balance of the player
    playersBank = playersData[player][1]
    # For each player in the array
    for i in range(len(playersData)):

        # If the player i is not the bank or Free Parking
        if i != 0 and i != len(playersData)-1:
            # The player is charged
            playersData[player][1] -= amount
            # The others are paid
            playersData[i][1] += amount

    return playersData

def movePlayerBy(playersData, numberOfTilesToMove, player):
    # Finds the tile the user is on
    currentTile = playersData[player][2]

    # If the move will place them in an invalid tile, then they "pass go"
    if currentTile + numberOfTilesToMove > 40:
        # The player's position is corrected
        currentTile =  currentTile + numberOfTilesToMove - 40
        # Increases the players balance for passing "go"
        playersData[player][1] += 200
        # The bank is charged
        playersData[0][1] -= 200
    
    # If the player lands on "go"
    elif currentTile + numberOfTilesToMove == 41:
        # The player is moved to the first tile (go)
        currentTile = 1
        # The player is paid for landing on "go"
        playersData[player][1] += 400
        # The bank is charged
        playersData[player][1] -= 400

    # If the player doesn't pass go, they move on
    else:
        currentTile += numberOfTilesToMove

    # Sets the players new position
    playersData[player][2] = currentTile

    return playersData

def displayMessageToUser(message):
    clearScreen(700,400,600,400,(255,255,255))
    writeText(message,800,400,fontColour="Red")

def communityChestChanceProtocol(card, playersData, player, reallyPlaying):
    # The players position
    tile = playersData[player][2]

    # Card value is entered in the form:
    # ["Message For The User To Read", InstructionToProcess]
    # E.g card = ["You've been caught by the IRS! Pay building repairs!", "Pay"]

    # Seperate the message and the instruction
    message = card[0]
    instruction = card[1]

    # Display the message for the user to read
    if reallyPlaying:

        showTextBox(message)

    # Change the instruction to lowecase to reduce issues
    instruction = instruction.lower()

    # If the card tells the player to move to a specific position
    if "move to" in instruction or "go to" in instruction:

        # If the user is told to go to jail
        if "jail" in instruction:
            playersData = goToJailProtocol(playersData, player)

        # If the user is told to got to the nearest travel square
        elif "nearest travel square" in instruction:
            if tile < 6:
                playersData = movePlayerTo(playersData, player, 6)
            elif tile < 16:
                playersData = movePlayerTo(playersData, player, 16)
            elif tile < 26:
                playersData = movePlayerTo(playersData, player, 26)
            elif tile < 36:
                playersData = movePlayerTo(playersData, player, 36)
            else:
                playersData = movePlayerTo(playersData, player, 6)
                # The player gets paid for passing go
                playersData[player][1] += 200
                # The bank gets charged for passing go
                playersData[0][1] -= 200

        elif "nearest utility" in instruction:
            if tile < 13:
                playersData = movePlayerTo(playersData, player, 13)
            elif tile < 29:
                playersData = movePlayerTo(playersData, player, 29)
            else:
                playersData = movePlayerTo(playersData, player, 13)
                # The player gets paid for passing go
                playersData[player][1] += 200
                # The bank gets charged for passing go
                playersData[0][1] -= 200
        
        elif "back 3 spaces" in instruction:
            # The player is moved back 3 spaces
            playersData = movePlayerTo(playersData, player, tile-3)

        elif "go" in instruction:
            newTile = 0
            playersData = movePlayerTo(playersData, player, newTile)

        else:
            # The last 2 digits are the tile numbers
            newTile = int(instruction[-2:])
            playersData = movePlayerTo(playersData, player, newTile)

            # If the player lands on go
            if newTile == 1:
                 # The player gets paid for passing go
                playersData[player][1] += 400
                # The bank gets charged for passing go
                playersData[0][1] -= 400               

            # If the player passes go
            elif newTile < tile:
                # The player gets paid for passing go
                playersData[player][1] += 200
                # The bank gets charged for passing go
                playersData[0][1] -= 200
                    
    elif "pay:" in instruction:
        amount = int(instruction[-3:])
        # The player pays the amount to free parking
        playersData[player][1] -= amount
        # Free Parking receives the money
        playersData[-1][1] += amount
    
    elif "building repairs" in instruction:
        # The last 3 digits of the card are the cost of repairs for hotels
        amountForHotels = instruction[-3:]
        # The last 7 to last 4 digits of the card the cost of repairs for houses
        amountForHouses = instruction[-7:-4]
        # The number of houses
        numOfHouses = playersData[player][3][0]
        # The number of hotels
        numOfHotels = playersData[player][3][1]

        playersData = buildingRepairsProtocol(playersData, player, amountForHotels, amountForHouses, numOfHouses, numOfHotels)

    elif "pay to each player" in instruction:
        # The amount is the last 3 digits on the card
        amount = int(instruction[-3:])
        # A function is called to pay each player
        playersData = payEachPlayerProtocol(playersData, amount, player)

    elif "collect" in instruction:
        # The amount is the last 3 digits on the card
        amount = int(instruction[-3:])
        # Paying the player
        playersData[player][1] += amount
        # Charging the bank       
        playersData[0][1] -= amount

    elif "each player pay you" in instruction:
        # The amount you get from each player is the last 3 digits on the card
        amount = int(instruction[-3:])

        for playerX in playersData:
            if reallyPlaying == True:
                print(f"Player = {playersData[player]}")
                print(f"playerX = {playerX}")
            if playerX[0] != "Bank" and playerX[0] != "Free Parking":
                amount = int(amount)
                # Charge each player
                playerX[1] -= amount
                # Give the money to the player who won :)
                playersData[player][1] += amount


    return playersData

def setNumberOfPlayers(reallyPlaying, legalPlayers):
    # Loop to find the number of players wanted
    numberOfPlayersDecided = 0
    while numberOfPlayersDecided == 0:
        # Check if the input is a number
        if reallyPlaying == True:
            try:
                writeText("How many players?", 700,370, fontColour="Red", fontSize=70)
                #number = int(getUsersInput([1,6], want="X"))
                number = 4
                # Check if the number entered is within the allowed limit
                if number <= 6 and number > 0:
                    # Ends the loop
                    numberOfPlayersDecided = number

            except:
                # Alerts the user that the input was invalid
                print("Sorry, that didn't work. Please try again.")
        else:
            numberOfPlayersDecided = 4
    print("Done",numberOfPlayersDecided)
    whichPlayers = ["User"]
    # -1 cos the players is already one ;p
    numberOfPlayersDecided -=1

    for i in range(numberOfPlayersDecided):
            # Clear Screen]
        clearScreen(0,0,1920,1010,COLOUR_ACTIVE)
        # Ask for which players
        writeText("Which players?", 500,400,fontSize=50)
        writeText(f"Current players: {whichPlayers}",500,800)
        nameInvalid = True
        while nameInvalid:
            
            #name = getUsersInput(["jeff", "tom", "tim", "richard", "jeremy"],want="")
            name = "tom"
            if name in legalPlayers:
                nameInvalid = False

        whichPlayers.append(name)

    

    return numberOfPlayersDecided, whichPlayers


def addPlayers(numberOfPlayersDesired, basePlateForNewPlayers, playersNames, reallyPlaying):
    # Sets the list for the data about the bank
    bank = ['Bank', 20450, 0, [34, 13], False, True]
    # Saves the list for the data about Free Parking
    freeParking = ['Free Parking', 0, 21, [0,0], False, True]

    # A temporary list to store the new players data
    tempList = [bank]

    # For each player that's wanted to be added
    for player in range(numberOfPlayersDesired):
        # Variable for the players name
        playerName = playersNames[player+1]
        if reallyPlaying == True:
            print("New player:",playerName)
        # The baseplate is altered to the players name
        # The new player is defined by the baseplate
        newPlayer = [playerName] + basePlateForNewPlayers
        # The new player is added to the list of players
        tempList.append(newPlayer)

        # As a new player has been added, the bank must be charge $1500 for the
        # new player's bank account value.
        # Bank's Bank Account is deducted $1500
        tempList[0][1] -= 1500
       # print(tempList)
    # Add Free Parking on the end
    tempList.append(freeParking)

    return tempList

def checkForBankruptcy(playersData):
    # Start by assuming noone is bankrupt
    bankrupt = False
    # Take note of who is bankrupt
    bankruptPlayer = ""

    # Check each player
    for player in playersData:
        # If the player has a balance of 0 or it's negative, then they are bankrupt
        if player[1] <= 0 and player[0] != "Free Parking":
            # The player's status of bankruptcy is anounced
           bankrupt = True 
           bankruptPlayer = player[0]
    
    return bankrupt,bankruptPlayer

def bankruptPlayerProtocol(playersData, propertiesData, player):
    # Start of by mortgaging EVERYTHING!!!
    for property in propertiesData:

        # If the owner of this property is bankrupt and the property is not mortgaged
        if property[2] == player and property[7] == False:
            # Property is mortgaged
            property[7] = True
            mortgageValue = property[6]
            # The player is given the money from mortgaging
            playersData[player][1] += mortgageValue

    # After all their properties are mortgaged, if they are still bankrupt, they are removed and their assets are returned to the bank.
    if playersData[player][1] <= 0:
        # Checks which properties are owned by the player
        for property in propertiesData:
            # If the owner of the property is the bankrupt player
            if property[2] == player:
                # The property is unmortgaged
                property[7] = False
                # The property is transferred to the bank
                property[2] = "Bank"
            # All the assets of the bankrupt player have now been transferred
            # The players status is changed to Out Of Game
            playersData[player][6] = False
    return playersData, propertiesData

def doTrade(properties, playersData, playersInvolvedInTrade, listOfPlayersNames):
    clearScreen(561,110, 755,755,(255,255,255))
    pygame.display.update()

    buttons = []
    #accept button
    #decline button
    acceptButton = Button("Accept", (920,450), (80,40), buttonType="Accept", textColour=(200,0,0))
    buttons.append(acceptButton)
    declineButton = Button("Decline", (920,500), (80,40), buttonType="Decline", textColour=(200,0,0))
    buttons.append(declineButton)

    # Add backgrounds for the buttons
    surface = pygame.Surface((80,40))
    surface.fill((255,0,0))
    screen.blit(surface, (920,450))
    surface = pygame.Surface((80,40))
    surface.fill((0,255,0))
    screen.blit(surface, (920,500))
    

    print(f"User: {playersInvolvedInTrade[0]}")
    print(f"Player: {playersInvolvedInTrade[1]}")
    computerChosen, userChosen, bothAccept  = False, False, False
    trade = [ [0], [0] ]

    playersIndexes = [listOfPlayersNames.index(playersInvolvedInTrade[0]), listOfPlayersNames.index(playersInvolvedInTrade[1])]
    # User owned properties and computer owned properties
    playerOwnedProperties, computerOwnedProperties = [], []
    for i in range(len(properties)):
        # owner is properties[i][2]
        if properties[i][2] == playersInvolvedInTrade[0]:
            playerOwnedProperties.append(properties[i]+[i])

        elif properties[i][2] == playersInvolvedInTrade[1]:
            computerOwnedProperties.append(properties[i]+[i])

    # Boards coordinates = 561,110, 755,755
    # Display user's options

    for i in range(len(playerOwnedProperties)):
        p = playerOwnedProperties[i]
        name = p[0]
        surface = pygame.Surface((80,40))
        surface.fill(((255,0,0)))
        screen.blit(surface, (700, 200+i*50))
        writeText(name, 600, 200+i*50, fontColour="Red")
        addOrRemoveButton = Button("AoR", (700,200+i*50), (70,20), "AddOrRemove1", textColour=(255,255,255), tileName=name,tileNum=p[8])
        buttons.append(addOrRemoveButton)

    writeText(f"Cash: {trade[0][0]}", 700, 200, fontColour="Red")
    writeText(f"Cash: {trade[1][0]}", 1000, 200, fontColour="Red")
    for i in range(len(computerOwnedProperties)):
        p = computerOwnedProperties[i]
        name = p[0]
        surface = pygame.Surface((80,40))
        surface.fill(((255,0,0)))
        screen.blit(surface, (1100, 200+i*50))
        writeText(name, 1000, 200+i*50, fontColour="Red")
        addOrRemoveButton = Button("AoR", (1100,200+i*50), (70,20), "AddOrRemove2", textColour=(255,255,255), tileName=name,tileNum=p[8])
        buttons.append(addOrRemoveButton)

    for b in buttons:
        b.show()
    pygame.display.update()
    input_box1 = InputBox(690, 140, 140, 32, bgColour, text="For Opponent")
    input_box2 = InputBox(1000, 140, 140, 32, bgColour, text="For You")
    input_boxes = [input_box1, input_box2]
    while not (computerChosen and userChosen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                computerChosen, userChosen = True, True
                pygame.quit()
                exit()
            # Accept or decline

           



            for box in input_boxes:
                if not (computerChosen and userChosen):
                    t = box.handle_event(event)
                    if t != None and t != "":
                        numbersOnly = True
                        for character in str(t):
                            if (character in "0123456789") == False:
                                numbersOnly = False
                        if numbersOnly:
                            cash = int(t)
                            # Check if it's for the computer or the player
                            if box.getName() == "For You":
                                playerIndex = 1
                            else:
                                playerIndex = 0
                            trade[playerIndex][0] = cash
                            clearScreen(690,200,150,30,(255,255,255))
                            clearScreen(1000,200,150,30,(255,255,255))                     
                            writeText(f"Cash: {trade[0][0]}", 700, 200, fontColour="Red")
                            writeText(f"Cash: {trade[1][0]}", 1000, 200, fontColour="Red")
                            pygame.display.update()
            for b in buttons:
                wants = b.click(event)
                
                if wants == "Accept":
                    userChosen = True
                    compsChoice = getComputersDecision(trade)

                    # If the computer agrees
                    if compsChoice == "Accept":
                        computerChosen = True
                        bothAccept = True

                    # If the computer declines :c
                    elif compsChoice == "Decline":
                        computerChosen = True
                        bothAccept = False

                elif wants == "Decline":
                    print("Aww")
                    userChosen = True
                    computerChosen = True
                    bothAccept = False

                elif wants == "AddOrRemove1" or wants == "AddOrRemove2":
                    wantedAddOrRemove = b.getAddOrRemove()
                    # Players Giving/Keeping
                    if wantedAddOrRemove == "Add1":
                        trade[0].append([b.getTileName(),b.getTileNum()])
                        newColour = (0,255,0)
                        text = "Trade"
                    elif wantedAddOrRemove == "Remove1":
                        trade[0].remove([b.getTileName(),b.getTileNum()])
                        newColour = (255,0,0)
                        text = "Keep"
                    # Computer Giving/Keeping
                    elif wantedAddOrRemove == "Add2":
                        trade[1].append([b.getTileName(),b.getTileNum()])
                        newColour = (0,255,0)
                        text = "Trade"
                    elif wantedAddOrRemove == "Remove2":
                        trade[1].remove([b.getTileName(),b.getTileNum()])
                        newColour = (255,0,0)
                        text = "Keep"

                    else:
                        newColour = (0,0,255)
                        text = "Huh?"

                    # Add backgrounds for the buttons
                    surface = pygame.Surface((80,40))
                    surface.fill((newColour))
                    screen.blit(surface, b.getPosition())
                    writeText(text, b.getPosition()[0], b.getPosition()[1])
                    pygame.display.update()

        for box in input_boxes:
            box.update()
            box.draw(screen)





    # Transfer the items T_T
    forComputer, forPlayer = trade[0], trade[1]
    for item in forComputer:
        if not isinstance(item,int):
            properties[item[1]][2] = playersInvolvedInTrade[1]
        elif isinstance(item,int):
            playersData[playersIndexes[1]][1] += item
            playersData[playersIndexes[0]][1] -= item

    for item in forPlayer:
        if not isinstance(item,int):
            properties[item[1]][2] = playersInvolvedInTrade[0]
        elif isinstance(item,int):
            playersData[playersIndexes[0]][1] += item
            playersData[playersIndexes[1]][1] -= item

    print(f"Both accepted = {bothAccept}")
    clearScreen(561,110, 755,755,(255,255,255))
    pygame.display.update()
    return properties, playersData

def getComputersDecision(trade):
    print(f"Trade = {trade}")
    # Decide to accept or decline the trade

    return "Accept"

def unMortgagePrompt(tile,cost, reallyPlaying=False):
    if reallyPlaying:
        surface = pygame.Surface((400,300))
        surface.fill((255,2,255))
        screen.blit(surface, (730,320))
        # Box for the display :D
        writeText(f"Would you like to unmortgage {tile} for {cost}?", 730,420, fontSize=40)
        answered = False

        buttons = []

        # Yes Button
        yesButton = Button("Yes", (740,530), (180,40), buttonType="Yes")
        buttons.append(yesButton)
        # No Button
        noButton = Button("No!", (950,530), (180,40), buttonType="No")
        buttons.append(noButton)
        for b in buttons:
            b.show()
        while answered == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    answered = True
                    pygame.quit()
                    exit()

                for b in buttons:
                    wants = b.click(event)

                    if wants == "Yes":
                        buttons.clear()
                        answered = True
                        answer = wants
                    elif wants == "No":
                        buttons.clear()
                        answered = True
                        answer = wants
        # Clear the screen D:
        
        clearScreen(561,110, 755,755,(255,255,255))
        pygame.display.update()
    else:
        answer = "Yes"
    return answer

def unMortgageProperty(playersData, propertiesData, tile, player, reallyPlaying):
    # If the property is mortgaged
    if propertiesData[tile][7]:
        # The price for unmortgaging
        unmortgagePrice = propertiesData[tile][6]
        # Checks if the user wishes to unmortgage
        userWishesToUnmortgage = unMortgagePrompt(tile, unmortgagePrice, reallyPlaying)
        if userWishesToUnmortgage == "Yes":
            # Checks if the player can afford to unmortgage
            if playersData[player][1] > unmortgagePrice:
                # Then the user can afford to unmortgage!
                # The user is charged
                playersData[player][1] -= unmortgagePrice
                # The bank is paid for this transaction
                playersData[0][1] += unmortgagePrice

                # The property is unmortgaged!
                propertiesData[tile][7] = False

    return propertiesData, playersData

def mortgageProperty(playersData, propertiesData, tile, player):
    # If the property is not mortgaged
    if propertiesData[tile][7] == False:
        # The money for mortgaging
        unmortgagePrice = propertiesData[tile][6]
        # Checks if the user wishes to mortgage
        userWishesToMortgage = mortgagePrompt(unmortgagePrice, tile)
        if userWishesToMortgage == "Yes":
            # Checks if the player can afford to unmortgage
            # The user is paid
            playersData[player][1] += unmortgagePrice
            # The bank is charged for this transaction
            playersData[0][1] -= unmortgagePrice
            # The property is mortgaged!
            propertiesData[tile][7] = True
        else:
            print("You didn't wanna mortgage huh?")
    return propertiesData, playersData

def mortgagePrompt(cost, tile):
    if reallyPlaying:
        surface = pygame.Surface((400,300))
        surface.fill((255,2,255))
        screen.blit(surface, (730,320))
        # Box for the display :D
        writeText(f"Would you like to mortgage tile {tile} for M${cost}?", 730,420, fontSize=30)
        answered = False

        buttons = []

        # Yes Button
        yesButton = Button("Yes", (740,530), (180,40), buttonType="Yes")
        buttons.append(yesButton)
        # No Button
        noButton = Button("No!", (950,530), (180,40), buttonType="No")
        buttons.append(noButton)
        for b in buttons:
            b.show()
        while answered == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    answered = True
                    pygame.quit()
                    exit()

                for b in buttons:
                    wants = b.click(event)

                    if wants == "Yes":
                        buttons.clear()
                        answered = True
                        answer = wants
                    elif wants == "No":
                        buttons.clear()
                        answered = True
                        answer = wants
        # Clear the screen D:
        clearScreen(561,110, 755,755,(255,255,255))
        pygame.display.update()
    else:
        answer = "Yes"
    print(answer)
    return answer

def main(propertiesData, basePlateForNewPlayers, playersNames, legalPlayers, reallyPlaying = True, roundLimit = 1000000, playerCoords={"Purple":[1336, 893], "Red":[1366, 893], "Orange":[1336, 923], "Blue":[1366, 923]}):
    allHousesList = []
    buttons = []
    # Creates a variable to decide if the user is ready to begin playing or not
    gameReady = False
    count = 0

    # Goes through this loop until the user is ready to continue playing
    while gameReady == False:

        buttons = [Button("Next Player", (1780,60), (80,40), buttonType="NextPlayer")]
        if count > roundLimit:
            gameReady = False
        else:
            count += 1
            

            # Shows a menu to the user to ask what they wish to do
            if reallyPlaying:
                pass

            option = 1

            # If the user wishes to start a new game
            if option == 1:
                # Clear the screen
                clearScreen(0,0,1920,1010,colour=COLOUR_ACTIVE)
                # Add players to the game
                numberOfPlayersDesired, whichPlayers = setNumberOfPlayers(reallyPlaying, legalPlayers)
                
                playersData = addPlayers(numberOfPlayersDesired+1, basePlateForNewPlayers, playersNames, reallyPlaying)
                
                # Starts with the first player's turn
                turn = 1
                
                gameReady = True

                # No new file was loaded so
                fileLoaded = ""


            # If the user instead wishes to load a previously saved game
            elif option == 2:
                # Display the options for loading a saved game
                options = checkNumberOfSaves()
                displayChoices(options)

                # Gets the users choice
                choice = getUsersChoice(len(options))

                # If the user does not wish to return to the main menu
                if choice != 0:
                    # Loads the game
                    difficulty, turn, playersData, propertiesData = loadGame(choice)
                    # Difficulty is not yet used but will be for the AI opponents ;P

                    # Ends the loop
                    gameReady = True

                    # The file loaded is used to save onto so no duplicates are created
                    fileLoaded = f"Save{choice}"
                    
                # Otherwise the user wishes to return to the main menu

            # If the option is 3 then the user wants to close the game :(
            if option == 3:
                exit()

        
        # A loop to play until stopped
        stillPlaying = True
        # The loop

        numOfTurnsTaken = 0

        playersList = whichPlayers

        while stillPlaying:
            # First player is chosen
            player = turn

            numOfTurnsTaken += 1
            # Checks is the user wants to unmortgage a property
            for property in propertiesData:
                if property != []:
                    # Checks who the owner of the property is and if it's mortgaged
                    if property[2] == player and property[6] == True:
                        # Finds the price of the mortgage
                        unmortgagePrice = property[5]
                        # Asks the user if they want to unmortgage
                        wantToUnmortgage = unMortgagePrompt(unmortgagePrice, tile, reallyPlaying)
                        # If the user wants to unmortgage
                        if wantToUnmortgage == "yes":
                            # The property is then passed into the unmortgage function
                            propertiesData, playersData = unMortgageProperty(playersData, propertiesData, tile, player, unMortgagePrompt)
                            clearScreen(1480,0,200,80,(0,0,200))
                            # Show money for ALL players
                            displayUsersMoney(playersData[1][1],name="Purple")

            # Checks that there are still at least 2 players left.
            numberOfPlayersRemaining = 0
            for p in playersData:
                # If the player is still in the game
                if p[5] == True:
                    numberOfPlayersRemaining += 1
            
            # numberOfPlayersRemaining Must be at least 4 because bank and free parking 
            # are counted as players
            if numberOfPlayersRemaining < 4:
                stillPlaying = False
            # Checks if the player is still in the game
            if playersData[player][5] and stillPlaying:


                # The dice is rolled
                diceRoll = diceRoller()
                # If the player is in jail
                if playersData[player][4]:
                    # The prisoner is free if they roll a 6
                    if diceRoll == 6:
                        # Frees the prisoner
                        playersData[player][4] = False
                        # The player is moved
                        playersData = movePlayerBy(playersData, diceRoll, player)
                        # The tile the player moved to
                        tile = playersData[player][2] -1
                        
                        # The tile is checked for ownership, bills, etc
                        playersCoords = displayAllPlayers(colours=["Red", "Orange", "Blue", "Purple"], playerCoords=playerCoords)

                        playersData, properties, allHousesList  = checkTile(tile, player, playersData, properties, reallyPlaying, playersList[player-1], allHousesList)
                        # Changes the players turn to the next person
                        
                    else:
                        # Define WantToLeave as "N" until the user chooses otherwise
                        wantToLeave = "N"
                        # Checks if the player can afford to leave jail
                        if playersData[player][1] > 300:
                            # Checks if the player wants to pay to get out of jail
                            if reallyPlaying:
                                bankBalance = playersData[player][1]
                                wantToLeave = getUsersOpinion("Would you like to pay $300 to leave jail?", bankBalance, player=playersList[player-1])
                           
                        if wantToLeave == "Y":
                            # Frees the prisoner from the confines of jail
                            playersData[player][4] = False
                            # Charges the play $300 for leaving jail  :(
                            playersData[player][1] -= 300
                            # Gives the bank the money that the player used to leave jail :)
                            playersData[0][1] += 300

                        # If the player does not wish to pay to leave jail or can't afford to then they remain there :(
                        else:
                            if reallyPlaying:
                                print("You remain in jail :(")

                # If the player is not in jail
                else:
                    # The player is moved to that tile
                    playersData = movePlayerBy(playersData, diceRoll, player)

                    # The tile the player landed on
                    tile = playersData[player][2]
                    print(f"Tile = {tile}")


                    # Move the players tile
                    playerCoords = movePlayer(playersNames[player], convertTileNumToCoordinates(tile, player),playerCoords)
                    buttons2, playersCoords,  infoButtons, mortgageButtons = displayMainBoard(allHousesList, properties = propertiesData, playerCoords = playerCoords)
                    

                    # Clear screen of users money
                    if True:
                        clearScreen(1480,0,200,80,(0,0,200))
                        # Show money for ALL players

                        displayUsersMoney(playersData[1][1],name="Purple")






                    # The tile is checked for anything special
                    playersData, propertiesData, allHousesList = checkTile(tile, player, playersData, propertiesData, reallyPlaying, playersList[player-1], allHousesList)
                    buttons2, playersCoords,  infoButtons, mortgageButtons = displayMainBoard(allHousesList, properties = propertiesData, playerCoords = playerCoords)
                    #if reallyPlaying:
                        #print(playersNames[player-1],"has",playersData[player][1])
                # Checking for bankruptcy
                anyoneBankrupt, bankruptPlayer = checkForBankruptcy(playersData)

                if anyoneBankrupt == True:
                    # Someone is bankrupt!!

                    # If the bankrupt player is free parking, it's okay!
                    if bankruptPlayer == len(playersData)-1:
                        #if reallyPlaying:
                            #print("Free Parking is bankrupt. :(")
                        freeParkingPlayerNumber = len(playersData)-1
                        del(bankruptPlayer[bankruptPlayer.index(freeParkingPlayerNumber)])
                    # If the bank is bankrupt, the game ends.
                    if bankruptPlayer == "Bank":
                        #if reallyPlaying:
                            #print(bankruptPlayer,"is bankrupt!!! It's the bank?")
                        stillPlaying = False
                    # If the bank is not bankrupt
                    elif bankruptPlayer != "Free Parking":
                        playersData, propertiesData = bankruptPlayerProtocol(playersData, propertiesData, bankruptPlayer)
                        #if reallyPlaying:
                            #print(bankruptPlayer, "is bankrupt!!!")
                        
                # Asks the user if they wish to continue playing
                if reallyPlaying == True:
                    keepPlaying = getUsersOpinion("Keep Playing", playersData[player][1], player=playersList[player-1])
                    
                else:
                    keepPlaying = "Yes"
                if keepPlaying == "No":
                    stillPlaying = False
                else:
                    stillPlaying = True
            turn += 1
            if turn >= len(playersData)-1:
                turn = 1
           
            buttonsList = buttons + infoButtons + mortgageButtons + buttons2
            clearScreen(1480,0,200,80,(0,0,200))
            # Show money for ALL players

            displayUsersMoney(playersData[1][1],name="Purple")
            if player ==1: # If player is the user 🥴
                waitingForTurnToEnd = True
                for b in buttonsList:
                    b.show()
                while waitingForTurnToEnd:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waitingForTurnToEnd = False
                        for b in buttonsList:
                            wants = b.click(event)
                            if wants == "NextPlayer":
                                waitingForTurnToEnd = False
                                print("Next Player Please")
                            elif wants != None:
                                if "Info" in wants:
                                    print(f"Wants = {wants}")
                                    tileNum = int(wants[-2:])
                                    showInfoBox(tileNum, propertiesData)
                                    closeWindowButton = Button("X", (1034,290), (39,39), buttonType="CloseWindow")
                                    closeWindowButton.show()
                                    buttonsList.append(closeWindowButton)
                                if wants=="CloseWindow":
                                    print("Closing?")
                                    clearScreen(561,110, 755,755,(255,255,255))
                                    pygame.display.update()
                                if "Mortgage" in wants:
                                    # want = Mortgage08 or Mortgage17 etc
                                    tile = int(wants[-2:])
                                    print("Wanna Mortgage")
                                    propertiesData, playersData = mortgageProperty(playersData, propertiesData, tile, player)
                                    print(playersData)
                                    clearScreen(1480,0,200,80,(0,0,200))
                                    # Show money for ALL players

                                    displayUsersMoney(playersData[1][1],name="Purple")

                                elif "Unmortgage" in wants:
                                    # want = Unmortgage08 or Unmortgage17 etc
                                    tile = int( wants[-2:])
                                    print("Wanna UnMortgage")
                                    propertiesData, playersData = unMortgageProperty(playersData, propertiesData, tile, player, reallyPlaying)
                                    print(playersData)
                                    clearScreen(1480,0,200,80,(0,0,200))
                                    # Show money for ALL players
                                    displayUsersMoney(playersData[1][1],name="Purple")

                                if "Trade" in wants:
                                    displayTradingScreen()
                                    print("Trade Requested")
                                    tradeablePlayers = []
                                    writeText("Who would you like to trade with?",860,450,fontColour="Red")
                                    for p in playersNames:
                                        if p != playersNames[player]:
                                            tradeablePlayers.append(p)
                                    
                                    playerTradingWith = getUsersInput(tradeablePlayers, want="")
                                    print(f"You wanna trade with {playerTradingWith}? Ha, lol")
                                    #(properties, playersData, playersInvolvedInTrade)
                                    propertiesData, playersData = doTrade(propertiesData, playersData, (playersNames[player], playerTradingWith), playersNames)
                                    # Update the properties list
                                    mortgageButtons, infoButtons = updatePropertiesList(propertiesData)
                                    buttonsList += mortgageButtons + infoButtons
                                    # Update Money
                                    clearScreen(1480,0,200,80,(0,0,200))
                                    # Show money for ALL players
                                    displayUsersMoney(playersData[1][1],name="Purple")
            pygame.time.wait(1000)

            
            # Saves the game ;P
         #   autoSaveGame(playersData, propertiesData, turn, fileLoaded)

class people:
    def __init__(self, bankBalance, position, properties, lucky = False, buyEverything=False, buildEverything=False, useWinningStrat = False, getOutOfJail = False):
        self.bankBalance = bankBalance
        self.position = position
        self.properties = properties
        self.lucky = lucky
        self.buyEverything = buyEverything
        self.buildEverything = buildEverything
        self.useWinningStrategy = useWinningStrat
        self.getOutOfJail = getOutOfJail


    def changeBalance(self, newBalance):
        self.bankBalance = newBalance
    
    def changeProperties(self, newProperties):
        self.properties = newProperties

    def wantOutOfJail(self):
        if self.getOutOfJail == True:
            return True
        else:
            return False
    
    def wantToBuy(self, price):
        # Check it can be afforded lol
        if self.bankBalance > price:
            if self.buyEverything == True:
                return True
            else:
                return False
        else:
            return False

    def wantToBuild(self, priceOfHouses, numberOfHousesLeftToBuy):
        if self.buildEverything == True:
            numberCanBuy = self.bankBalance // priceOfHouses
            if numberCanBuy > numberOfHousesLeftToBuy:
                numberToBuy = numberOfHousesLeftToBuy
            else:
                numberToBuy = numberCanBuy
        else:
            numberToBuy = 0
        return numberToBuy




def getUsersOpinion(offer, bankBalance, player="user"):
    player = player.lower()

    if "keep playing" in offer.lower():
        return "Y"
    elif player == "user":
        writeText(f"Your balance is {bankBalance}. Your decision: ", 800,600,fontColour="Blue")
        decision = getUsersInput(["Y","N"])

        return decision
    elif player == "jeff":
        if "jail" in offer.lower():
            return "N"
        elif "build" in offer.lower():
            return "Y"
        elif "buy" in offer.lower():
            return "Y"
    elif player == "tom":
        if "jail" in offer.lower():
            return "N"
        elif "build" in offer.lower():
            return "Y"
        elif "buy" in offer.lower():
            return "Y"    
    elif player == "tim":
        if "jail" in offer.lower():
            return "N"
        elif "build" in offer.lower():
            return "Y"
        elif "buy" in offer.lower():
            return "Y"
    elif player == "richard":
        if "jail" in offer.lower():
            return "no"
        elif "build" in offer.lower():
            return "yes"
        elif "buy" in offer.lower():
            return "yes"
    elif player == "jeremy":
        if "jail" in offer.lower():
            return "N"
        elif "build" in offer.lower():
            return "Y"
        elif "buy" in offer.lower():
            return "Y"
    





def addToFile(count, numberOfTurns):
    emptyString = ""
    for tile in count:
        emptyString += f"{tile},"
    emptyString += f"{numberOfTurns},\n"
    file = open("tilePopularity.csv", "a")
    file.write(emptyString)
    file.close()


def getMenuOptions():
    option = ""
    # While the option is not valid
    while option != 1 and option != 2 and option != 3:
        # It tries again :)
        option = input("")
        try:
            option = int(option)
        except:
            print("Only 1,2 or 3 are valid inputs!!!!")
    
    return option



def autoSaveGame(allPlayersData, allPropertiesData, playersTurn, loadedFile = ""):
    import os
    # Automatically saves the game after every players turn in case they wish to continue playing later on ;P

    # We want the file to be named in a way that allows multiple different saves
    # So the save slots will be numbered, 1 - 5

    # If it's a new game 
    if loadedFile == "":
        path = os.getcwd()+f"/SavedGames/"
        number = len(os.listdir(path))+1
        loadedFile = f"{path}Save{number}"

    # Sets the file type for the file name that is opened
    fileName = loadedFile+".txt"

    # Opens a file to save to
    file = open(fileName, "w")

    
    # Saves who's turn it is as well ;P
    file.write(str(playersTurn)+"\n")

    # Saves the players Data
    file.write(str(allPlayersData)+"\n")

    # Saves all the property Data
    file.write(str(allPropertiesData)+"\n")

    # Saves who's turn it is as well ;P
    file.write(str(playersTurn))

    # Closes the file to save the changes
    file.close()

def checkNumberOfSaves():
    import os


    # The path to the directory that the game is saved in
    currentDirectory = os.getcwd()
    # The path to where the saved games are stored
    savesDirectory = currentDirectory + "/SavedGames/"

    # Creates a list of all the files in the save directory
    filesInSaveDirectory = os.listdir(savesDirectory)

    # Creates an empty list to store all of the saved game files
    options = []

    # Checks every file in the saved games folder
    for file in filesInSaveDirectory:
        # Checks if the file is a text file
        if file[-4:] == ".txt":
            # Stores just the file name with the .txt extension
            fileName = file[:-4]
            options.append(fileName)

    return options

def displayChoices(choices):
    import os
    from datetime import datetime

    count = 1
    for choice in choices:
        # The name of the saved file
        name = choice

        # Finds the path of the file
        path = os.getcwd()+f"/SavedGames/{choice}.txt"

        # Reads the file to find the difficulty ;P
        file = open(path, "r")
        difficulty = file.readline()
        file.close()

        # Checks the date it was saved ;P
        dateSaved = os.path.getmtime(path)
        # Converts the date to a readable format
        dateSaved = datetime.fromtimestamp(dateSaved).strftime('%d-%m-%y %H:%M:%S')


        
        # Increase the count by 1
        count += 1  

def getUsersChoice(numberOfChoices):
    # Creates a loop to ask the user for a valid input until 1 is provided
    valid = False
    while valid == False:

        # Receives an input from the user
        choice = input("")

        # Checks if the choice is a number
        if choice.isnumeric():
            # Converts the choice to a number
            choice = int(choice)
            # If the choice is valid
            if choice <= numberOfChoices and choice > 0:
                valid = True
            


    return choice

def loadGame(desiredGame):
    import os

    # The path of the desired game
    path = f"{os.getcwd()}/SavedGames/Save{desiredGame}.txt"

    # Opens the file
    file = open(path, "r")
    # Reads the file
    gameData = file.readlines()
    # Closes the file
    file.close()
    
    # Gets the difficulty
    difficulty = str(gameData[0]).replace("\n","")

    # Finds out who's turn it is
    playersTurn = int(str(gameData[1]).replace("\n",""))

    # Finds out all of the data from the players
    playersData = str(gameData[2]).replace("\n","")

    # Finds out all of the data about the properties
    propertiesData = str(gameData[3]).replace("\n","")

    return difficulty, playersTurn, playersData, propertiesData

 







reallyPlaying = True
roundLimit = 1000000


























legalPlayers = ["jeff", "tom", "tim", "richard", "jeremy"]




buttons = [displayMainMenu()]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for b in buttons:
            wants = b.click(event)
            if wants == "AcceptButton":
                buttons.clear()
                buttons = removeWindow("TextBox")

            elif wants == "CloseButton":
                buttons.clear()
                buttons = removeWindow("TextBox")

            elif wants == "MainMenu":
                buttons = [displayMainMenu()]
                bgColour = COLOUR_ACTIVE

            elif wants == "NewGame":
                # Executes the program
                main(pd, basePlateForNewPlayers, playersNames, legalPlayers, reallyPlaying, roundLimit)


    clock.tick(10)
