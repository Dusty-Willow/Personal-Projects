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
state = ""
winner = None

pygame.init()
myBoard = [["IGNORE"]*3, ["IGNORE"]*3, ["IGNORE"]*3]
cpuMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xoFont = pygame.font.SysFont('arial', 80)


def playerMove(mouse, cellPositions):
    global state, myBoard, cpuMoves, playerMoves
    
    if (state == "player"):
        if ((cellPositions['TOPLEFT'][0] <= mouse[0] <= (cellPositions['TOPLEFT'][0] + 90)) and (cellPositions['TOPLEFT'][1] <= mouse[1] <= (cellPositions['TOPLEFT'][1] + 90)) and myBoard[0][0] == "IGNORE"):
            placeXO("X", 0, 0)
            cpuMoves.remove(1)
            playerMoves.remove(1)
        elif ((cellPositions['TOPMID'][0] <= mouse[0] <= (cellPositions['TOPMID'][0] + 90)) and (cellPositions['TOPMID'][1] <= mouse[1] <= (cellPositions['TOPMID'][1] + 90)) and myBoard[1][0] == "IGNORE"):
            placeXO("X", 0, 1)
            cpuMoves.remove(2)
            playerMoves.remove(2)
        elif ((cellPositions['TOPRIGHT'][0] <= mouse[0] <= (cellPositions['TOPRIGHT'][0] + 90)) and (cellPositions['TOPRIGHT'][1] <= mouse[1] <= (cellPositions['TOPRIGHT'][1] + 90)) and myBoard[2][0] == "IGNORE"):
            placeXO("X", 0, 2)
            cpuMoves.remove(3)
            playerMoves.remove(3)
        elif ((cellPositions['MIDLEFT'][0] <= mouse[0] <= (cellPositions['MIDLEFT'][0] + 90)) and (cellPositions['MIDLEFT'][1] <= mouse[1] <= (cellPositions['MIDLEFT'][1] + 90)) and myBoard[0][1] == "IGNORE"):
            placeXO("X", 1, 0)
            cpuMoves.remove(4)
            playerMoves.remove(4)
        elif ((cellPositions['MIDMID'][0] <= mouse[0] <= (cellPositions['MIDMID'][0] + 90)) and (cellPositions['MIDMID'][1] <= mouse[1] <= (cellPositions['MIDMID'][1] + 90)) and myBoard[1][1] == "IGNORE"):
            placeXO("X", 1, 1)
            cpuMoves.remove(5)
            playerMoves.remove(5)
        elif ((cellPositions['MIDRIGHT'][0] <= mouse[0] <= (cellPositions['MIDRIGHT'][0] + 90)) and (cellPositions['MIDRIGHT'][1] <= mouse[1] <= (cellPositions['MIDRIGHT'][1] + 90)) and myBoard[2][2] == "IGNORE"):
            placeXO("X", 1, 2)
            cpuMoves.remove(6)
            playerMoves.remove(6)
        elif ((cellPositions['BOTLEFT'][0] <= mouse[0] <= (cellPositions['BOTLEFT'][0] + 90)) and (cellPositions['BOTLEFT'][1] <= mouse[1] <= (cellPositions['BOTLEFT'][1] + 90)) and myBoard[0][2] == "IGNORE"):
            placeXO("X", 2, 0)
            cpuMoves.remove(7)
            playerMoves.remove(7)
        elif ((cellPositions['BOTMID'][0] <= mouse[0] <= (cellPositions['BOTMID'][0] + 90)) and (cellPositions['BOTMID'][1] <= mouse[1] <= (cellPositions['BOTMID'][1] + 90)) and myBoard[1][2] == "IGNORE"):
            placeXO("X", 2, 1)
            cpuMoves.remove(8)
            playerMoves.remove(8)
        elif ((cellPositions['BOTRIGHT'][0] <= mouse[0] <= (cellPositions['BOTRIGHT'][0] + 90)) and (cellPositions['BOTRIGHT'][1] <= mouse[1] <= (cellPositions['BOTRIGHT'][1] + 90)) and myBoard[2][2] == "IGNORE"):
            placeXO("X", 2, 2)
            cpuMoves.remove(9)
            playerMoves.remove(9)

    print(myBoard)
    state = "cpu"

def cpuMove(mouse, cellPositions):
    global state, cpuMoves
    time.sleep(2)
    cpuChoice = random.choice(cpuMoves)

    if (state == "cpu"):
        match cpuChoice:
            case 1:
                placeXO("O", 0, 0)
                cpuMoves.remove(1)
                playerMoves.remove(1)
            case 2:
                placeXO("O", 1, 0)
                cpuMoves.remove(2)
                playerMoves.remove(2)
            case 3:
                placeXO("O", 2, 0)
                cpuMoves.remove(3)
                playerMoves.remove(3)
            case 4:
                placeXO("O", 0, 1)
                cpuMoves.remove(4)
                playerMoves.remove(4)
            case 5:
                placeXO("O", 1, 1)
                cpuMoves.remove(5)
                playerMoves.remove(5)
            case 6:
                placeXO("O", 2, 1)
                cpuMoves.remove(6)
                playerMoves.remove(6)
            case 7:
                placeXO("O", 0, 2)
                cpuMoves.remove(7)
                playerMoves.remove(7)
            case 8:
                placeXO("O", 1, 2)
                cpuMoves.remove(8)
                playerMoves.remove(8)
            case 9:
                placeXO("O", 2, 2)
                cpuMoves.remove(9)
                playerMoves.remove(9)
    
    state = "player"

