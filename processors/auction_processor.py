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

    async def process_file(self, path: str) -> Tuple[Dict[Auction, List[Vehicle]], List[Vehicle]]:
        rows = await CSVLoader.load_async(path)
        auctions: Dict[Auction, List[Vehicle]] = {}
        all_vehicles: List[Vehicle] = []

        for row in rows:
            auction = RowMapper.to_auction(row)
            vehicle = RowMapper.to_vehicle(row)
            auctions.setdefault(auction, []).append(vehicle)
            all_vehicles.append(vehicle)

        return auctions, all_vehicles

    async def process_folder(self, folder_path: str) -> Tuple[Dict[Auction, List[Vehicle]], List[Vehicle]]:
        # pobierz wszystkie pliki CSV w folderze
        files = glob.glob(f"{folder_path}/*.csv")
        all_auctions: Dict[Auction, List[Vehicle]] = {}
        all_vehicles: List[Vehicle] = []

        # równoległe przetwarzanie wszystkich plików
        tasks = [self.process_file(f) for f in files]
        results = await asyncio.gather(*tasks)

        # połącz wyniki
        for auctions, vehicles in results:
            for auction, v_list in auctions.items():
                all_auctions.setdefault(auction, []).extend(v_list)
            all_vehicles.extend(vehicles)

        return all_auctions, all_vehicles
