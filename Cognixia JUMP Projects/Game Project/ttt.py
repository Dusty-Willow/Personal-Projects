import pygame
import random
import json
import time
import os
from guiUtilities import drawButton, drawSystemMessages, drawScore

wins = 0
losses = 0
ties = 0
prompt = ""
gameWon = False
state = "player"
winner = None
winAchieved = None

pygame.init()
dummyBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
myBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
cpuMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xoFont = pygame.font.SysFont('arial', 80)


def playerMove(mouse, cellPositions):
    global state, myBoard, cpuMoves, playerMoves
    
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

def cpuMove():
    global state, cpuMoves
    # time.sleep(2)
    cpuChoice = random.choice(cpuMoves)

    if (state == "cpu"):
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

def winCheck(screen, screenWidth, screenHeight):
    global dummyBoard, winner, winAchieved
    RED = (255, 0, 0)

    # Check Row Victory
    for row in range(0, 9, 3):
        if((dummyBoard[row] == dummyBoard[row + 1] == dummyBoard[row + 2]) and not (dummyBoard[row] == "IGNORE")):

            if (dummyBoard[row] == "X"):
                winner = "Player"
            elif (dummyBoard[row] == "O"):
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

            if (dummyBoard[col] == "X"):
                winner = "Player"
            elif (dummyBoard[col] == "O"):
                winner = "CPU"

            match col:
                case 0:
                    pygame.draw.line(screen, RED, (120 + 45, screenHeight / 3 - 50), (120 + 45, screenHeight / 3 + 300 + 140), 7)
                case 1:
                    pygame.draw.line(screen, RED, (120 + 45 + 200, screenHeight / 3 - 50), (120 + 45 + 200, screenHeight / 3 + 300 + 140), 7)
                case 2:
                    pygame.draw.line(screen, RED, (120 + 45 + 380, screenHeight / 3 - 50), (120 + 45 + 380, screenHeight / 3 + 300 + 140), 7)        

        if((dummyBoard[0] == dummyBoard[4] == dummyBoard[8]) and not (dummyBoard[0] == "IGNORE")):
            
            if (dummyBoard[0] == "X"):
                winner = "Player"
            elif (dummyBoard[0] == "O"):
                winner = "CPU"

            pygame.draw.line(screen, RED, (120 - 35, screenHeight / 3 - 30), (120 + 30 + 380 + 95, screenHeight / 3 + 300 + 110), 7)        
    
        if((dummyBoard[2] == dummyBoard[4] == dummyBoard[6]) and not (dummyBoard[2] == "IGNORE")):
            
            if (dummyBoard[2] == "X"):
                winner = "Player"
            elif (dummyBoard[2] == "O"):
                winner = "CPU"

            pygame.draw.line(screen, RED, (120 + 470 + 35, screenHeight / 3 - 30), (120 - 35, screenHeight / 3 + 300 + 110), 7)        

def movesLeft():
    if (bool(cpuMoves) == False and bool(playerMoves) == False and winner == None):
        winner = "tie"

def resetGame():
    dummyBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
    myBoard = ["IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE", "IGNORE"]
    cpuMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    playerMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def placeXO(XO, position):
    global myBoard, dummyBoard

    dummyBoard[position] = XO
    myBoard[position] = xoFont.render(XO, True, (0,0,0))

def saveScores():
    global wins, losses, ties
    
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

def alterPrompt(gameState, systemMessage):
    global prompt

    if (not gameWon):
        match gameState:
            case "playerTurn":
                prompt = systemMessage['PLAYERTURN']
            case "cpuTurn":
                prompt = systemMessage['CPUTURN']
            case "playerWon":
                prompt = systemMessage['VICTORY']
            case "cpuWon":
                prompt = systemMessage['LOSS']
            case "gameTie":
                prompt = systemMessage['TIE']

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

