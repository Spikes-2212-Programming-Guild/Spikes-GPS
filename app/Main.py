from app import Map, Data as nt, Menu


def main():
    robot_width = 0.96
    robot_length = 0.86

    color = Menu.draw_menu()
    Map.draw_field(robot_length=robot_length, robot_width=robot_width, color=color, data_function=nt.get_data)


if __name__ == '__main__':
    main()