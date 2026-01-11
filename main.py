import asyncio
from processors.auction_processor import AuctionProcessor

async def main():
    processor = AuctionProcessor()
    auctions, vehicles = await processor.process_folder('data')

    print(f"Liczba aukcji: {len(auctions)}")
    print(f"Liczba pojazdów: {len(vehicles)}")

    # przykład pierwszej aukcji
    first_auction = auctions[0] if auctions else None
    if first_auction:
        print("\nPrzykładowa aukcja:")
        print(f"Data aukcji: {first_auction.auction_date}, Oddział: {first_auction.branch_name}, Region: {first_auction.region}")
        print(f"Pojazdy na aukcji: {len(first_auction.vehicles)}")

if __name__ == "__main__":
    asyncio.run(main())
