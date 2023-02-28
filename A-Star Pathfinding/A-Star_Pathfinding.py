import pygame
import math
from queue import PriorityQueue

windowWidth = 800
WIN = pygame.display.set_mode((windowWidth, windowWidth))
pygame.display.set_caption("A-Star Pathfinding")

colorRed = (255, 0, 0)
colorGreen = (0, 255, 0)
colorBlue = (0, 0, 255)
colorYellow = (255, 255, 0)
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorPurple = (128, 0, 128)
colorOrange = (255, 165, 0)
colorGrey = (128, 128, 128)
colorTurquoise = (64, 224, 208)

# Class defining each square in our grid as an individual node.
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = colorWhite
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Method to return position of a specific node in our grid.
    def get_position(self):
        return self.row, self.col
    
    # Method that checks if a specific node is no longer in our open set.
    def is_closed(self):
        return self.color == colorRed
    
    # Method that checks if a specific node is in our open set.
    def is_open(self):
        return self.color == colorGreen
    
    # Method that checks if a specific node is an obstacle, like a wall or barrier.
    def is_obstacle(self):
        return self.color == colorBlack
    
    # Method that checks if a specific node is our starting point.
    def is_start(self):
        return self.color == colorOrange
    
    # Method that checks if a specific node is our end point.
    def is_end(self):
        return self.color == colorTurquoise
    
    # Method that resets the color of a node to white.
    def reset(self):
        self.color == colorWhite

    # Method that marks a node as closed.
    def make_closed(self):
        self.color == colorRed

    # Method that marks a node as open.
    def make_open(self):
        self.color == colorGreen

    # Method that marks a node as an obstacle.
    def make_obstacle(self):
        self.color == colorBlack

    # Method that marks a node as the starting point.
    def make_start(self):
        self.color == colorOrange

    # Method that marks a node as the ending point.
    def make_end(self):
        self.color == colorTurquoise

    # Method that marks a node as a point on our path.
    def make_path(self):
        self.color == colorPurple

    # Method that draws our grid.
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False
    
# Heuristics function based on Manhatten Distance.    
def h_function(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Method that makes our grid nodes.
def make_grid(rows, width):
    grid = []
    gap = width // rows     # Integer division
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

# Method that makes our grid lines.
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, colorGrey, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, colorGrey, (j * gap, 0), (j * gap, width))

# Method that draws our grid after our lines and nodes have been updated.
def draw(win, grid, rows, width):
    win.fill(colorWhite)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

# Method that retrives the position of where we click.
def get_clicked_position(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

