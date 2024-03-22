import random
import os

# Define constants for the grid size and screen dimensions
WIDTH = 5
HEIGHT = 5
CELL_SIZE = 20  # Adjust for desired screen size
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

# Define snake and food positions
snake = [(2, 2)]  # Starting position for the snake head
food_x, food_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)

# Define directions
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Initialize direction (avoid starting with the opposite direction)
direction = random.choice([RIGHT, DOWN])
moving = True  # Flag to track game state

def clear_screen():
  """Clears the terminal screen for a fresh display."""
  os.system('cls' if os.name == 'nt' else 'clear')  # Clear for Windows or Linux/macOS

def draw_grid():
  """Draws the grid using plus signs at cell boundaries."""
  for y in range(HEIGHT + 1):
    for x in range(WIDTH + 1):
      print("+", end="")
    print()

def draw_snake():
  """Draws the snake body using 'S' for the head and 'o' for the body."""
  head_x, head_y = snake[0]
  print("S", end="")
  for x, y in snake[1:]:
    print("o", end="")
  print()

def draw_food():
  """Draws the food at its current position using 'F'."""
  x, y = food_x, food_y
  print("F", end="")
  for _ in range(WIDTH - 1):
    print(" ", end="")
  print()

def draw_all():
  """Clears the screen and draws all game elements (grid, snake, and food)."""
  clear_screen()
  draw_grid()
  draw_snake()
  draw_food()

def game_over():
  """Prints a game over message and sets the moving flag to False."""
  print("Game Over!")
  global moving
  moving = False

def check_collision():
  """Checks for collisions with walls or the snake's own body."""
  head_x, head_y = snake[0]
  if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
    game_over()
  for x, y in snake[1:]:  # Check for collision with snake body
    if head_x == x and head_y == y:
      game_over()

def get_user_input():
  """Gets user input for direction change and returns the new direction."""
  key = input("Enter a direction (w, a, s, d): ")
  new_direction = None
  if key.lower() == 'w' and direction != DOWN:
    new_direction = UP
  elif key.lower() == 'a' and direction != RIGHT:
    new_direction = LEFT
  elif key.lower() == 's' and direction != UP:
    new_direction = DOWN
  elif key.lower() == 'd' and direction != LEFT:
    new_direction = RIGHT
  return new_direction

def update_snake():
  """Updates the snake position based on the current direction."""
  global snake, food_x, food_y
  head_x, head_y = snake[0]
  new_x = head_x + direction[0]
  new_y = head_y + direction[1]
  snake.insert(0, (new_x, new_y))  # Add new head
  if new_x == food_x and new_y == food_y:  # Check if food is eaten
    food_x, food_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
  else:
    snake.pop()  # Remove tail if food not eaten (keeps snake length constant)

def main():
  """Main game loop that handles drawing, updates, and user input."""
  while moving:
    draw_all()
    new_direction = get_user_input()  # Get user input and store in new_direction
    # Rest of the code using new_direction...

main()