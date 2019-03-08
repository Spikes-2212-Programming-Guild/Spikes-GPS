from src import map, data as nt, menu


def main():
    robot_width = 0.7
    robot_length = 0.8

    color = menu.draw_menu()
    map.draw_field(robot_length=robot_length, robot_width=robot_width, color=color, data_function=nt.get_data)


if __name__ == '__main__':
    main()