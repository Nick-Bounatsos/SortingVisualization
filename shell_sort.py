import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shell Sort")


class Array(list):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.append(value)

    def shell_sort(self) -> None:
        """Shell sorts the array."""
        n = len(self)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                key = self[i]
                j = i
                while j >= gap and self[j - gap] > key:
                    pygame.time.wait(1)
                    self[j] = self[j - gap]
                    j -= gap
                self[j] = key
            gap //= 2

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
            threading.Thread(target=array.shell_sort).start()
    array.draw()
    pygame.display.update()
