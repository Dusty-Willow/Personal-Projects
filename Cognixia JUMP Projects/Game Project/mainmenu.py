import pygame
import sys

from guiUtilities import drawButton
from rps import runRPS
from ttt import runTTT

# Constructor initialization
myPyGame = pygame.init()

# Setting up screen resolution and opening window
resolution = (720, 720)
WIN = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Games")

# Color, Text and Font Settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
DIMGREY = (105, 105, 105)
myFont = pygame.font.SysFont('arial', 35)

# Saving screen dimensions to reusable variables
screenWidth = WIN.get_width()
screenHeight = WIN.get_height()

# Game running check
runGame = True

# Menu button positions
buttons = {
    "QUIT" : ((screenWidth / 2) - 150, (screenHeight / 2) + 60),
    "RPS" : ((screenWidth / 2) - 150, (screenHeight / 2) + 10),
    "TTT" : ((screenWidth / 2) - 150, (screenHeight / 2) + -40)
}

# Menu button texts
text = {
    "QUIT" : myFont.render('Quit', True, BLACK),
    "RPS" : myFont.render('Rock Paper Scissors', True, BLACK),
    "TTT" : myFont.render('Tic Tac Toe', True, BLACK)
}

# Menu loop
while runGame:

    # Sets window header
    pygame.display.set_caption("Game Runner - Main Menu")

    # Functionality for input events
    for event in pygame.event.get():
        # Functionality for if Player closes application
        if event.type == pygame.QUIT:
            runGame = False
            pygame.quit()

        # Mouse click detection
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if mouse clicked QUIT button
            if ((buttons['QUIT'][0] <= mouse[0] <= (buttons['QUIT'][0] + 300)) and (buttons['QUIT'][1] <= mouse[1] <= (buttons['QUIT'][1] + 40))):
                runGame = False
                pygame.quit()
            # Checks if mouse clicked ROCK PAPER SCISSORS button
            elif ((buttons['RPS'][0] <= mouse[0] <= (buttons['RPS'][0] + 300)) and (buttons['RPS'][1] <= mouse[1] <= (buttons['RPS'][1] + 40))):
                runRPS(WIN, mouse, screenWidth, screenHeight, myFont)
            # Checks if mouse clicked Tic Tac Toe button
            elif ((buttons['TTT'][0] <= mouse[0] <= (buttons['TTT'][0] + 300)) and (buttons['TTT'][1] <= mouse[1] <= (buttons['TTT'][1] + 40))):
                runTTT(WIN, mouse, screenWidth, screenHeight, myFont)

    # Fills screen with specific color
    WIN.fill(DIMGREY)

    # Updates mouse cursor position and stores coordinates in a tuple
    mouse = pygame.mouse.get_pos()

    # Draws TTT button
    drawButton(WIN, WHITE, GREY, buttons['TTT'][0], buttons['TTT'][1], 300, 42, text['TTT'], 80, mouse)

    # Draws RPS button
    drawButton(WIN, WHITE, GREY, buttons['RPS'][0], buttons['RPS'][1], 300, 42, text['RPS'], 20, mouse)

    # Draws QUIT button
    drawButton(WIN, WHITE, GREY, buttons['QUIT'][0], buttons['QUIT'][1], 300, 42, text['QUIT'], 113, mouse)

    # Updates game frames
    pygame.display.update()