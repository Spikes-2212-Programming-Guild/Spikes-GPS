import pygame
import time

screen_width = 784
screen_length = 455

field_width = 16.46
field_length = 8.23
red = (255, 0, 0)


get_pixle_width = lambda real_width: int(real_width * screen_width / field_width)
get_pixle_length = lambda real_length: int(real_length * screen_length / field_length)


class Robot:
    def __init__(self, width, length, image_path):
        self.image = pygame.image.load(image_path)
        self.width = get_pixle_width(width)
        self.length = get_pixle_length(length)
        self.image = pygame.transform.scale(self.image, (self.width, self.length))

        self._org_img = pygame.image.load(image_path)
        self._org_img = pygame.transform.scale(self.image, (self.width, self.length))

        self.x = 0
        self.y = 0

    def update_location(self, new_x, new_y, new_angle):
        self.x = get_pixle_width(new_x)
        self.y = get_pixle_length(new_y)

        self.image = self._org_img
        self.image = pygame.transform.rotate(self.image, new_angle-90)


def setup():
    logo = pygame.image.load("sprites/Logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Spikes GPS")


def draw_field(robot_length, robot_width, data_function=None):
    global screen_width
    global screen_length

    pygame.init()
    setup()

    screen = pygame.display.set_mode((screen_width, screen_length))
    bg = pygame.image.load("sprites/2019-field.jpg")
    bg = pygame.transform.scale(bg, (screen_width, screen_length))

    bot = Robot(robot_width, robot_length, "sprites/arrow.png")

    done = False
    while not done:

        if data_function:
            x_function, y_function, angle_function = data_function()
            bot.update_location(x_function(), y_function(), angle_function())

        screen.blit(bg, (0, 0))
        screen.blit(bot.image, (bot.x, bot.y))

        pygame.display.update()
        time.sleep(0.04)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
