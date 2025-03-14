import pygame
import datetime

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_face = pygame.image.load("clock_face.jpg").convert_alpha() 
right_hand = pygame.image.load("right_hand.jpg").convert_alpha()  
left_hand = pygame.image.load("left_hand.jpg").convert_alpha()  

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
    angle_minutes = -(minutes * 6)  
    angle_seconds = -(seconds * 6) 
    rotated_right_hand = pygame.transform.rotate(right_hand, angle_minutes)
    rotated_left_hand = pygame.transform.rotate(left_hand, angle_seconds)
    right_hand_rect = rotated_right_hand.get_rect(center=center)
    left_hand_rect = rotated_left_hand.get_rect(center=center)

    screen.blit(rotated_right_hand, right_hand_rect.topleft)
    screen.blit(rotated_left_hand, left_hand_rect.topleft)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

