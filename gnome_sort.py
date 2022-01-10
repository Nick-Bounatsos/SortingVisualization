import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gnome Sort")


class Array(list):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.append(value)

    def gnome_sort(self) -> None:
        """Gnome sorts the array."""
        n = len(self)
        index = 0
        while index < n:
            if self[index] >= self[index - 1] or index == 0:
                index += 1
            else:
                pygame.time.wait(1)
                self[index], self[index - 1] = self[index - 1], self[index]
                index -= 1

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
            threading.Thread(target=array.gnome_sort).start()
    array.draw()
    pygame.display.update()
