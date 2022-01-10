import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort")


class Array(list):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.append(value)

    def bubble_sort(self) -> None:
        """Bubble sorts the array."""
        n = len(self)
        for i in range(0, n):
            swapped = False
            for j in range(0, n - i - 1):
                if self[j] > self[j + 1]:
                    pygame.time.wait(1)
                    self[j], self[j + 1] = self[j + 1], self[j]
                    swapped = True
            if not swapped:
                break

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
            threading.Thread(target=array.bubble_sort).start()
    array.draw()
    pygame.display.update()
