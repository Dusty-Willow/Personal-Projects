import pygame
import random
import json
import time
import os
from guiUtilities import drawButton, drawSystemMessages, drawScore

# Game variables and placeholders
wins = 0
losses = 0
ties = 0
prompt = ""
gameWon = False
state = "player"
winner = None
incrementScore = False
pygame.init()

# Board variables and possible moves for Player and CPU
dummyBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
myBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
cpuMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xoFont = pygame.font.SysFont('arial', 80)

# Function to register Player moves
def playerMove(mouse, cellPositions):
    global state, myBoard, cpuMoves, playerMoves
    
    # Checks to see which grid cell player chooses
    if (state == "player"):
        if ((cellPositions['TOPLEFT'][0] <= mouse[0] <= (cellPositions['TOPLEFT'][0] + 90)) and (cellPositions['TOPLEFT'][1] <= mouse[1] <= (cellPositions['TOPLEFT'][1] + 90)) and myBoard[0] == "IGNORE"):
            placeXO("X", 0)
            cpuMoves.remove(1)
            playerMoves.remove(1)
            state = "cpu"
        elif ((cellPositions['TOPMID'][0] <= mouse[0] <= (cellPositions['TOPMID'][0] + 90)) and (cellPositions['TOPMID'][1] <= mouse[1] <= (cellPositions['TOPMID'][1] + 90)) and myBoard[1] == "IGNORE"):
            placeXO("X", 1)
            cpuMoves.remove(2)
            playerMoves.remove(2)
            state = "cpu"
        elif ((cellPositions['TOPRIGHT'][0] <= mouse[0] <= (cellPositions['TOPRIGHT'][0] + 90)) and (cellPositions['TOPRIGHT'][1] <= mouse[1] <= (cellPositions['TOPRIGHT'][1] + 90)) and myBoard[2] == "IGNORE"):
            placeXO("X", 2)
            cpuMoves.remove(3)
            playerMoves.remove(3)
            state = "cpu"
        elif ((cellPositions['MIDLEFT'][0] <= mouse[0] <= (cellPositions['MIDLEFT'][0] + 90)) and (cellPositions['MIDLEFT'][1] <= mouse[1] <= (cellPositions['MIDLEFT'][1] + 90)) and myBoard[3] == "IGNORE"):
            placeXO("X", 3)
            cpuMoves.remove(4)
            playerMoves.remove(4)
            state = "cpu"
        elif ((cellPositions['MIDMID'][0] <= mouse[0] <= (cellPositions['MIDMID'][0] + 90)) and (cellPositions['MIDMID'][1] <= mouse[1] <= (cellPositions['MIDMID'][1] + 90)) and myBoard[4] == "IGNORE"):
            placeXO("X", 4)
            cpuMoves.remove(5)
            playerMoves.remove(5)
            state = "cpu"
        elif ((cellPositions['MIDRIGHT'][0] <= mouse[0] <= (cellPositions['MIDRIGHT'][0] + 90)) and (cellPositions['MIDRIGHT'][1] <= mouse[1] <= (cellPositions['MIDRIGHT'][1] + 90)) and myBoard[5] == "IGNORE"):
            placeXO("X", 5)
            cpuMoves.remove(6)
            playerMoves.remove(6)
            state = "cpu"
        elif ((cellPositions['BOTLEFT'][0] <= mouse[0] <= (cellPositions['BOTLEFT'][0] + 90)) and (cellPositions['BOTLEFT'][1] <= mouse[1] <= (cellPositions['BOTLEFT'][1] + 90)) and myBoard[6] == "IGNORE"):
            placeXO("X", 6)
            cpuMoves.remove(7)
            playerMoves.remove(7)
            state = "cpu"
        elif ((cellPositions['BOTMID'][0] <= mouse[0] <= (cellPositions['BOTMID'][0] + 90)) and (cellPositions['BOTMID'][1] <= mouse[1] <= (cellPositions['BOTMID'][1] + 90)) and myBoard[7] == "IGNORE"):
            placeXO("X", 7)
            cpuMoves.remove(8)
            playerMoves.remove(8)
            state = "cpu"
        elif ((cellPositions['BOTRIGHT'][0] <= mouse[0] <= (cellPositions['BOTRIGHT'][0] + 90)) and (cellPositions['BOTRIGHT'][1] <= mouse[1] <= (cellPositions['BOTRIGHT'][1] + 90)) and myBoard[8] == "IGNORE"):
            placeXO("X", 8)
            cpuMoves.remove(9)
            playerMoves.remove(9)
            state = "cpu"

