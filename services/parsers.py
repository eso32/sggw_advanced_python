import re
from typing import Optional
from models.enums import BodyStyle, FuelType, TransmissionType, DriveLineType


def parse_int(value: str) -> Optional[int]:
    if not value:
        return None
    digits = re.sub(r'[^0-9]', '', value)
    return int(digits) if digits else None

def parse_body_style(value: str) -> BodyStyle:
    try:
        return BodyStyle(value)
    except ValueError:
        return BodyStyle.OTHER

def parse_fuel_type(value: str) -> FuelType:
    try:
        return FuelType(value)
    except ValueError:
        return FuelType.OTHER

def parse_transmission(value: str) -> TransmissionType:
    try:
        return TransmissionType(value)
    except ValueError:
        return TransmissionType.UNKNOWN

def parse_drive_line(value: str) -> DriveLineType:
    try:
        return DriveLineType(value)
    except ValueError:
        return DriveLineType.UNKNOWN