import pygame
import sys
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
colors = [black, red, green, blue, yellow, purple]

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enhanced Paint Application")
screen.fill(white)

clock = pygame.time.Clock()

drawing = False
last_pos = None
tool = "pencil"  
radius = 5     
current_color = black
fill_mode = False 

font = pygame.font.SysFont('Arial', 16)

def draw_line(surface, color, start_pos, end_pos, width):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start_pos[0] + float(i) / distance * dx)
        y = int(start_pos[1] + float(i) / distance * dy)
        pygame.draw.circle(surface, color, (x, y), width)

def draw_rectangle(surface, color, start_pos, end_pos, fill=False):
    x = min(start_pos[0], end_pos[0])
    y = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    if fill:
        pygame.draw.rect(surface, color, (x, y, width, height))
    else:
        pygame.draw.rect(surface, color, (x, y, width, height), 2)

def draw_circle(surface, color, start_pos, end_pos, fill=False):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    radius = int((dx**2 + dy**2)**0.5)
    if fill:
        pygame.draw.circle(surface, color, start_pos, radius)
    else:
        pygame.draw.circle(surface, color, start_pos, radius, 2)

def draw_ui():
    tool_text = font.render(f"Tool: {tool}", True, black)
    screen.blit(tool_text, (10, 10))
    
    color_text = font.render(f"Color: {current_color}", True, black)
    screen.blit(color_text, (10, 30))
    
    size_text = font.render(f"Brush Size: {radius}", True, black)
    screen.blit(size_text, (10, 50))
    
    fill_text = font.render(f"Fill: {'ON' if fill_mode else 'OFF'}", True, black)
    screen.blit(fill_text, (10, 70))
    
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (700, 10 + i*30, 25, 25))
        if color == current_color:
            pygame.draw.rect(screen, black, (700, 10 + i*30, 25, 25), 2)

def clear_screen():
    screen.fill(white)

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
                last_pos = event.pos
                start_pos = event.pos
                
                for i, color in enumerate(colors):
                    if 700 <= event.pos[0] <= 725 and 10 + i*30 <= event.pos[1] <= 35 + i*30:
                        current_color = color
            
            elif event.button == 4:  
                radius = min(50, radius + 1)
            elif event.button == 5:  
                radius = max(1, radius - 1)
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                drawing = False
                if tool == "rectangle" and start_pos:
                    draw_rectangle(screen, current_color, start_pos, event.pos, fill_mode)
                elif tool == "circle" and start_pos:
                    draw_circle(screen, current_color, start_pos, event.pos, fill_mode)
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
            elif event.key == pygame.K_f:
                fill_mode = not fill_mode  
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                radius = min(50, radius + 1) 
            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 1)  
            elif event.key == pygame.K_SPACE:
                clear_screen()  
            
            if pygame.K_1 <= event.key <= pygame.K_6:
                index = event.key - pygame.K_1
                if index < len(colors):
                    current_color = colors[index]
    
    draw_ui()
    
    pygame.display.update()
    clock.tick(60)