# Function to register CPU moves
def cpuMove():
    global state, cpuMoves        

    # Decide what cell CPU chooses
    if (state == "cpu" and bool(cpuMoves)):
        cpuChoice = random.choice(cpuMoves)
        match cpuChoice:
            case 1:
                placeXO("O", 0)
                cpuMoves.remove(1)
                playerMoves.remove(1)
            case 2:
                placeXO("O", 1)
                cpuMoves.remove(2)
                playerMoves.remove(2)
            case 3:
                placeXO("O", 2)
                cpuMoves.remove(3)
                playerMoves.remove(3)
            case 4:
                placeXO("O", 3)
                cpuMoves.remove(4)
                playerMoves.remove(4)
            case 5:
                placeXO("O", 4)
                cpuMoves.remove(5)
                playerMoves.remove(5)
            case 6:
                placeXO("O", 5)
                cpuMoves.remove(6)
                playerMoves.remove(6)
            case 7:
                placeXO("O", 6)
                cpuMoves.remove(7)
                playerMoves.remove(7)
            case 8:
                placeXO("O", 7)
                cpuMoves.remove(8)
                playerMoves.remove(8)
            case 9:
                placeXO("O", 8)
                cpuMoves.remove(9)
                playerMoves.remove(9)
    
    state = "player"

# Function to check if the current game state is indicative of a winner
def winCheck(screen, screenHeight):
    global dummyBoard, winner, incrementScore
    RED = (255, 0, 0)

    # Check Row Victory
    for row in range(0, 9, 3):
        if((dummyBoard[row] == dummyBoard[row + 1] == dummyBoard[row + 2]) and not (dummyBoard[row] == "IGNORE")):

            if (dummyBoard[row] == "X" and winner == None):
                incrementScore = True
                winner = "Player"
            elif (dummyBoard[row] == "O" and winner == None):
                incrementScore = True
                winner = "CPU"

            match row:
                case 0:
                    pygame.draw.line(screen, RED, (120 - 50, screenHeight / 3 + 45), (500 + 140, screenHeight / 3 + 45), 7)
                case 3:
                    pygame.draw.line(screen, RED, (120 - 50, screenHeight / 3 + 150 + 45), (500 + 140, screenHeight / 3 + 150 + 45), 7)
                case 6:
                    pygame.draw.line(screen, RED, (120 - 50, screenHeight / 3 + 300 + 45), (500 + 140, screenHeight / 3 + 300 + 45), 7)        

    # Check Column Victory
    for col in range(0, 3):
        if((dummyBoard[col] == dummyBoard[col + 3] == dummyBoard[col + 6]) and not (dummyBoard[col] == "IGNORE")):

            if (dummyBoard[col] == "X" and winner == None):
                incrementScore = True
                winner = "Player"
            elif (dummyBoard[col] == "O" and winner == None):
                incrementScore = True
                winner = "CPU"

            match col:
                case 0:
                    pygame.draw.line(screen, RED, (120 + 45, screenHeight / 3 - 50), (120 + 45, screenHeight / 3 + 300 + 140), 7)
                case 1:
                    pygame.draw.line(screen, RED, (120 + 45 + 200, screenHeight / 3 - 50), (120 + 45 + 200, screenHeight / 3 + 300 + 140), 7)
                case 2:
                    pygame.draw.line(screen, RED, (120 + 45 + 380, screenHeight / 3 - 50), (120 + 45 + 380, screenHeight / 3 + 300 + 140), 7)        

        # Check diagonal victory from top left to bottom right
        if((dummyBoard[0] == dummyBoard[4] == dummyBoard[8]) and not (dummyBoard[0] == "IGNORE")):
            
            if (dummyBoard[0] == "X" and winner == None):
                incrementScore = True
                winner = "Player"
            elif (dummyBoard[0] == "O" and winner == None):
                incrementScore = True
                winner = "CPU"

            pygame.draw.line(screen, RED, (120 - 35, screenHeight / 3 - 30), (120 + 30 + 380 + 95, screenHeight / 3 + 300 + 110), 7)        
    
        # Check diagonal victory from top right to bottom left
        if((dummyBoard[2] == dummyBoard[4] == dummyBoard[6]) and not (dummyBoard[2] == "IGNORE")):
            
            if (dummyBoard[2] == "X"):
                winner = "Player"
            elif (dummyBoard[2] == "O"):
                winner = "CPU"

            pygame.draw.line(screen, RED, (120 + 470 + 35, screenHeight / 3 - 30), (120 - 35, screenHeight / 3 + 300 + 110), 7)   

    # Check if any moves left for Player or CPU
    movesLeft()

