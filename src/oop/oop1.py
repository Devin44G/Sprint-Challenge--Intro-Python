# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# BASE CLASS:
class Vehicle:
    """docstring for Vehicle. This is the base class"""
    pass


# GroundVehicle and its children:
class GroundVehicle(Vehicle):
    """docstring for GroundVehicle. Child of Vehicle"""
    pass


class Car(GroundVehicle):
    """docstring for Car. Child of GroundVehicle. Granchild of Vehicle"""
    pass


class Motorcycle(GroundVehicle):
    """docstring for Motorcycle. Child of GroundVehicle.
    Granchild of Vehicle"""
    pass


# FlightVehicle and its children:
class FlightVehicle(Vehicle):
    """docstring for FlightVehicle. Child of Vehicle"""
    pass


class Airplane(FlightVehicle):
    """docstring for Airplane. Child of FlightVehicle. Granchild of Vehicle"""
    pass


class Starship(FlightVehicle):
    """docstring for Starship. Child of FlightVehicle. Granchild of Vehicle"""
    pass
