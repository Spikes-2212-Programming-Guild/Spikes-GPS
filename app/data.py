from networktables import NetworkTables
import logging

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize(server="10.22.12.2")
sd = NetworkTables.getTable("SmartDashboard")


def get_data():
    x = sd.getNumber("Robot x", 0)
    y = sd.getNumber("Robot y", 0)
    angle = sd.getNumber("Robot angle", 0)
    return x, y, angle
