import pygame
import random
import json
import os
from guiUtilities import drawButton, drawSystemMessages, drawScore

wins = 0
losses = 0
ties = 0
prompt = ""
cpuResponse = ""

# Function for game implementation. CPU choice, prompt displays and Player VS CPU choice comparisons. Also alters score values based on results
def playGame(playerChoice, systemMessages, myFont):
    global prompt, wins, losses, ties, cpuResponse

    # CPU choice and resulting message
    cpuChoice = random.choice(["Rock", "Paper", "Scissors"])
    cpuResponse = myFont.render(f"CPU chose {cpuChoice}. Player chose {playerChoice}.", True, (255, 255, 255))

    # Player vs CPU choice comparisons
    if ((playerChoice == "Rock" and cpuChoice == "Scissors") or (playerChoice == "Paper" and cpuChoice == "Rock") or (playerChoice == "Scissors" and cpuChoice == "Paper")):
        prompt = systemMessages['VICTORY']
        wins += 1
    elif (playerChoice == cpuChoice):
        prompt = systemMessages['TIE']
        ties += 1
    else:
        prompt = systemMessages['LOSS']
        losses += 1

# Function to update gamelogs with score changes made during game
def saveScores():
    global wins, losses, ties
    
    try:
        with open('gamelogs.json', 'rt') as file:
            data = json.load(file)   

        data['RPS']['Wins'] = wins
        data['RPS']['Losses'] = losses
        data['RPS']['Ties'] = ties

        with open('gamelogs.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("This file doesn't exist.")

# Game function
def runRPS(screen, mouse, screenWidth, screenHeight, myFont):
    global prompt, wins, losses, ties, cpuResponse

    # Load scores from gamelogs file
    try:
        with open('gamelogs.json', 'rt') as file:
            data = json.load(file)

        wins = data['RPS']['Wins']
        losses = data['RPS']['Losses']
        ties = data['RPS']['Ties']
    except:
        print("This file doesn't exist.")

    # Sets window header
    pygame.display.set_caption("Rock, Paper, Scissors")

    # Game loop condition
    runRPS = True

    # Color, rpsText and Font Settings
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (192, 192, 192)
    DIMGREY = (105, 105, 105)

    # Game button positions
    rpsButtons = {
        "ROCK" : ((screenWidth / 2) - 270, (screenHeight / 2) + 300),
        "PAPER" : ((screenWidth / 2) - 70, (screenHeight / 2) + 300),
        "SCISSORS" : ((screenWidth / 2) + 130, (screenHeight / 2) + 300),
        "BACK" : ((screenWidth / 2) + 215, (screenHeight / 2) - 300),
        "AGAIN" : ((screenWidth / 2) - 70, (screenHeight / 2) + 200),
    }

    # Game button texts
    rpsText = {
        "ROCK" : myFont.render('Rock', True, BLACK),
        "PAPER" : myFont.render('Paper', True, BLACK),
        "SCISSORS" : myFont.render('Scissors', True, BLACK),
        "BACK" : myFont.render('Back', True, BLACK),
        "AGAIN" : myFont.render('Play again!', True, BLACK)
    }

    # Game messages
    systemMessages = {
        "INITIAL" : myFont.render("Let's play. Rock, Paper or Scissors?", True, WHITE),
        "VICTORY" : myFont.render("Player wins!", True, WHITE),
        "LOSS" : myFont.render("CPU wins!", True, WHITE),
        "TIE" : myFont.render("It's a tie!", True, WHITE),
        "AGAIN" : myFont.render("Would you like to play again?", True, WHITE)
    }
    
    # Initial prompt message
    prompt = systemMessages['INITIAL']

    # Replay message initialization
    replay = systemMessages['AGAIN']
    
    # Game end flag set to inactive
    playAgain = False

    # Game loop
    while runRPS:
        # Scores displayed on screen
        scoreWins = myFont.render(f"Wins: {wins}", True, BLACK)
        scoreLosses = myFont.render(f"Losses: {losses}", True, BLACK)
        scoreTies = myFont.render(f"Ties: {ties}", True, BLACK)

        # Input event functionality
        for event in pygame.event.get():
            # Functionality for if Player closes application
            if event.type == pygame.QUIT:
                runGame = False
                pygame.quit()
                saveScores()

            # Mouse click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse clicked ROCK button
                if ((rpsButtons['ROCK'][0] <= mouse[0] <= (rpsButtons['ROCK'][0] + 140)) and (rpsButtons['ROCK'][1] <= mouse[1] <= (rpsButtons['ROCK'][1] + 42))):
                    playGame("Rock", systemMessages, myFont)
                    playAgain = True
                    data['RPS']['Wins'] = wins
                # Checks if mouse clicked PAPER button
                elif ((rpsButtons['PAPER'][0] <= mouse[0] <= (rpsButtons['PAPER'][0] + 140)) and (rpsButtons['PAPER'][1] <= mouse[1] <= (rpsButtons['PAPER'][1] + 42))):
                    playGame("Paper", systemMessages, myFont)
                    playAgain = True
                # Checks if mouse clicked Scissors button
                elif ((rpsButtons['SCISSORS'][0] <= mouse[0] <= (rpsButtons['SCISSORS'][0] + 140)) and (rpsButtons['SCISSORS'][1] <= mouse[1] <= (rpsButtons['SCISSORS'][1] + 42))):
                    playGame("Scissors", systemMessages, myFont)
                    playAgain = True
                # Checks if mouse clicked BACK button
                elif ((rpsButtons['BACK'][0] <= mouse[0] <= (rpsButtons['BACK'][0] + 140)) and (rpsButtons['BACK'][1] <= mouse[1] <= (rpsButtons['BACK'][1] + 42))):
                    runRPS = False
                    saveScores()


        # Fills screen with specific color
        screen.fill(DIMGREY)
        
        # Updates mouse cursor position and stores coordinates in a tuple
        mouse = pygame.mouse.get_pos()

        # Display choice and BACK buttons
        if (not playAgain):
            # Draws ROCK button
            drawButton(screen, WHITE, GREY, rpsButtons['ROCK'][0], rpsButtons['ROCK'][1], 140, 42, rpsText['ROCK'], 35, mouse)

            # Draws PAPER button
            drawButton(screen, WHITE, GREY, rpsButtons['PAPER'][0], rpsButtons['PAPER'][1], 140, 42, rpsText['PAPER'], 32, mouse)

            # Draws SCISSORS button
            drawButton(screen, WHITE, GREY, rpsButtons['SCISSORS'][0], rpsButtons['SCISSORS'][1], 140, 42, rpsText['SCISSORS'], 15, mouse)

            # Draws BACK button
            drawButton(screen, WHITE, GREY, rpsButtons['BACK'][0], rpsButtons['BACK'][1], 140, 42, rpsText['BACK'], 35, mouse)
        # Display game end screen with PLAY AGAIN button and replay message
        else:
            drawSystemMessages(screen, cpuResponse, 100, 50)
            drawSystemMessages(screen, replay, 100, 150)
            drawButton(screen, WHITE, GREY, rpsButtons['AGAIN'][0], rpsButtons['AGAIN'][1], 150, 42, rpsText['AGAIN'], 5, mouse)

            # Functionality for if Player clicks PLAY AGAIN button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((rpsButtons['AGAIN'][0] <= mouse[0] <= (rpsButtons['AGAIN'][0] + 300)) and (rpsButtons['AGAIN'][1] <= mouse[1] <= (rpsButtons['AGAIN'][1] + 40))):
                    playAgain = False
                    prompt = systemMessages['INITIAL']

        # Prompts on screen
        drawSystemMessages(screen, prompt, 100, 100)

        # Scoreboard
        drawScore("RPS", screen, WHITE, 235, 250, 250, 130, scoreWins, scoreLosses, scoreTies, 10)

        # Updates game frames
        pygame.display.update()