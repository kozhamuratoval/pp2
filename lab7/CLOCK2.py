import pygame
import datetime
import math
#CORRECT 
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
clock_face = pygame.image.load("clock_face.jpg").convert_alpha()

MINUTE_HAND_COLOR = (0, 0, 0)
SECOND_HAND_COLOR = (255, 0, 0) 

MINUTE_HAND_LENGTH = 150
SECOND_HAND_LENGTH = 200
center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) 
    clock_face_rect = clock_face.get_rect(center=center)
    screen.blit(clock_face, clock_face_rect)
    current_time = datetime.datetime.now()
    minutes = current_time.minute
    seconds = current_time.second
    angle_minutes = (minutes * 6) % 360  
    angle_seconds = (seconds * 6) % 360  
    angle_minutes_rad = math.radians(angle_minutes)
    angle_seconds_rad = math.radians(angle_seconds)

    minute_hand_end_x = center[0] + MINUTE_HAND_LENGTH * math.sin(angle_minutes_rad)
    minute_hand_end_y = center[1] - MINUTE_HAND_LENGTH * math.cos(angle_minutes_rad)
    minute_hand_end = (minute_hand_end_x, minute_hand_end_y)

    second_hand_end_x = center[0] + SECOND_HAND_LENGTH * math.sin(angle_seconds_rad)
    second_hand_end_y = center[1] - SECOND_HAND_LENGTH * math.cos(angle_seconds_rad)
    second_hand_end = (second_hand_end_x, second_hand_end_y)
    pygame.draw.line(screen, MINUTE_HAND_COLOR, center, minute_hand_end, 5)  
    pygame.draw.line(screen, SECOND_HAND_COLOR, center, second_hand_end, 3) 

    pygame.draw.circle(screen, (0, 0, 0), center, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()