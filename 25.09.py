#import pygame
#import sys
#import math
 
#size = width, height = 800, 600
#black = 0, 0, 0

#bg = pygame.image.load("bg.png")
#gameDisplay.blit(bg, (0, 0))

#def main():
#    pygame.init()
 
#    screen = pygame.display.set_mode(size)
#    game_over = False
#    smile_x = 150
#    smile_y = 150
#    circle1_x = 100
#    circle1_y = 100
#    circle2_x = 200
#    circle2_y = 100
#    mouth_x1 = 85
#    mouth_x2 = 145
#    mouth_y1 = 150
#    mouth_y2 = 150
#    while not game_over:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                game_over = True
#        if smile_x < 800 or smile_y < 800:
#            screen.fill(black)
#            smile_x += 1
#            smile_y += 1
#            circle1_x += 1
#            circle1_y += 1
#            circle2_x += 1
#            circle2_y += 1
#            mouth_x1 += 1
#            mouth_x2 += 1
#            mouth_y1 += 1
#             mouth_y2 += 1
#        else:
#            pass
#        pygame.draw.circle(screen, (0, 255, 0), (smile_x, smile_y), 150)
#        pygame.draw.circle(screen, (255, 255, 255), (circle1_x, circle1_y), 30)
#        pygame.draw.circle(screen, (255, 255, 255), (circle2_x, circle2_y), 30)
#        pygame.draw.arc(screen, (255, 0, 0), (mouth_x1, mouth_y1, 70, 70), math.pi, 2 * math.pi, 5)
#        pygame.draw.arc(screen, (255, 0, 0), (mouth_x2, mouth_y2, 70, 70), math.pi, 2 * math.pi, 5)
#        pygame.display.flip()
#        pygame.time.wait(10)
 
 
#if __name__ == '__main__':
#    main()
#    pygame.quit()

