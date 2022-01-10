import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Search")


class Array(list):
    low = 0
    high = WIDTH

    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.append(value)
        self.low = -1
        self.high = -1

    def binary_search(self, key) -> int:
        """Performs binary search on a sorted iterable and returns the keys' index.
        Returns -1 if it doesn't exist. Can also search within a section [low, high]."""
        self.low = 0
        self.high = len(self) - 1
        if self[self.low] < self[self.high]:  # Check whether the iterable is in ascending/descending order
            # Ascending
            while self.low <= self.high:
                pygame.time.wait(500)
                self.draw(self.low, self.high)
                middle = (self.low + self.high) // 2
                if key < self[middle]:  # If key is smaller search the left half
                    self.high = middle - 1
                elif key > self[middle]:  # If key is greater search the right half
                    self.low = middle + 1
                else:
                    self.low = middle
                    self.high = middle
                    return middle
        return -1

    def draw(self, low, high) -> None:
        """Projects the array on the screen. The index is x, and the value is y."""
        n = len(self)
        for i in range(0, n):
            if low <= i <= high:
                pygame.draw.line(screen, (100, 100, 100), (i, HEIGHT), (i, HEIGHT - self[i]), 1)
            else:
                pygame.draw.line(screen, (0, 0, 0), (i, HEIGHT), (i, HEIGHT - self[i]), 1)


array = Array()
for i in range(WIDTH):
    array.append(random.randint(0, HEIGHT - 20))
array.sort()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Start sorting on mouse button click or enter
            threading.Thread(target=array.binary_search, args=[random.choice(array)]).start()
    array.draw(array.low, array.high)
    pygame.display.update()
