from services.parsers import (
    parse_int,
    parse_body_style,
    parse_fuel_type,
    parse_transmission,
    parse_drive_line
)
from models.enums import BodyStyle, FuelType, TransmissionType, DriveLineType

def test_parse_int():
    assert parse_int('155,445 mi') == 155445
    assert parse_int('$2,200 USD') == 2200
    assert parse_int('') is None

def test_parse_body_style():
    assert parse_body_style('Sport Utility') == BodyStyle.SUV
    assert parse_body_style('Sedan') == BodyStyle.SEDAN
    assert parse_body_style('Wagon') == BodyStyle.WAGON
    assert parse_body_style('Nonsensowna wartość') == BodyStyle.OTHER

def test_parse_fuel_type():
    assert parse_fuel_type('Gasoline') == FuelType.GASOLINE
    assert parse_fuel_type('Electric') == FuelType.ELECTRIC
    assert parse_fuel_type('') == FuelType.OTHER
    assert parse_fuel_type('Diesel') == FuelType.DIESEL
    assert parse_fuel_type('Coś dziwnego') == FuelType.OTHER

def test_parse_transmission():
    assert parse_transmission('Automatic') == TransmissionType.AUTOMATIC
    assert parse_transmission('Manual') == TransmissionType.MANUAL
    assert parse_transmission('Unknown') == TransmissionType.UNKNOWN
    assert parse_transmission('Nonsense') == TransmissionType.UNKNOWN

def test_parse_drive_line():
    assert parse_drive_line('Front Wheel Drive') == DriveLineType.FWD
    assert parse_drive_line('Rear Wheel Drive') == DriveLineType.RWD
    assert parse_drive_line('Four Wheel Drive') == DriveLineType.FOUR_WD
    assert parse_drive_line('4X2 Drive') == DriveLineType.FOUR_X_TWO
    assert parse_drive_line('Coś nieznane') == DriveLineType.UNKNOWN
