from src import window_handler
import pygame

screen_width = 960
screen_length = 656

field_width = 10.3632
field_length = 8.2296
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
        self.image = pygame.transform.rotate(self.image, new_angle)


def setup():
    logo = pygame.image.load("sprites/Logo.ico")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Spikes GPS")


def init_field(color):
    global screen
    global screen_width
    global screen_length

    pygame.init()
    setup()

    screen = pygame.display.set_mode((screen_width, screen_length))
    bg = pygame.image.load("sprites/2019-field.jpg")
    bg = pygame.transform.scale(bg, (screen_width, screen_length))
    if color == "red":
        bg = pygame.transform.rotate(bg, 180)

    window_handler.on_top(pygame.display.get_wm_info()['window'])
    screen.blit(bg, (0, 0))


def draw_field(robot_length, robot_width, data_function):
    bot = Robot(robot_width, robot_length, "sprites/arrow.png")
    if data_function:
        x, y, angle = data_function()
        bot.update_location(x, y, angle)

    screen.blit(bot.image, (bot.x, bot.y))

    pygame.display.update()
