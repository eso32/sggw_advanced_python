from enum import Enum

class TitleStatus(Enum):
    SALVAGE = "Salvage"
    CLEAR = "Clear"

class PrimaryDamage(Enum):
    FRONT_END = "Front End"
    REAR = "Rear"
    ALL_OVER = "All Over"
    NORMAL_WEAR = "Normal Wear & Tear"
    LEFT_REAR = "Left Rear"
    OTHER = "Other"

class VehicleType(Enum):
    SUV = "SUVs"
    AUTOMOBILE = "Automobiles"
    VAN = "Vans"
    MOTORCYCLE = "Motorcycles"

class TransmissionType(Enum):
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    UNKNOWN = "Unknown"

class DriveLineType(Enum):
    FWD = "Front Wheel Drive"
    RWD = "Rear Wheel Drive"
    FOUR_WD = "Four Wheel Drive"
    FOUR_X_TWO = "4X2 Drive"
    UNKNOWN = "Unknown"

class SellerType(Enum):
    INSURANCE = "Insurance"
    NON_INSURANCE = "Non-Insurance"

class FuelType(Enum):
    GASOLINE = "Gasoline"
    DIESEL = "Diesel"
    FLEXIBLE = "Flexible Fuel"
    ELECTRIC = "Electric"
    OTHER = "Other"

class ACVType(Enum):
    E = "E"
    MC = "MC"
    EV = "EV"
    U = "U"

class BodyStyle(Enum):
    SUV = "Sport Utility"
    SEDAN = "Sedan"
    VAN = "Passenger Van"
    WAGON = "Wagon"
    CREW_CAB = "Crew Cab"
    REGULAR_CAB = "Regular Cab Styleside"
    OTHER = "Other"