def winCheck(screen, cellPos):
    global myBoard, winner
    temp = None
    # Check Row Victory
    for row in range(0, 3):
        if((myBoard[row][0] == myBoard[row][1] == myBoard[row][2]) and not (myBoard[row][0] == "IGNORE")):
            winner = myBoard[row][0]
            temp = row
    
    if (not (winner == None)):
        match temp:
            case 0:
                pygame.draw.line(screen, (0, 0, 0), cellPos['TOPLEFT'], cellPos['TOPRIGHT'])
            case 1:
                pygame.draw.line(screen, (0, 0, 0), cellPos['MIDLEFT'], cellPos['MIDRIGHT'])
            case 2:
                pygame.draw.line(screen, (0, 0, 0), cellPos['BOTLEFT'], cellPos['BOTRIGHT'])
    
    # Check Column Victory
    for col in range(0, 3):
        if((myBoard[0][col] == myBoard[1][col] == myBoard[2][col]) and not (myBoard[0][col] == "IGNORE")):
            winner = myBoard[0][col]
            temp = row
    
    if (not winner == None):
        match temp:
            case 0:
                pygame.draw.line(screen, (0, 0, 0), cellPos['TOPLEFT'], cellPos['BOTLEFT'])
            case 1:
                pygame.draw.line(screen, (0, 0, 0), cellPos['TOPMID'], cellPos['BOTMID'])
            case 2:
                pygame.draw.line(screen, (0, 0, 0), cellPos['TOPRIGHT'], cellPos['BOTRIGHT'])



def placeXO(XO, boardRow, boardCol):
    global myBoard

    myBoard[boardCol][boardRow] = xoFont.render(XO, True, (0,0,0))

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
    drawButton(screen, cellColor, cellHover, 120, screenHeight / 3, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[0][0], 22, mouse)
    drawButton(screen, cellColor, cellHover, 120, screenHeight / 3 + 150, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[0][1], 22, mouse)
    drawButton(screen, cellColor, cellHover, 120, screenHeight / 3 + 300, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[0][2], 22, mouse)
    drawButton(screen, cellColor, cellHover, 320, screenHeight / 3, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[1][0], 22, mouse)
    drawButton(screen, cellColor, cellHover, 320, screenHeight / 3 + 150, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[1][1], 22, mouse)
    drawButton(screen, cellColor, cellHover, 320, screenHeight / 3 + 300, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[1][2], 22, mouse)
    drawButton(screen, cellColor, cellHover, 500, screenHeight / 3, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[2][0], 22, mouse)
    drawButton(screen, cellColor, cellHover, 500, screenHeight / 3 + 150, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[2][1], 22, mouse)
    drawButton(screen, cellColor, cellHover, 500, screenHeight / 3 + 300, buttons['GRIDCELL'][0], buttons['GRIDCELL'][1], myBoard[2][2], 22, mouse)

def runTTT(screen, mouse, screenWidth, screenHeight, myFont):
    runTTT = True

    print(myBoard)

    global prompt, wins, losses, ties, state

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
        "BACK" : ((screenWidth / 2) + 215, (screenHeight / 2) - 300),
        "AGAIN" : ((screenWidth / 2) - 70, (screenHeight / 2) + 200),
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
                state = "player"
                playerMove(mouse, cellPos)

        # Fills screen with specific color
        screen.fill(DIMGREY)
        
        # Updates mouse cursor position and stores coordinates in a tuple
        mouse = pygame.mouse.get_pos()

        if (not playAgain):
            drawGrid(screen, BLACK, screenWidth, screenHeight, WHITE, GREY, tttButtons, mouse)
        else:
            drawSystemMessages(screen, replay, 100, 150)
            drawButton(screen, WHITE, GREY, tttButtons['AGAIN'][0], tttButtons['AGAIN'][1], 150, 42, tttText['AGAIN'], 5, mouse)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((tttButtons['AGAIN'][0] <= mouse[0] <= (tttButtons['AGAIN'][0] + 300)) and (tttButtons['AGAIN'][1] <= mouse[1] <= (tttButtons['AGAIN'][1] + 40))):
                    playAgain = False
                    prompt = systemMessages['INITIAL']

        # Check win conditions
        winCheck(screen, cellPos)

        # Prompts on screen
        drawSystemMessages(screen, prompt, 60, 100)

        # Scoreboard
        drawScore("TTT", screen, WHITE, 450, 70, 250, 130, scoreWins, scoreLosses, scoreTies, 10)


        # Updates game frames
        pygame.display.update()



