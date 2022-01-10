import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cycle Sort")


class Array(list):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.append(value)

    def cycle_sort(self) -> None:
        """Cycle sorts the array."""
        n = len(self)

        # Loop through the array to find cycles to rotate.
        for cycle_start in range(0, n - 1):
            pygame.time.wait(10)
            item = self[cycle_start]

            # Find where to put the item.
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if self[i] < item:
                    pos += 1

            # If the item is already there, this is not a cycle.
            if pos == cycle_start:
                continue

            # Otherwise, put the item there or right after any duplicates.
            while item == self[pos]:
                pos += 1
            self[pos], item = item, self[pos]

            # Rotate the rest of the cycle.
            while pos != cycle_start:
                pygame.time.wait(1)
                # Find where to put the item.
                pos = cycle_start
                for i in range(cycle_start + 1, n):
                    if self[i] < item:
                        pos += 1

                # Put the item there or right after any duplicates.
                while item == self[pos]:
                    pygame.time.wait(1)
                    pos += 1
                self[pos], item = item, self[pos]

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
            threading.Thread(target=array.cycle_sort).start()
    array.draw()
    pygame.display.update()
