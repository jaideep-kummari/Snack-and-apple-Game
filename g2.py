import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake and Apple Game')

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue=(0,0,255)

# Snake settings
snake_block = 10
snake_speed = 12
clock = pygame.time.Clock()

# Font settings
font_style = pygame.font.SysFont(None, 35)

# Score function
def score_display(score):
    value = font_style.render(f"Your Score: {score}", True,red)
    window.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], snake_block, snake_block])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Random apple coordinates
    apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:
        while game_close:
            window.fill(black)
            message = font_style.render("Game Over! Press 'C' to Play Again or 'Q' to Quit", True, blue)
            window.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        # Draw apple
        pygame.draw.rect(window, red, [apple_x, apple_y, snake_block, snake_block])

        # Update the snake's position
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Draw the snake
        draw_snake(snake_block, snake_list)

        # Display score
        score_display(score)

        pygame.display.update()

        # Check if snake eats the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
