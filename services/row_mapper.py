from dateutil import parser
from dateutil.tz import gettz
from models.auction import Auction
from models.vehicle import Vehicle
from services.parsers import parse_int, parse_body_style, parse_fuel_type, parse_transmission, parse_drive_line


TZINFOS = {
    "CST": gettz("US/Central"),
    "CDT": gettz("US/Central"),
    "EST": gettz("US/Eastern"),
    "EDT": gettz("US/Eastern"),
    "PST": gettz("US/Pacific"),
    "PDT": gettz("US/Pacific"),
    "CEST": gettz("Europe/Berlin"),
    "CEDT": gettz("Europe/Berlin"),
    "UTC": gettz("UTC")
}

class RowMapper:
    @staticmethod
    def to_auction(row: dict):
        try:
            auction_date = parser.parse(row['Auction Date'], tzinfos=TZINFOS)
        except Exception:
            # fallback: usuń wszystko po ostatniej spacji i sparsuj bez tz
            date_clean = row['Auction Date'].rsplit(' ', 1)[0]
            auction_date = parser.parse(date_clean)

        return Auction(
            auction_date=auction_date,
            branch_name=row['Branch Name'],
            region=row['Region']
        )

    @staticmethod
    def to_vehicle(row: dict) -> Vehicle:
        return Vehicle(
            stock_number=int(row["Stock Number"]),
            year=int(row["Year"]),
            make=row["Make"],
            model=row["Model"],
            series=row.get("Series Name"),
            mileage=parse_int(row.get("Odometer")),
            fuel_type=parse_fuel_type(row.get("Fuel Type")),
            transmission=parse_transmission(row.get("Transmission Type")),
            drive_line=parse_drive_line(row.get("Drive Line Type")),
            body_style=parse_body_style(row.get("Body Style")),
            current_bid_usd=parse_int(row.get("Current Bid")),
            vin=row.get("Vin#")
        )
