# Design a parking lot

## Constraints and assumptions

* What types of vehicles should we support?
** Motorcycle, Car, Bus
* Does each vehicle type take up a different amount of parking spots?
** Yes
** Motorcycle spot -> Motorcycle
** Compact spot -> Motorcycle, Car
** Large spot -> Motorcycle, Car
** Bus can park if we have 5 consecutive "large" spots
* Does the parking lot have multiple levels?
** Yes

```
from abc import ABCMeta, abstractmethod


class VehicleSize(Enum):

    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2

class Vehicle(metaclass=ABCMeta):

    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []

    def clear_spots(self):
        for spot in self.spots_taken:
            spot.remove_vehicle(self)
        self.spots_taken = []

    def take_spot(self, spot):
        self.spots_taken.append(spot)

    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass

class Motorcycle(Vehicle):

    def __init__(self, license_plate):
        super(Motorcycle, self).__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True

class Car(Vehicle):

    def __init__(self, license_plate):
        super(Car, self).__init__(VehicleSize.COMPACT, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True if (spot.size == LARGE or spot.size == COMPACT) else False

class Bus(Vehicle):

    def __init__(self, license_plate):
        super(Bus, self).__init__(VehicleSize.LARGE, license_plate, spot_size=5)

    def can_fit_in_spot(self, spot):
        return True if spot.size == LARGE else False

class ParkingLot(object):

    def __init__(self, num_levels):
        self.num_levels = num_levels
        self.levels = []

    def park_vehicle(self, vehicle):
        for level in levels:
            if level.park_vehicle(vehicle):
                return True
        return False
```
