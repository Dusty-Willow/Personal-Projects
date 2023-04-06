import pygame

def drawButton(surface, basecolor, hovercolor, xOffset, yOffset, buttonWidth, buttonHeight, text, textOffset, mouse):
    # Draws button based on whether mouse is hovering over it or not
    if (xOffset <= mouse[0] <= (xOffset + buttonWidth) and yOffset <= mouse[1] <= (yOffset + buttonHeight)):
        pygame.draw.rect(surface, hovercolor, [xOffset, yOffset, buttonWidth, buttonHeight])
    else:
        pygame.draw.rect(surface, basecolor, [xOffset, yOffset, buttonWidth, buttonHeight])
    # Puts text on buttons
    surface.blit(text, ((xOffset + textOffset), yOffset))

def drawScore(game, surface, basecolor, xOffset, yOffset, boardWidth, boardHeight, text1, text2, text3, textOffset):
    # Draws score for specific game
    pygame.draw.rect(surface, basecolor, [xOffset, yOffset, boardWidth, boardHeight])
    surface.blit(text1, ((xOffset + textOffset + 70), yOffset))
    surface.blit(text2, ((xOffset + textOffset + 55), yOffset + 40))
    surface.blit(text3, ((xOffset + textOffset + 78), yOffset + 80))


def drawSystemMessages(surface, text, xOffset, yOffset):
    # Draws system messages on screen
    surface.blit(text, (xOffset, yOffset))

