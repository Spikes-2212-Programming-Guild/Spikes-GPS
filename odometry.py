from networktables import NetworkTables as nt
import math
import mathutil
from src import map
nt.initialize(server="10.22.12.2")
smart_dashboard = nt.getTable("SmartDashboard")
preferences = nt.getTable("Preferences")


class OdometryHandler:
    def __init__(self, x, y, yaw, width_entry, length_entry, left_distance_entry, right_distance_entry, angle_entry):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.width = preferences.getNumber(width_entry, 0)
        self.length = preferences.getNumber(length_entry, 0)
        self._left_distance = smart_dashboard.getNumber(left_distance_entry, 0)
        self._right_distance = smart_dashboard.getNumber(right_distance_entry, 0)
        self._robot_angle = smart_dashboard.getNumber(angle_entry, 0)

        def get_left_distance():
            left_displacement = smart_dashboard.getNumber(left_distance_entry, 0) - self._left_distance
            self._left_distance = smart_dashboard.getNumber(left_distance_entry, 0)
            return left_displacement

        self.left_distance_supplier = get_left_distance

        def get_right_distance():
            right_displacement = smart_dashboard.getNumber(right_distance_entry, 0) - self._right_distance
            self._right_distance = smart_dashboard.getNumber(right_distance_entry, 0)
            return right_displacement

        self.right_distance_supplier = get_right_distance

        def get_angle_change():
            angle_change = smart_dashboard.getNumber(angle_entry, 0) - self._robot_angle
            self._robot_angle = smart_dashboard.getNumber(angle_entry, 0)
            return angle_change

        self.yaw_difference_supplier = get_angle_change

        def get_angle():
            return smart_dashboard.getNumber(angle_entry, 0) + self.yaw

        self.angle_supplier = get_angle

    def calculate(self):
        yaw = math.radians(self.angle_supplier())
        right_distance = self.right_distance_supplier()
        left_distance = self.left_distance_supplier()
        yaw_difference = self.yaw_difference_supplier()
        arch_distance = (right_distance + left_distance) / 2
        if yaw_difference == 0:
            center_distance = abs(right_distance)
        else:
            rotation_radius = arch_distance / yaw_difference
            center_distance = mathutil.cosinelaw(rotation_radius, rotation_radius, yaw_difference)
        arg = yaw - 1 / 2.0 * yaw_difference
        if arch_distance < 0:
            arg += math.pi
        x_displacement, y_displacement = mathutil.tocartesian(center_distance, -arg)
        self.x += x_displacement
        self.y += y_displacement

    def data_function(self):
        return self.x, self.y, self.angle_supplier()

    def set_position(self, x, y, yaw):
        self.x = x
        self.y = y
        self.yaw = yaw
