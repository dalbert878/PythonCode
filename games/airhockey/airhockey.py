import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 50
BALL_SIZE = 20
WHITE = (255, 255, 255)
FONT_COLOR = (255, 255, 0)
FONT_SIZE = 48

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Hockey")

# Paddle and Ball Positions
player1_pos = [20, HEIGHT // 2 - PADDLE_HEIGHT // 2]
player2_pos = [WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2]
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]

# Scores
player1_score = 0
player2_score = 0

# Font for displaying text
font = pygame.font.SysFont(None, FONT_SIZE)

def display_winner(winner):
    """Display the winner message on the screen."""
    text = font.render(f"Player {winner} Wins!", True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before restarting

# Game Loop
running = True
while running:
    pygame.time.delay(30)  # Control frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= 5  # Move Player 1 paddle up
    if keys[pygame.K_s] and player1_pos[1] < HEIGHT - PADDLE_HEIGHT:
        player1_pos[1] += 5  # Move Player 1 paddle down
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= 5  # Move Player 2 paddle up
    if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - PADDLE_HEIGHT:
        player2_pos[1] += 5  # Move Player 2 paddle down

    # Ball Movement
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball Collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
        ball_vel[1] = -ball_vel[1]  # Reverse vertical direction

    # Ball Collision with paddles
    if (ball_pos[0] <= player1_pos[0] + PADDLE_WIDTH and
        player1_pos[1] <= ball_pos[1] <= player1_pos[1] + PADDLE_HEIGHT):
        ball_vel[0] = -ball_vel[0]  # Reverse horizontal direction

    if (ball_pos[0] >= player2_pos[0] - BALL_SIZE and
        player2_pos[1] <= ball_pos[1] <= player2_pos[1] + PADDLE_HEIGHT):
        ball_vel[0] = -ball_vel[0]  # Reverse horizontal direction

    # Check for scoring
    if ball_pos[0] < 0:  # Player 2 scores
        player2_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]  # Reset ball position
        ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]  # Reset ball velocity

    if ball_pos[0] > WIDTH:  # Player 1 scores
        player1_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]  # Reset ball position
        ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]  # Reset ball velocity

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (*player1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (*player2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (*ball_pos, BALL_SIZE, BALL_SIZE))

    # Display scores
    score_text = font.render(f"{player1_score} : {player2_score}", True, FONT_COLOR)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Check for winner
    if player1_score == 1:
        display_winner(1)
        player1_score = 0
        player2_score = 0  # Reset scores for a new game
    elif player2_score == 1:
        display_winner(2)
        player1_score = 0
        player2_score = 0  # Reset scores for a new game

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
