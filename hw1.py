import time
import numpy as np
from gridgame import *

##############################################################################################################################

# You can visualize what your code is doing by setting the GUI argument in the following line to true.
# The render_delay_sec argument allows you to slow down the animation, to be able to see each step more clearly.

# For your final submission, please set the GUI option to False.

# The gs argument controls the grid size. You should experiment with various sizes to ensure your code generalizes.

##############################################################################################################################

setup(GUI = True, render_delay_sec = 0.1, gs = 10)


##############################################################################################################################

# Initialization

# shapePos is the current position of the brush.

# currentShapeIndex is the index of the current brush type being placed (order specified in gridgame.py, and assignment instructions).

# currentColorIndex is the index of the current color being placed (order specified in gridgame.py, and assignment instructions).

# grid represents the current state of the board. 
    
    # -1 indicates an empty cell
    # 0 indicates a cell colored in the first color (indigo by default)
    # 1 indicates a cell colored in the second color (taupe by default)
    # 2 indicates a cell colored in the third color (veridian by default)
    # 3 indicates a cell colored in the fourth color (peach by default)

# placedShapes is a list of shapes that have currently been placed on the board.
    
    # Each shape is represented as a list containing three elements: a) the brush type (number between 0-8), 
    # b) the location of the shape (coordinates of top-left cell of the shape) and c) color of the shape (number between 0-3)

    # For instance [0, (0,0), 2] represents a shape spanning a single cell in the color 2=veridian, placed at the top left cell in the grid.

# done is a Boolean that represents whether coloring constraints are satisfied. Updated by the gridgames.py file.

##############################################################################################################################

shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done = execute('export')
# input()   # <-- workaround to prevent PyGame window from closing after execute() is called, for when GUI set to True. Uncomment to enable.
print(shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done)

####################################################
# Timing your code's execution for the leaderboard.
####################################################

start = time.time()  # <- do not modify this.



##########################################
# Write all your code in the area below. 
##########################################



### GLOBALS

grid_size = len(grid)
gridSize = len(grid)
myShapeCounter = 0 # currentShapeIndex was not updating as expected for me
myColorCounter = 0 # currentColorIndex was not updating as expected for me
count = 100

### FUNCTIONS

# move() quantifies every cell within a shape, checks the shape conditions in a similar way to canPlace(), and moves the shape accordingly.  
def move(myShapeCounter):
    
    x,y = shapePos[0], shapePos[1]
    shapeWidth = len(shapes[myShapeCounter][0])
    shapeHeight = len(shapes[myShapeCounter])

    if x + shapeWidth < (grid_size): # If shape bounds are less than grid bounds
        execute('D') # Move one to the right
    if x + shapeWidth >= (grid_size):
        execute('S') # One down
        for i in range(grid_size):
                execute('A') # Reinitialize at [0, y]
    if (x + shapeWidth) >= (grid_size) and (y + shapeHeight) >= (grid_size):
        for i in range(grid_size):
            execute('A')
            execute('W') # go back up to grid[0,0]
    
            

# notNeighboringColors() checks through all adjacent cells to a shape and appends the adjacent_colors array if that color exists. available_colors are the remaining 
# colors not within the adjacent_colors array. This function draws inspiration from getAvailableColor() in gridgame.py that establishes the randomly placed colored cells
# at grid initialization.
def notNeighboringColors(grid, shapes, shapePos):
    adjacent_colors = set()
    for i, row in enumerate(shapes):
        for j, cells in enumerate(row):
            if cells:
                x, y = shapePos[0]+ j, shapePos[1] + i

                if x > 0:
                    adjacent_colors.add(grid[y, x - 1])
                if x < (grid_size - 1):
                    adjacent_colors.add(grid[y, x + 1])
                if y > 0:
                    adjacent_colors.add(grid[y - 1, x])
                if y < (grid_size - 1):
                    adjacent_colors.add(grid[y + 1, x])

    available_colors = [i for i in range(len(colors)) if i not in adjacent_colors]

    #print (f"available colors =", available_colors)

    return available_colors

def checkGrid(grid):
    # Ensure all cells are filled
    if -1 in grid:
        return False

    # Check that no adjacent cells have the same color
    for i in range(gridSize):
        for j in range(gridSize):
            color = grid[i, j]
            if i > 0 and grid[i - 1, j] == color:
                return False
            if i < gridSize - 1 and grid[i + 1, j] == color:
                return False
            if j > 0 and grid[i, j - 1] == color:
                return False
            if j < gridSize - 1 and grid[i, j + 1] == color:
                return False

    return True
  
    
### EXECUTABLE


while not done:

    if count > 30:
        while myShapeCounter != 3: # Base case: Start iterating with the largest shape first. 
            execute('H')
            myShapeCounter = (myShapeCounter + 1) % len(shapes)
    elif count > 15:
        while myShapeCounter != 1: # Base case: Start iterating with the largest shape first. 
            execute('H')
            myShapeCounter = (myShapeCounter + 1) % len(shapes)
    else:
        while myShapeCounter != 0: # Base case: Start iterating with the largest shape first. 
            execute('H')
            myShapeCounter = (myShapeCounter + 1) % len(shapes)

    while myColorCounter != 0: # Base case: Start iterating with first color. 
        execute('K')
        myColorCounter = (myColorCounter + 1) % len(colors)

    while grid[shapePos[1], shapePos[0]] > -1: # If the source cell of the shape is filled
        move(myShapeCounter)

    while not canPlace(grid, shapes[myShapeCounter], shapePos): # Change shape until one physicially fits
        execute('H')
        myShapeCounter = (myShapeCounter + 1) % len(shapes)

        while grid[shapePos[1], shapePos[0]] > -1: # If the source cell of the shape is filled
            move(myShapeCounter)

    while myColorCounter not in notNeighboringColors(grid, shapes[myShapeCounter], shapePos): # Change color until one does not conflict neighboring colors 
        execute('K')
        myColorCounter = (myColorCounter + 1) % len(colors)

    execute('P') # Arrive here if shape fits and colors don't conflict
    count = np.count_nonzero(grid == -1)
    print(count)

    if checkGrid(grid) == True:
        execute('export')
        break  




########################################

# Do not modify any of the code below. 

########################################

end=time.time()

np.savetxt('grid.txt', grid, fmt="%d")
with open("shapes.txt", "w") as outfile:
    outfile.write(str(placedShapes))
with open("time.txt", "w") as outfile:
    outfile.write(str(end-start))
