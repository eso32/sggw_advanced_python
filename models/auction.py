from datetime import datetime
from typing import List
from pydantic.dataclasses import dataclass, Field
from models.vehicle import Vehicle

@dataclass
class Auction:
    auction_date: datetime
    branch_name: str
    region: str
    vehicles: List[Vehicle] = Field(default_factory=list)
