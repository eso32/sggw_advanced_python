from datetime import datetime
from pydantic.dataclasses import dataclass

@dataclass(frozen=True)
class Auction:
    auction_date: datetime
    branch_name: str
    region: str
