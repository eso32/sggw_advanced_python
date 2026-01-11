import asyncio
from processors.auction_processor import AuctionProcessor

async def main():
    processor = AuctionProcessor()
    auctions, vehicles = await processor.process_folder('data')

    print(f"Liczba aukcji: {len(auctions)}")
    print(f"Liczba pojazdów: {len(vehicles)}")

    # przykład pierwszej aukcji
    first_auction = next(iter(auctions.items()))
    print("\nPrzykładowa aukcja:")
    print(first_auction[0])
    print(f"Pojazdy na aukcji: {len(first_auction[1])}")

if __name__ == "__main__":
    asyncio.run(main())
