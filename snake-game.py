import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

# Set the clock
clock = pygame.time.Clock()

# Set the font
font = pygame.font.Font(None, 36)

# Set the initial position and direction of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction

# Set the initial position of the food
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Set the initial score
score = 0


# Function to display text on the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)


# Function to reset the game
def reset_game():
    global snake_position, snake_body, direction, change_to, food_position, food_spawn, score
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = "RIGHT"
    change_to = direction
    food_position = [random.randrange(1, (width // 10)) * 10,
                     random.randrange(1, (height // 10)) * 10]
    food_spawn = True
    score = 0


# Game loop
running = True
game_over = False
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_over:
                game_over = False
                reset_game()
            if not game_over:
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    change_to = "RIGHT"
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    change_to = "LEFT"
                if event.key == pygame.K_UP or event.key == ord("w"):
                    change_to = "UP"
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    change_to = "DOWN"

    # Validate direction
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # Move the snake
    if not game_over:
        if direction == "RIGHT":
            snake_position[0] += 10
        if direction == "LEFT":
            snake_position[0] -= 10
        if direction == "UP":
            snake_position[1] -= 10
        if direction == "DOWN":
            snake_position[1] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Respawn food
        if not food_spawn:
            food_position = [random.randrange(1, (width // 10)) * 10,
                             random.randrange(1, (height // 10)) * 10]
            food_spawn = True

        # Game over conditions
        if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
            game_over = True
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over = True

    # Background
    window.fill(black)

    if game_over:
        # Display game over text and play again button
        display_text("Game Over!", red, width // 2, height // 2 - 50)
        display_text("Press Enter to Play Again", white, width // 2, height // 2 + 50)
    else:
        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw food
        pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Scoreboard
    display_text(f"Score: {score}", blue, 70, 15)

    # Refresh the game screen
    pygame.display.flip()

    # Set the frames per second
    clock.tick(15)

# Quit the game
pygame.quit()
