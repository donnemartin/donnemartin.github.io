from abc import ABCMeta, abstractmethod
from enum import Enum


class VehicleSize(Enum):

    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2


class Vehicle(metaclass=ABCMeta):

    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size
        self.spots_taken = []