def runTTT(screen, mouse, screenWidth, screenHeight, myFont):
    runTTT = True
    global prompt, wins, losses, ties, state, winner

    # Load data regarding wins, losses and ties from gamelogs file
    try:
        with open('gamelogs.json', 'rt') as file:
            data = json.load(file)

        wins = data['TTT']['Wins']
        losses = data['TTT']['Losses']
        ties = data['TTT']['Ties']
    except:
        print("This file doesn't exist.")


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (192, 192, 192)
    DIMGREY = (105, 105, 105)

    tttButtons = {
        "BACK" : (10, 20),
        "AGAIN" : ((screenWidth / 2) - 130, 40),
        "GRIDCELL" : (90, 90),
    }

    tttText = {
        "BACK" : myFont.render('Back', True, BLACK),
        "AGAIN" : myFont.render('Play again!', True, BLACK)
    }

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


    systemMessages = {
        "INITIAL" : myFont.render("Let's play Tic Tac Toe.", True, WHITE),
        "PLAYERTURN" : myFont.render("Player turn. Waiting for decisions.", True, WHITE),
        "CPUTURN" : myFont.render("CPU turn. Making decision.", True, WHITE),
        "VICTORY" : myFont.render("Player wins!", True, WHITE),
        "LOSS" : myFont.render("CPU wins!", True, WHITE),
        "TIE" : myFont.render("It's a tie!", True, WHITE),
        "AGAIN" : myFont.render("Would you like to play again?", True, WHITE)
    }

    prompt = systemMessages['INITIAL']
    replay = systemMessages['AGAIN']
    
    playAgain = False

    while runTTT:
        scoreWins = myFont.render(f"Wins: {wins}", True, BLACK)
        scoreLosses = myFont.render(f"Losses: {losses}", True, BLACK)
        scoreTies = myFont.render(f"Ties: {ties}", True, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
                pygame.quit()
                saveScores()

            # Mouse click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse clicked ROCK button
                if (not playAgain):
                    playerMove(mouse, cellPos)
                    
                if ((tttButtons['BACK'][0] <= mouse[0] <= (tttButtons['BACK'][0] + 300)) and (tttButtons['BACK'][1] <= mouse[1] <= (tttButtons['BACK'][1] + 40))):
                    runTTT = False
                    saveScores()
                if ((tttButtons['AGAIN'][0] <= mouse[0] <= (tttButtons['AGAIN'][0] + 140)) and (tttButtons['AGAIN'][1] <= mouse[1] <= (tttButtons['AGAIN'][1] + 42))):
                    playAgain = False
                    prompt = systemMessages['INITIAL']
                    resetGame()

        # Fills screen with specific color
        screen.fill(DIMGREY)
        
        # Updates mouse cursor position and stores coordinates in a tuple
        mouse = pygame.mouse.get_pos()

        drawGrid(screen, BLACK, screenWidth, screenHeight, WHITE, GREY, tttButtons, mouse)

        if (playAgain):
            drawSystemMessages(screen, replay, 60, 150)
            drawButton(screen, WHITE, GREY, tttButtons['AGAIN'][0], tttButtons['AGAIN'][1], 150, 42, tttText['AGAIN'], 5, mouse)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((tttButtons['AGAIN'][0] <= mouse[0] <= (tttButtons['AGAIN'][0] + 300)) and (tttButtons['AGAIN'][1] <= mouse[1] <= (tttButtons['AGAIN'][1] + 40))):
                    playAgain = False
                    prompt = systemMessages['INITIAL']


        # CPU move if turn
        if (not playAgain and winner == None):
            cpuMove()
        
        # Check win conditions after cpu move
        winCheck(screen, screenWidth, screenHeight)

        # End game if win achieved
        if (not winner == None):
            playAgain = True

        # Prompts on screen
        drawSystemMessages(screen, prompt, 60, 100)

        # Scoreboard
        drawScore("TTT", screen, WHITE, 450, 20, 250, 130, scoreWins, scoreLosses, scoreTies, 10)

        # Draws BACK button
        drawButton(screen, WHITE, GREY, tttButtons['BACK'][0], tttButtons['BACK'][1], 140, 42, tttText['BACK'], 35, mouse)

        movesLeft()

        if (winner == "player"):
            wins += 1
        elif (winner == "cpu"):
            losses += 1
        elif (winner == "tie"):
            ties += 1

        # Updates game frames
        pygame.display.update()



