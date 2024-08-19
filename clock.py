import pygame
import math
from datetime import datetime, timedelta, timezone

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 800  # Increase width to accommodate two clocks side by side
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dual Clock Simulation: GMT+5 and GMT+7")
BALL_RADIUS = 5

# Set up game loop control
running = True
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Define circle and ball properties
CIRCLE_RADIUS = 150

# Clock positions
CIRCLE_CENTER_GMT5 = [WIDTH // 4, HEIGHT // 2]
CIRCLE_CENTER_GMT7 = [3 * WIDTH // 4, HEIGHT // 2]

def draw_clock(center, time, label):
    # Draw the circle
    pygame.draw.circle(window, ORANGE, center, CIRCLE_RADIUS, 3)

    # Draw the clock face
    ball_pos = [center[0], center[1] - CIRCLE_RADIUS + 20]
    pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)

    # Draw the label
    font = pygame.font.SysFont(None, 36)
    text = font.render(label, True, WHITE)
    window.blit(text, (center[0] - text.get_width() // 2, center[1] - CIRCLE_RADIUS - 40))
    
    # Extract hour, minute, and second
    hour = time.hour % 12
    minute = time.minute
    second = time.second

    # Calculate angles for each hand
    hour_angle = (360 / 12) * (hour + minute / 60.0 + second / 3600.0) - 90
    minute_angle = (360 / 60) * (minute + second / 60.0) - 90
    second_angle = (360 / 60) * second - 90

    # Draw the hour hand
    x_h = CIRCLE_RADIUS * 0.5 * math.cos(math.radians(hour_angle))
    y_h = CIRCLE_RADIUS * 0.5 * math.sin(math.radians(hour_angle))
    pygame.draw.line(window, WHITE, center, [center[0] + x_h, center[1] + y_h], 5)

    # Draw the minute hand
    x_m = CIRCLE_RADIUS * 0.7 * math.cos(math.radians(minute_angle))
    y_m = CIRCLE_RADIUS * 0.7 * math.sin(math.radians(minute_angle))
    pygame.draw.line(window, WHITE, center, [center[0] + x_m, center[1] + y_m], 3)

    # Draw the second hand
    x_s = CIRCLE_RADIUS * 0.9 * math.cos(math.radians(second_angle))
    y_s = CIRCLE_RADIUS * 0.9 * math.sin(math.radians(second_angle))
    pygame.draw.line(window, WHITE, center, [center[0] + x_s, center[1] + y_s], 1)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the window with black color
    window.fill(BLACK)
    
    # Get the current time in GMT+5 and GMT+7
    gmt_plus_5 = timezone(timedelta(hours=5))
    gmt_plus_7 = timezone(timedelta(hours=7))
    current_time_gmt5 = datetime.now(gmt_plus_5)
    current_time_gmt7 = datetime.now(gmt_plus_7)
    
    # Draw both clocks
    draw_clock(CIRCLE_CENTER_GMT5, current_time_gmt5, "GMT +5")
    draw_clock(CIRCLE_CENTER_GMT7, current_time_gmt7, "GMT +7")
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
