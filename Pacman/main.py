import pygame
import math
from board import board

pygame.init()

WIDTH = 900
HEIGHT = 950
fps = 60

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
level = board
color = 'purple'
PI = math.pi

run = True


def draw_board():
    rows = ((HEIGHT - 50)//32)
    cols = (WIDTH // 30)

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * cols + (0.5 * cols), i * rows + (0.5 * rows)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * cols + (0.5 * cols), i * rows + (0.5 * rows)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * cols + (0.5 * cols), i * rows),
                                 (j * cols + (0.5 * cols), i * rows + rows), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * cols, i * rows + (0.5 * rows)),
                                 (j * cols + cols, i * rows + (0.5 * rows)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j*cols - (cols * 0.5)), (i * rows + (0.5 * rows)), cols, rows],
                                0, PI/2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j*cols + (cols * 0.5)), (i * rows + (0.5 * rows)), cols, rows],
                                PI/2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j*cols + (cols * 0.5)), (i * rows - (0.5 * rows)), cols, rows],
                                PI, 3*PI/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j*cols - (cols * 0.5)), (i * rows - (0.5 * rows)), cols, rows],
                                3*PI/2, 2*PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * cols, i * rows + (0.5 * rows)),
                                 (j * cols + cols, i * rows + (0.5 * rows)), 3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

    while run:
        timer.tick(fps)
        screen.fill('black')

        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip() # everything that is drawn in every iteration

    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
