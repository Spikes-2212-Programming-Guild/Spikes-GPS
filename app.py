from src import menu, map
import odometry
import time
import pygame


def main():
    color = menu.draw_menu()
    map.init_field(color)

    handler = odometry.OdometryHandler(0, 0, 0, "width", "length", "Robot x", "Robot y", "Robot angle")
    done = False
    while not done:
        handler.calculate()
        map.draw_field(handler.length, handler.width, handler.data_function)
        time.sleep(0.04)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


if __name__ == '__main__':
    main()
