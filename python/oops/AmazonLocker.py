import datetime
import random
from collections import defaultdict
from enum import Enum

from abc import ABC, abstractmethod

class Temp(ABC):

    @abstractmethod
    def temp(self):
        pass

class LockerSize(Enum):
    SMALL = 100
    MEDIUM = 200
    LARGE = 300
    EXTRA_LARGE = 500
    DOUBLE_EXTRA_LARGE = 1000


class Package:
    def __init__(self, size, package_id):
        self.size = size
        self.id = package_id


class Location:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def get_location(self):
        return self.lat, self.lng


class Person:
    def __init__(self, person_id, location=None):
        self.id = person_id
        self.location = location
        self.locker = None

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_locker_to_pickup(self, locker):
        self.locker = locker

    def pickup_package(self):
        locker = self.locker
        if locker:
            return locker['pickup_package'](locker['locker_id'], locker['code'])
        return False


class Locker:
    def __init__(self, size, id, location):
        self.size = size
        self.packages = set([])
        self.location = location
        self.code = None
        self.id = id

    def add_package(self, package):
        if self.is_available():
            self.packages.add(package)
            self.set_code()
            return self
        return False

    def pickup_package(self, id, code):
        if len(self.packages):
            package_present = False
            for package in self.packages:
                if self.id == id and self.code == code:
                    package_present = package
                    break

            if package_present:
                self.packages.remove(package)
                return package

    def is_available(self):
        return len(self.packages) == 0

    @staticmethod
    def __get_random_code():
        code = ""
        for i in range(6):
            code += str(random.randrange(1, 9))
        return code

    def set_code(self):
        self.code = self.__get_random_code()

    def get_code(self):
        return self.code


class LockerSystem:
    def __init__(self):
        self.opening_time = datetime.time(8, 0, 0)
        self.closing_time = datetime.time(20, 0, 0)
        self.lockers = defaultdict(list)

    def add_lockers(self, locker):
        self.lockers[locker.size].append(locker)

    def get_nearest_locker(self, lockers, package):
        return lockers[0]

    def add_package_to_locker(self, package, person):
        current_lockers = []
        for lockers in self.lockers.values():
            for locker in lockers:
                if locker.size.value >= package.size and locker.is_available():
                    current_lockers.append(locker)

        if not len(current_lockers):
            return False

        nearest_locker = self.get_nearest_locker(current_lockers, package)
        res = nearest_locker.add_package(package)
        json = {'code': res.code, 'locker_id': res.id, 'locker_location': res.location,
                'pickup_package': res.pickup_package}
        person.set_locker_to_pickup(json)
        return res


locker_system = LockerSystem()

current_location = Location(10, 10)

locker1 = Locker(LockerSize.SMALL, 1, current_location)
locker2 = Locker(LockerSize.MEDIUM, 2, current_location)
locker3 = Locker(LockerSize.LARGE, 3, current_location)
locker4 = Locker(LockerSize.DOUBLE_EXTRA_LARGE, 4, current_location)
locker5 = Locker(LockerSize.SMALL, 5, current_location)

locker_system.add_lockers(locker1)
locker_system.add_lockers(locker2)
locker_system.add_lockers(locker3)
locker_system.add_lockers(locker4)
locker_system.add_lockers(locker5)

location1 = Location(10, 10)
person1 = Person(1, location1)

person2 = Person(2)
person2.set_location(location1)

person3 = Person(3, Location(10, 20))

package1 = Package(150, 1)
package2 = Package(500, 2)
package3 = Package(1020, 3)

res1 = locker_system.add_package_to_locker(package1, person1)
res2 = locker_system.add_package_to_locker(package2, person2)
res3 = locker_system.add_package_to_locker(package3, person3)

print(person1.pickup_package())
print(person2.pickup_package())
print(person3.pickup_package())
