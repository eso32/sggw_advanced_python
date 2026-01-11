from pydantic.dataclasses import dataclass
from typing import Optional
from models.enums import FuelType, TransmissionType, DriveLineType, BodyStyle

@dataclass
class Vehicle:
    stock_number: int
    year: int
    make: str
    model: str
    series: Optional[str]
    mileage: Optional[int]
    fuel_type: Optional[FuelType]
    transmission: Optional[TransmissionType]
    drive_line: Optional[DriveLineType]
    body_style: Optional[BodyStyle]
    current_bid_usd: Optional[int]
    vin: str
