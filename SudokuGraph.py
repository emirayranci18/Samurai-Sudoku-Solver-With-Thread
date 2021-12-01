import pygame
import SudokuCreater
import SudokuCreaterT
import SudokuSolver
import matplotlib.pyplot as plt


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 28)

WIDTH = 40
HEIGHT = 40
MARGIN = 1

grid = []
for row in range(21):
    grid.append([])
    for column in range(21):
        grid[row].append(0)


pygame.init()
WINDOW_SIZE = [900, 900]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Çözücü")

done = False
clock = pygame.time.Clock()

if SudokuSolver.final():
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        for row in range(21):
            for column in range(21):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN

                if grid[row][column] == 0:
                    color = WHITE
                    img = font.render('1', True, BLACK)

                if (row <= 8 and column <= 8) or (column >= 12 and row <= 8) or (row >= 12 and column <= 8) or (
                        row >= 12 and column >= 12) or (
                        (row >= 6 and column >= 6) and (row <= 14 and column <= 14)):
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

        for b in range(9):
            for a in range(9):
                txt = str(SudokuCreater.sudoku1[b][a])
                text = font.render(txt, False, BLACK)
                screen.blit(text, (10 + (a * 41), 10 + (b * 41)))

        for a in range(9):
            for b in range(9):
                txt = str(SudokuCreater.sudoku2[b][a])
                text = font.render(txt, False, BLACK)
                screen.blit(text, (500 + (a * 41), 10 + (b * 41)))

        for a in range(9):
            for b in range(9):
                txt = str(SudokuCreater.sudoku4[b][a])
                text = font.render(txt, False, BLACK)
                screen.blit(text, (10 + (a * 41), 500 + (b * 41)))

        for a in range(9):
            for b in range(9):
                txt = str(SudokuCreater.sudoku5[b][a])
                text = font.render(txt, False, BLACK)
                screen.blit(text, (500 + (a * 41), 500 + (b * 41)))

        for a in range(9):
            for b in range(9):
                if 2 < a < 6 and b < 3:
                    txt = str(SudokuCreater.sudoku3[b][a])
                    text = font.render(txt, False, BLACK)
                    screen.blit(text, (255 + (a * 41), 255 + (b * 41)))
                elif 6 > b > 2:
                    txt = str(SudokuCreater.sudoku3[b][a])
                    text = font.render(txt, False, BLACK)
                    screen.blit(text, (255 + (a * 41), 255 + (b * 41)))
                if 2 < a < 6 and b > 5:
                    txt = str(SudokuCreater.sudoku3[b][a])
                    text = font.render(txt, False, BLACK)
                    screen.blit(text, (255 + (a * 41), 255 + (b * 41)))

        clock.tick(60)
        pygame.display.flip()

pygame.quit()