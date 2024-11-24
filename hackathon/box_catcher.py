import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Box Catcher')

# Set up game variables
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

box_width = 50
box_height = 50
box_speed = 3
boxes = []

score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()  # Create clock object for controlling FPS
while running:
    screen.fill((0, 0, 0))  # Clear screen
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    
    # Create new boxes with a random spawn chance
    if random.random() < 0.02:  # Chance of box spawning
        box_x = random.randint(0, screen_width - box_width)
        boxes.append([box_x, 0])  # Box starts at top
    
    # Move boxes and handle collisions
    remaining_boxes = []
    for box in boxes:
        box[1] += box_speed  # Move box downwards
        if box[1] > screen_height:
            continue  # Skip the box if it falls off the screen
        
        # Check for collision with player
        if (box[1] + box_height > player_y and
            player_x < box[0] + box_width and
            player_x + player_width > box[0]):
            score += 1  # Catch box and increase score
        else:
            remaining_boxes.append(box)  # Keep the box if not caught
    
    boxes = remaining_boxes  # Update box list with only the remaining boxes
    
    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))
    
    # Draw boxes
    for box in boxes:
        pygame.draw.rect(screen, (0, 255, 0), (box[0], box[1], box_width, box_height))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    # Update screen and control frame rate
    pygame.display.flip()  # Update screen
    clock.tick(60)  # Limit frame rate to 60 FPS

# Quit Pygame
pygame.quit()
