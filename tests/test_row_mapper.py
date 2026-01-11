import pytest
from services.row_mapper import RowMapper
from models.auction import Auction
from models.vehicle import Vehicle
from models.enums import FuelType, TransmissionType, DriveLineType, BodyStyle
from datetime import datetime

def test_to_auction_regular_tz():
    row = {
        'Auction Date': '2025-12-09 09:00:00 CST',
        'Branch Name': 'Dallas',
        'Region': 'South'
    }
    auction = RowMapper.to_auction(row)
    assert isinstance(auction, Auction)
    assert auction.branch_name == 'Dallas'
    assert auction.region == 'South'
    assert auction.auction_date.year == 2025
    assert auction.auction_date.tzinfo is not None

    assert auction.auction_date.strftime('%Z') in ('CST', 'CDT')

def test_to_auction_fallback_no_tz():
    row = {
        'Auction Date': '2025-12-09 09:00:00 extra',
        'Branch Name': 'Dallas',
        'Region': 'South'
    }
    auction = RowMapper.to_auction(row)
    assert auction.auction_date.year == 2025
    assert auction.auction_date.tzinfo is None

def test_to_vehicle_parsing():
    row = {
        'Stock Number': '101',
        'Year': '2020',
        'Make': 'Ford',
        'Model': 'Fusion',
        'Series Name': 'SE',
        'Odometer': '113,666 mi',
        'Fuel Type': 'Gasoline',
        'Transmission Type': 'Automatic',
        'Drive Line Type': 'Front Wheel Drive',
        'Body Style': 'Sedan',
        'Current Bid': '$1,600 USD',
        'Vin#': 'ABC123XYZ'
    }
    vehicle = RowMapper.to_vehicle(row)
    assert isinstance(vehicle, Vehicle)
    assert vehicle.stock_number == 101
    assert vehicle.year == 2020
    assert vehicle.make == 'Ford'
    assert vehicle.model == 'Fusion'
    assert vehicle.series == 'SE'
    assert vehicle.mileage == 113666
    assert vehicle.fuel_type == FuelType.GASOLINE
    assert vehicle.transmission == TransmissionType.AUTOMATIC
    assert vehicle.drive_line == DriveLineType.FWD
    assert vehicle.body_style == BodyStyle.SEDAN
    assert vehicle.current_bid_usd == 1600
    assert vehicle.vin == 'ABC123XYZ'

def test_to_vehicle_missing_optional():
    row = {
        'Stock Number': '102',
        'Year': '2021',
        'Make': 'Honda',
        'Model': 'Accord',
        'Series Name': None,
        'Odometer': None,
        'Fuel Type': None,
        'Transmission Type': None,
        'Drive Line Type': None,
        'Body Style': None,
        'Current Bid': None,
        'Vin#': 'XYZ789ABC'
    }
    vehicle = RowMapper.to_vehicle(row)
    assert isinstance(vehicle, Vehicle)
    assert vehicle.series is None
    assert vehicle.mileage is None
    assert vehicle.fuel_type == FuelType.OTHER or vehicle.fuel_type is None
    assert vehicle.transmission == TransmissionType.UNKNOWN or vehicle.transmission is None
    assert vehicle.drive_line == DriveLineType.UNKNOWN or vehicle.drive_line is None
    assert vehicle.body_style == BodyStyle.OTHER or vehicle.body_style is None
    assert vehicle.current_bid_usd is None
    assert vehicle.vin == 'XYZ789ABC'

