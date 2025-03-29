import pygame
import sys
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paint Application")
screen.fill(white)

clock = pygame.time.Clock()
drawing = False
last_pos = None
tool = "pencil"
radius = 5
current_color = black


def draw_line(surface, color, start_pos, end_pos, width):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start_pos[0] + float(i) / distance * dx)
        y = int(start_pos[1] + float(i) / distance * dy)
        pygame.draw.circle(surface, color, (x, y), width)


def draw_rectangle(surface, color, start_pos, end_pos):
    x = min(start_pos[0], end_pos[0])
    y = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    pygame.draw.rect(surface, color, (x, y, width, height), 2)


def draw_circle(surface, color, start_pos, end_pos):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    radius = int((dx**2 + dy**2)**0.5)
    pygame.draw.circle(surface, color, start_pos, radius, 2)


running = True
start_pos = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if tool == "rectangle" and start_pos:
                    draw_rectangle(screen, current_color, start_pos, event.pos)
                elif tool == "circle" and start_pos:
                    draw_circle(screen, current_color, start_pos, event.pos)
                start_pos = None
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "pencil":
                    draw_line(screen, current_color, last_pos, event.pos, radius)
                elif tool == "eraser":
                    draw_line(screen, white, last_pos, event.pos, radius)
                last_pos = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_p:
                tool = "pencil"
            elif event.key == pygame.K_1:
                current_color = black
            elif event.key == pygame.K_2:
                current_color = red
            elif event.key == pygame.K_3:
                current_color = green
            elif event.key == pygame.K_4:
                current_color = blue

    pygame.display.update()
    clock.tick(60)