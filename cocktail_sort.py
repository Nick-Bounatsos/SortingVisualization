import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cocktail Sort")


class Array(list):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.append(value)

    def cocktail_sort(self) -> None:
        """Cocktail sorts the array."""
        n = len(self)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            # Loop from left to right same as the bubble sort
            for i in range(start, end):
                if self[i] > self[i + 1]:
                    self[i], self[i + 1] = self[i + 1], self[i]
                    pygame.time.wait(1)
                    swapped = True

            if not swapped:
                break

            swapped = False
            # Move the end point back by one, because item at the end is in its rightful spot
            end -= 1
            # Loop from right to left same as the bubble sort
            for i in range(end - 1, start - 1, -1):
                if self[i] > self[i + 1]:
                    self[i], self[i + 1] = self[i + 1], self[i]
                    pygame.time.wait(1)
                    swapped = True
            # Move the start point forward by one, because item at the start is in its rightful spot
            start += 1

    def draw(self) -> None:
        """Projects the array on the screen. The index is x, and the value is y."""
        n = len(self)
        for i in range(0, n):
            pygame.draw.line(screen, (0, 0, 0), (i, HEIGHT), (i, HEIGHT - self[i]), 1)


array = Array()
for i in range(WIDTH):
    array.append(random.randint(0, HEIGHT - 20))

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Start sorting on mouse button click or enter
            threading.Thread(target=array.cocktail_sort).start()
    array.draw()
    pygame.display.update()
