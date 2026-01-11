import csv
import asyncio
from typing import List, Dict

class CSVLoader:
    @staticmethod
    async def load_async(path: str) -> List[Dict[str, str]]:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, CSVLoader._load_sync, path)

    @staticmethod
    def _load_sync(path: str) -> List[Dict[str, str]]:
        with open(path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
