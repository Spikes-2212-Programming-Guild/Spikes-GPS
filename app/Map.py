import pygame
import time

screen_width = 784
screen_height = 455

field_width = 16.46
field_length = 8.23
red = (255, 0, 0)


get_pixle_width = lambda real_width: int(real_width * screen_width / field_width)
get_pixle_length = lambda real_length: int(real_length * screen_width / field_width)


class Robot:
    def __init__(self, width, length, image_path):
        self.image = pygame.image.load(image_path)
        self.width = get_pixle_width(width)
        self.length = get_pixle_length(length)
        self.image = pygame.transform.scale(self.image, (self.width, self.length))

        self._org_img = pygame.image.load(image_path)
        self._org_img = pygame.transform.scale(self.image, (self.width, self.length))

        self.x = 0
        self.y = 200
        self.angle = 0

    def update_location(self, delta_width, delta_length, delta_angle):
        self.x = get_pixle_width(delta_width)
        self.y = get_pixle_length(delta_length)

        self.image = self._org_img
        self.image = pygame.transform.rotate(self.image, delta_angle-90)
        self.angle = delta_angle


def setup():
    logo = pygame.image.load("sprites/Logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Auto courses")


def main():
    global screen_width
    global screen_height

    pygame.init()
    setup()

    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = pygame.image.load("sprites/2019-field.jpg")
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    roby = Robot(1, 1, "sprites/arraow.png")

    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.blit(bg, (0, 0))
        screen.blit(roby.image, (roby.x, roby.y))

        pygame.display.update()
        time.sleep(0.04)


if __name__ == '__main__':
    main()
