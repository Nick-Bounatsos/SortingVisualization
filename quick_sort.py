import pygame
import random
import threading

pygame.init()
WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quick Sort")


def quick_sort(array: list, low: int, high: int) -> None:
    """Quick sorts the array."""
    # This algorithm picks the last item as pivot, and partitions around it.
    if low < high:
        # Pick the last item as pivot, place it at the correct spot
        # And place all smaller to its left, and all greater to its right
        i = low - 1  # index of smaller element
        pivot = array[high]
        for j in range(low, high):
            # If current element is smaller than the pivot
            if array[j] < pivot:
                pygame.time.delay(1)
                # Increment index of smaller element
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        partition_index = i + 1

        # Separately sort elements before and after partition
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)


def draw(array: list) -> None:
    """Projects the array on the screen. The index is x, and the value is y."""
    n = len(array)
    for i in range(0, n):
        pygame.draw.line(screen, (0, 0, 0), (i, HEIGHT), (i, HEIGHT - array[i]), 1)


array = []
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
            threading.Thread(target=quick_sort, args=[array, 0, len(array) - 1]).start()
    draw(array)
    pygame.display.update()
