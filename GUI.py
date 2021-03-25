import pygame, math, time, sys, os
from ast import literal_eval



class GUI_Support:

    def initDisplay(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)

    def isQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False

    
    def drawGraphics(self, position, screen, dims):
        handX, handY, handZ = position
        handXVisual = handX
        handZVisual = handZ
        #Centers the X and Z coordinates
        handY = handY * -1
        handX += 400
        handZ += 400
        handY += 850
        width, height = dims
        screen.fill((175, 238, 247))

        circleRadius = 20
        pygame.draw.circle(screen, (0, 0, 0), (handX, handZ), circleRadius)
        pygame.draw.circle(screen, (0, 0, 0), (1050, handY), circleRadius)

        #Draws the circle and lines across the screen
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 150, 5)

        #Vertical Line                       
        pygame.draw.line(screen, (0, 0, 0), (800, 0), (800, 800))

        #Y Axis Deadzone
        pygame.draw.line(screen, (0, 0, 0), (800, 300), (1300, 300))
        pygame.draw.line(screen, (0, 0, 0), (800, 500), (1300, 500))

        #                                       -             -             |          /          \            -          -
        #pygame.draw.polygon(screen, (0, 0, 0), ((560, 410), (620,410), (620, 425), (650, 400), (620, 375), (620,390), (560,390)))
        #***************************************************************************
        # RIGHT ARROW
        pygame.draw.line(screen, (0, 0, 0), (550, 410), (620,410), 2)
        pygame.draw.line(screen, (0, 0, 0), (620,410), (620, 425), 2)
        pygame.draw.line(screen, (0, 0, 0), (620, 425), (650, 400), 2)
        pygame.draw.line(screen, (0, 0, 0), (650, 400), (620, 375), 2)
        pygame.draw.line(screen, (0, 0, 0), (620, 375), (620,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (620,390), (550,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (550,390), (550, 410), 2)
        wRight = arrowFont.render(f'Right', True, (0,0,0))
        screen.blit(wRight, (562, 388))

        # LEFT ARROW
        pygame.draw.line(screen, (0, 0, 0), (250, 410), (180,410), 2)
        pygame.draw.line(screen, (0, 0, 0), (180,410), (180, 425), 2)
        pygame.draw.line(screen, (0, 0, 0), (180, 425), (150, 400), 2)
        pygame.draw.line(screen, (0, 0, 0), (150, 400), (180, 375), 2)
        pygame.draw.line(screen, (0, 0, 0), (180, 375), (180,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (180,390), (250,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (250,390), (250, 410), 2)
        wLeft = arrowFont.render(f'Left', True, (0,0,0))
        screen.blit(wLeft, (200, 388))

        # FORWARD ARROW
        pygame.draw.line(screen, (0, 0, 0), (410, 250), (410,180), 2)
        pygame.draw.line(screen, (0, 0, 0), (410,180), (425, 180), 2)
        pygame.draw.line(screen, (0, 0, 0), (425, 180), (400, 150), 2)
        pygame.draw.line(screen, (0, 0, 0), (400, 150), (375, 180), 2)
        pygame.draw.line(screen, (0, 0, 0), (375, 180), (390,180), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,180), (390,250), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,250), (410, 250), 2)
        wF = arrowFont.render(f'F', True, (0,0,0))
        screen.blit(wF, (395, 157))
        wo = arrowFont.render(f'o', True, (0,0,0))
        screen.blit(wo, (395, 169))
        wr = arrowFont.render(f'r', True, (0,0,0))
        screen.blit(wr, (395, 181))
        ww = arrowFont.render(f'w', True, (0,0,0))
        screen.blit(ww, (395, 193))
        wa = arrowFont.render(f'a', True, (0,0,0))
        screen.blit(wa, (395, 205))
        wr = arrowFont.render(f'r', True, (0,0,0))
        screen.blit(wr, (395, 217))
        wd = arrowFont.render(f'd', True, (0,0,0))
        screen.blit(wd, (395, 229))

        # REVERSE ARROW
        pygame.draw.line(screen, (0, 0, 0), (410, 549), (410,620), 2)
        pygame.draw.line(screen, (0, 0, 0), (410,620), (425, 620), 2)
        pygame.draw.line(screen, (0, 0, 0), (425, 620), (400, 650), 2)
        pygame.draw.line(screen, (0, 0, 0), (400, 650), (375, 620), 2)
        pygame.draw.line(screen, (0, 0, 0), (375, 620), (390,620), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,620), (390,549), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,549), (410, 549), 2)
        wR = arrowFont.render(f'R', True, (0,0,0))
        screen.blit(wR, (395, 550))
        we = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(we, (395, 562))
        wv = arrowFont.render(f'v', True, (0,0,0))
        screen.blit(wv, (395, 574))
        we = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(we, (395, 586))
        wr = arrowFont.render(f'r', True, (0,0,0))
        screen.blit(wr, (395, 598))
        ws = arrowFont.render(f's', True, (0,0,0))
        screen.blit(ws, (395, 610))
        we = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(we, (395, 622))

        #DESCEND ARROW
        pygame.draw.line(screen, (0, 0, 0), (840, 505), (840,575), 2)
        pygame.draw.line(screen, (0, 0, 0), (840,575), (855, 575), 2)
        pygame.draw.line(screen, (0, 0, 0), (855, 575), (830, 605), 2)
        pygame.draw.line(screen, (0, 0, 0), (830, 605), (805, 575), 2)
        pygame.draw.line(screen, (0, 0, 0), (805, 575), (820,575), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,575), (820,505), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,505), (840, 505), 2)
        wDescend = arrowFont.render(f'D', True, (0,0,0))
        screen.blit(wDescend, (825, 502))
        wDescend = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(wDescend, (825, 514))
        wDescend = arrowFont.render(f's', True, (0,0,0))
        screen.blit(wDescend, (825, 526))
        wDescend = arrowFont.render(f'c', True, (0,0,0))
        screen.blit(wDescend, (825, 538))
        wDescend = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(wDescend, (825, 550))
        wDescend = arrowFont.render(f'n', True, (0,0,0))
        screen.blit(wDescend, (825, 562))
        wDescend = arrowFont.render(f'd', True, (0,0,0))
        screen.blit(wDescend, (825, 574))

        # ASCEND ARROW
        pygame.draw.line(screen, (0, 0, 0), (840, 295), (840,225), 2)
        pygame.draw.line(screen, (0, 0, 0), (840,225), (855, 225), 2)
        pygame.draw.line(screen, (0, 0, 0), (855, 225), (830, 195), 2)
        pygame.draw.line(screen, (0, 0, 0), (830, 195), (805, 225), 2)
        pygame.draw.line(screen, (0, 0, 0), (805, 225), (820,225), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,225), (820,295), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,295), (840, 295), 2)
        wAscend = arrowFont.render(f'A', True, (0,0,0))
        screen.blit(wAscend, (825, 210))
        wAscend = arrowFont.render(f's', True, (0,0,0))
        screen.blit(wAscend, (825, 222))
        wAscend = arrowFont.render(f'c', True, (0,0,0))
        screen.blit(wAscend, (825, 234))
        wAscend = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(wAscend, (825, 246))
        wAscend = arrowFont.render(f'n', True, (0,0,0))
        screen.blit(wAscend, (825, 258))
        wAscend = arrowFont.render(f'd', True, (0,0,0))
        screen.blit(wAscend, (825, 270))

        #Take off                                _______
        takeOffVisual = myFont.render(f'Take-Off:_____T', True, (0,0,0))
        screen.blit(takeOffVisual, (12,712))

        #Land                             _____________
        landVisual = myFont.render(f'Land:________L', True, (0,0,0))
        screen.blit(landVisual, (12,731))

        # Rotate Left: a                         ___
        rotateLeft = myFont.render(f'Rotate-Left:___A', True, (0,0,0))
        screen.blit(rotateLeft, (12,750))

        # Rotate Right: d                         
        rotateRight = myFont.render(f'Rotate-Right:__D', True, (0,0,0))
        screen.blit(rotateRight, (12,772))

        #box
        pygame.draw.line(screen, (0, 0, 0), (4, 710), (4,797), 2)
        pygame.draw.line(screen, (0, 0, 0), (4, 797), (155,797), 2)
        pygame.draw.line(screen, (0, 0, 0), (155,797), (155,710), 2)
        pygame.draw.line(screen, (0, 0, 0), (155, 710), (4,710), 2)
        
        #show battery % 
        #telloBattery = tello.get_battery()
        #screen.blit(telloBattery, (100,0))
        

         
        showXZCoords = myFont.render(f'X,Z Coords:{handXVisual},{handZVisual}', True, (0,0,0))
        screen.blit(showXZCoords, (0, 10))

        handYVisual = 400 - handY 
        showYCoords = myFont.render(f'Y Coords:{handYVisual}', True, (0,0,0))
        screen.blit(showYCoords, (810, 0))




    






