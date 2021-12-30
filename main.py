import sys, pygame


size = [255, 255]
width = 20
height = 20
margin = 5

black = 0, 0, 0
grey = 128, 128, 128
white = 255, 255, 255

# Return the number of alive surrounding cells
def living_neighbors(grid, x_pos, y_pos):
    total = 0
    for column in range(max(0, x_pos - 1), min(10, x_pos + 2)):
        for row in range(max(0, y_pos - 1), min(10, y_pos + 2)):
            # print("{0}, {1}".format(row, column))
            if column == x_pos and row == y_pos:
                continue
            else:
                if grid[row][column] == 1:
                    total += 1
    return total

def main():
    # ball = pygame.image.load("intro_ball.gif")
    # ballrect = ball.get_rect()
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(black)

    # Remember that the grid is row first column second
    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)

    # Don't start evolution until the player wants it to start
    evolve = False

    # Main loop
    while 1:
        # Event logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # Set the block as turned on or off
            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = pygame.mouse.get_pos()
                x_pos = x_pos // (width + margin)
                if x_pos == 10:
                    x_pos = 9
                y_pos = y_pos // (height + margin)
                if y_pos == 10:
                    y_pos = 9
                grid[y_pos][x_pos] = 0 if grid[y_pos][x_pos] else 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    evolve = False if evolve else True

        # Game logic
        if evolve:
            # Copy grid
            grid_copy = []
            for row in range(10):
                grid_copy.append([])
                for column in range(10):
                    grid_copy[row].append(grid[row][column])

            # Rules of life
            for column in range(10):
                for row in range(10):
                    total = living_neighbors(grid, column, row)
                    if grid[row][column] == 1: # If the cell is alive
                        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                        if total < 2:
                            grid_copy[row][column] = 0
                        
                        # Any live cell with more than three live neighbours dies, as if by overpopulation.
                        elif total > 3:
                            grid_copy[row][column] = 0

                        # Any live cell with two or three live neighbours lives on to the next generation.
                    else:
                        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                        if total == 3:
                            grid_copy[row][column] = 1
            grid = grid_copy
            pygame.time.wait(500)
                

        # Drawing logic
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