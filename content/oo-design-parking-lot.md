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
```
