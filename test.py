import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.Clock()
shape_x_pos = 0
shape_y_pos = 0
color = ['white','red','blue','purple','yellow','orange','green']
shape = pygame.draw.rect(screen, (random.choice(color)), pygame.Rect(shape_x_pos,shape_y_pos,50,50))
pygame.display.set_caption(' ')
moved = False
moving_right = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    shape = pygame.draw.rect(screen, (random.choice(color)), pygame.Rect(shape_x_pos,shape_y_pos,50,50))
    
    
    
    if moving_right:
        shape_x_pos += 5
        if shape_x_pos + 50 >= 550:
            shape_x_pos = 500
            if not moved:
                shape_y_pos += 50
                moved = True
            moving_right = False
    else: 
        shape_x_pos -= 5
        if shape_x_pos <= -50:
            shape_x_pos = 0
            if not moved:
                shape_y_pos += 50
                moved = True
            moving_right = True

    if (moving_right and shape_x_pos < 500 - 50) or (not moving_right and shape_x_pos > 0):
        moved = False
    
    if shape_x_pos == 0 and shape_y_pos == 500:
        pygame.quit()
        exit()
       

    pygame.display.update()
    clock.tick(60)


    