#Alternates between the two coordinate points
def main():
    x, y, z = 300, 50 ,250
    guiSupport.drawGraphics((x, y, z), screen, (xWidth, yHeight))
    pygame.display.update()
    time.sleep(.1)
    x, y, z = 100, 100, 250
    guiSupport.drawGraphics((x, y, z), screen, (xWidth, yHeight))
    pygame.display.update()
    time.sleep(.1)
    x, y, z = -400, 710, -387
    guiSupport.drawGraphics((x, y, z), screen, (xWidth, yHeight))
    pygame.display.update()
    time.sleep(.1)
    x, y, z = -268, 850, 250
    guiSupport.drawGraphics((x, y, z), screen, (xWidth, yHeight))
    pygame.display.update()
    time.sleep(.1)
    x, y, z = 69, 420, 400
    guiSupport.drawGraphics((x, y, z), screen, (xWidth, yHeight))
    pygame.display.update()
    time.sleep(.1)

#Initializes GUI 
if __name__ == "__main__":
    path = os.getcwd()
    guiSupport = GUI_Support()
    xWidth = 1300
    yHeight = 800
    screen = guiSupport.initDisplay((xWidth, yHeight))
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 22)
    #********************************
    arrowFont = pygame.font.SysFont('Comic Sans MS', 18)
    
    
    icon = pygame.image.load(path + '\Drone.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Drone Controller')
    
    while 1:
        main()
    