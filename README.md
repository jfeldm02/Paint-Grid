# Paint-Grid
Given an n x n grid, and eight different tetris shapes each with four different color options, the algorithm solves the game using the fewest shapes while avoiding color matching of adjacent shapes.   

# Overview
You are given a PyGame environment (in the gridgame.py file) that renders a randomly initialized n × n grid, with some cells pre-filled with one of four colors. Your goal is to build an AI agent that solves a coloring problem over this grid (see next page for constraints), such that no two cells that share an edge have the same color. Your agent will attempt to fill the environment by moving a virtual ‘brush’ over this grid and placing colored shapes, where the shape of the brush can be cycled through the following choices (numbered 0-8):
<img width="442" alt="Screenshot 2025-01-06 at 6 38 24 PM" src="https://github.com/user-attachments/assets/bb477591-3f8a-4406-9d25-f5c821c815b5" />

Additionally, each brush can be cycled through one of four colors (numbered 0-3):
<img width="500" alt="Screenshot 2025-01-06 at 6 41 28 PM" src="https://github.com/user-attachments/assets/3d47c3de-cdbc-4dc4-a380-135aca1ec0ec" />

# Agent Interaction with the Environment

Your agent must interact with the environment using the `execute()` function, which is called from within the `hw1.py` file. The function supports the following argument options (passed as strings):

### Argument Options:
- **`export`**:  
  Returns:
  1. The current state of the grid.
  2. A list of shapes with positions and colors currently placed on the grid.
  3. A Boolean indicating whether the coloring constraints have been satisfied.

- **`up` / `down` / `left` / `right`**:  
  Move the brush in the specified direction by one cell.  
  *Note*: The brush starts in the top-left corner of the grid when the program is executed.

- **`place`**:  
  Place a shape on the grid by coloring the cells covered by the brush in the currently selected brush color.

- **`switchshape`**:  
  Cycle to the next brush shape option.

- **`switchcolor`**:  
  Cycle to the next brush color option.

- **`undo`**:  
  Undo the last placed shape.

### Function Return Values:
Running the `execute()` function with any argument returns the following six items:
<img width="788" alt="Screenshot 2025-01-06 at 6 41 46 PM" src="https://github.com/user-attachments/assets/41040360-1a4f-49c0-b040-be476b07560b" />

# Environment Rules: 
Adjacent cells are defined as cells that share an edge between them (i.e., diagonally neighboring cells may share the same color, since they only share a vertex). If a brush partially or fully overlaps with an area of the grid that is already colored, the execute function with the place argument will fail, i.e. the colors in those cells will not be overwritten.
