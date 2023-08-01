import pygame

pygame.init()

WIDTH = 900
HEIGHT = 950
fps = 60

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)

run = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

    while run:
        timer.tick(fps)
        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip() # everything that is drawn in every iteration

    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