# Function to check if the current game state is indicative of a tie
def movesLeft():
    global cpuMoves, playerMoves, winner, incrementScore
    if (bool(cpuMoves) == False and bool(playerMoves) == False and winner == None):
        incrementScore = True
        winner = "tie"

# Function to reset game state and variables
def resetGame(string):
    global dummyBoard, myBoard, cpuMoves, playerMoves, prompt, winner
    winner = None
    prompt = string
    dummyBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
    myBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
    cpuMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    playerMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function to place X and O on code-based board
def placeXO(XO, position):
    global myBoard, dummyBoard

    dummyBoard[position] = XO
    myBoard[position] = xoFont.render(XO, True, (0,0,0))

# Function to save win, loss and tie count when game is closed or Player returns to menu
def saveScores():
    global wins, losses, ties
    
    # Save wins, loss and tie score to gamelogs file
    try:
        with open('gamelogs.json', 'rt') as file:
            data = json.load(file)   

        data['TTT']['Wins'] = wins
        data['TTT']['Losses'] = losses
        data['TTT']['Ties'] = ties

        with open('gamelogs.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("This file doesn't exist.")

# Function to draw Tic Tac Toe grid. This includes X and O based on code-based board 
def drawGrid(screen, lineColor, screenWidth, screenHeight, cellColor, cellHover, buttons, mouse):
    global myBoard
    # Vertical grid lines
    pygame.draw.line(screen, lineColor, (screenWidth / 3 + 30, 220), (screenWidth / 3 + 30, screenHeight - 50), 7)
    pygame.draw.line(screen, lineColor, (screenWidth / 3 * 2 - 30, 220), (screenWidth / 3 * 2 - 30, screenHeight - 50), 7)
 
    # Horizontal grid lines
    pygame.draw.line(screen, lineColor, (80, screenHeight / 3 + 40 + 75), (screenWidth - 80, screenHeight / 3 + 40 + 75), 7)
    pygame.draw.line(screen, lineColor, (80, screenHeight / 3 * 2 - 40 + 75), (screenWidth - 80, screenHeight / 3 * 2 - 40 + 75), 7)

    # Drawing cells
    drawButton(screen, cellColor, cellHover, 120, screenHeight / 3, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[0], 22, mouse)
    drawButton(screen, cellColor, cellHover, 120, screenHeight / 3 + 150, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[3], 22, mouse)
    drawButton(screen, cellColor, cellHover, 120, screenHeight / 3 + 300, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[6], 22, mouse)
    drawButton(screen, cellColor, cellHover, 320, screenHeight / 3, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[1], 22, mouse)
    drawButton(screen, cellColor, cellHover, 320, screenHeight / 3 + 150, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[4], 22, mouse)
    drawButton(screen, cellColor, cellHover, 320, screenHeight / 3 + 300, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[7], 22, mouse)
    drawButton(screen, cellColor, cellHover, 500, screenHeight / 3, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[2], 22, mouse)
    drawButton(screen, cellColor, cellHover, 500, screenHeight / 3 + 150, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[5], 22, mouse)
    drawButton(screen, cellColor, cellHover, 500, screenHeight / 3 + 300, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[8], 22, mouse)

# Function to instantiate and run Tic Tac Toe game
def runTTT(screen, mouse, screenWidth, screenHeight, myFont):
    runTTT = True
    global prompt, wins, losses, ties, state, winner, incrementScore

    # Sets window header
    pygame.display.set_caption("Tic Tac Toe")

    # Load data regarding wins, losses and ties from gamelogs file
    try:
        with open('gamelogs.json', 'rt') as file:
            data = json.load(file)

        wins = data['TTT']['Wins']
        losses = data['TTT']['Losses']
        ties = data['TTT']['Ties']
    except:
        print("This file doesn't exist.")


    # Color codes used
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (192, 192, 192)
    DIMGREY = (105, 105, 105)

    # Buttons used and their positions
    tttButtons = {
        "BACK" : (10, 20),
        "AGAIN" : ((screenWidth / 2) - 130, 40),
        "GRIDCELL" : (90, 90),
    }

    # Button text
    tttText = {
        "BACK" : myFont.render('Back', True, BLACK),
        "AGAIN" : myFont.render('Play again!', True, BLACK)
    }

    # Position for each grid cell on screen
    cellPos = {
    "TOPLEFT" : (120, screenHeight / 3),
    "MIDLEFT" : (120, screenHeight / 3 + 150),
    "BOTLEFT" : (120, screenHeight / 3 + 300),
    "TOPMID" : (320, screenHeight / 3),
    "MIDMID" : (320, screenHeight / 3 + 150),
    "BOTMID" : (320, screenHeight / 3 + 300),
    "TOPRIGHT" : (500, screenHeight / 3),
    "MIDRIGHT" : (500, screenHeight / 3 + 150),
    "BOTRIGHT" : (500, screenHeight / 3 + 300)

    }

    # Messages to be showed on screen
    systemMessages = {
        "INITIAL" : myFont.render("Let's play Tic Tac Toe.", True, WHITE),
        "PLAYERTURN" : myFont.render("Player turn. Waiting for decisions.", True, WHITE),
        "CPUTURN" : myFont.render("CPU turn. Making decision.", True, WHITE),
        "VICTORY" : myFont.render("Player wins!", True, WHITE),
        "LOSS" : myFont.render("CPU wins!", True, WHITE),
        "TIE" : myFont.render("It's a tie!", True, WHITE),
        "AGAIN" : myFont.render("Would you like to play again?", True, WHITE)
    }

    # Set up initial prompt message and replay message
    prompt = systemMessages['INITIAL']
    replay = systemMessages['AGAIN']
    
    playAgain = False

    # Reset game state when game first starts
    resetGame(systemMessages["INITIAL"])

    # Start game loop
    while runTTT:
        # Show score on screen
        scoreWins = myFont.render(f"Wins: {wins}", True, BLACK)
        scoreLosses = myFont.render(f"Losses: {losses}", True, BLACK)
        scoreTies = myFont.render(f"Ties: {ties}", True, BLACK)

        # Check for input events
        for event in pygame.event.get():
            # Functionality for Player closing out of application entirely
            if event.type == pygame.QUIT:
                runGame = False
                pygame.quit()
                saveScores()

            # Mouse click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Functionality for Player clicking gric cells
                if (not playAgain):
                    playerMove(mouse, cellPos)

                    # Check win conditions after CPU move
                    winCheck(screen, screenHeight)  

                # Functionality for when BACK button pressed. Ends game loop and returns to main menu screen
                if ((tttButtons['BACK'][0] <= mouse[0] <= (tttButtons['BACK'][0] + 150)) and (tttButtons['BACK'][1] <= mouse[1] <= (tttButtons['BACK'][1] + 42)) and not playAgain):
                    runTTT = False
                    saveScores()
                # Functionality for when PLAY AGAIN button pressed. Resets game state and starts game again
                elif ((tttButtons['AGAIN'][0] <= mouse[0] <= (tttButtons['AGAIN'][0] + 140)) and (tttButtons['AGAIN'][1] <= mouse[1] <= (tttButtons['AGAIN'][1] + 42)) and playAgain):
                    playAgain = False
                    prompt = systemMessages['INITIAL']
                    resetGame(systemMessages["INITIAL"])
            
            
        # Fills screen with specific color
        screen.fill(DIMGREY)
        
        # Updates mouse cursor position and stores coordinates in a tuple
        mouse = pygame.mouse.get_pos()

        # Draws game grid
        drawGrid(screen, BLACK, screenWidth, screenHeight, WHITE, GREY, tttButtons, mouse)

        # CPU move if turn
        if (not playAgain and winner == None):
            cpuMove()

        # Check win conditions after CPU move
        winCheck(screen, screenHeight)
        
        
        # End game if win achieved
        if (not winner == None):
            playAgain = True

        # Display game end screen with PLAY AGAIN button
        if (playAgain):
            drawSystemMessages(screen, replay, 60, 150)
            drawButton(screen, WHITE, GREY, tttButtons['AGAIN'][0], tttButtons['AGAIN'][1], 150, 42, tttText['AGAIN'], 5, mouse)

        # Draws Prompt on screen
        drawSystemMessages(screen, prompt, 60, 100)

        # Draws Scoreboard on screen
        drawScore("TTT", screen, WHITE, 450, 20, 250, 130, scoreWins, scoreLosses, scoreTies, 10)

        # Draws BACK button on screen if game not completed
        if (not playAgain):
            drawButton(screen, WHITE, GREY, tttButtons['BACK'][0], tttButtons['BACK'][1], 140, 42, tttText['BACK'], 35, mouse)

        # Alters score values based on result of game
        if (incrementScore):
            if (winner == "Player"):
                prompt = systemMessages["VICTORY"]
                wins += 1
            elif (winner == "CPU"):
                prompt = systemMessages["LOSS"]
                losses += 1
            elif (winner == "tie"):
                prompt = systemMessages["TIE"]
                ties += 1

            incrementScore = False

        # Updates game frames
        pygame.display.update()