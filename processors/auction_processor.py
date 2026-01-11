from typing import Dict, List, Tuple
from models.auction import Auction
from models.vehicle import Vehicle
from services.csv_loader import CSVLoader
from services.row_mapper import RowMapper
import asyncio
from concurrent.futures import ThreadPoolExecutor
import glob

class AuctionProcessor:
    def __init__(self):
        self.executor = ThreadPoolExecutor()

    async def process_file(self, path: str) -> Tuple[List[Auction], List[Vehicle]]:
        rows = await CSVLoader.load_async(path)
        auction_map: Dict[Tuple, Auction] = {}
        all_vehicles: List[Vehicle] = []

        for row in rows:
            temp_auction = RowMapper.to_auction(row)
            vehicle = RowMapper.to_vehicle(row)

            auction_key = (temp_auction.auction_date, temp_auction.branch_name, temp_auction.region)

            if auction_key not in auction_map:
                new_auction = Auction(
                    auction_date=temp_auction.auction_date,
                    branch_name=temp_auction.branch_name,
                    region=temp_auction.region
                )
                auction_map[auction_key] = new_auction
            
            auction_map[auction_key].vehicles.append(vehicle)
            all_vehicles.append(vehicle)

        return list(auction_map.values()), all_vehicles

    async def process_folder(self, folder_path: str) -> Tuple[List[Auction], List[Vehicle]]:
        files = glob.glob(f"{folder_path}/*.csv")
        all_auctions_map: Dict[Tuple, Auction] = {}
        all_vehicles: List[Vehicle] = []

        tasks = [self.process_file(f) for f in files]
        results = await asyncio.gather(*tasks)

        for auctions_from_file, vehicles_from_file in results:
            all_vehicles.extend(vehicles_from_file)
            for auction_obj in auctions_from_file:
                auction_key = (auction_obj.auction_date, auction_obj.branch_name, auction_obj.region)
                if auction_key not in all_auctions_map:
                    all_auctions_map[auction_key] = auction_obj
                else:
                    all_auctions_map[auction_key].vehicles.extend(auction_obj.vehicles)

        return list(all_auctions_map.values()), all_vehicles
