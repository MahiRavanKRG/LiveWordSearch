import pygame
import pyautogui

# Initialize Pygame
pygame.init()

# Set the width and height of the box
box_width = 40
box_height = 24

# Create a Pygame window
window = pygame.display.set_mode((800, 600))

# Set the font and size
font = pygame.font.Font(None, 24)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    x, y = pyautogui.position()

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the box
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(x, y, box_width, box_height))

    # Render the text
    text = font.render('Hello, world!', True, (255, 255, 255))
    window.blit(text, (x, y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()