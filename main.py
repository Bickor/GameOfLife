import sys, pygame


size = [255, 255]
width = 20
height = 20
margin = 5

black = 0, 0, 0
grey = 128, 128, 128
white = 255, 255, 255

def main():
    # ball = pygame.image.load("intro_ball.gif")
    # ballrect = ball.get_rect()
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(black)

    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(1)

    grid[1][5] = 0

    # Main loop
    while 1:
        # Event logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = pygame.mouse.get_pos()
                print("Click: ({0}, {1})".format(x_pos, y_pos))

        # Game logic
        for column in range(10):
            for row in range(10):
                rect = pygame.Rect(margin + column * width + column * margin, margin + row * width + row * margin, width, height)
                if grid[row][column]:
                    pygame.draw.rect(screen, white, rect)
                else:
                    pygame.draw.rect(screen, grey, rect)

        # Drawing logic
        pygame.display.update()

main()