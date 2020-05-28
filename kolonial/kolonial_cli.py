import argparse

from helpers import get_logo
from args import arg_search, arg_products, arg_id, arg_all


def main():
    parser = argparse.ArgumentParser(description="Kolonial produktkatalog")
    parser.add_argument("--all", help="Lister alle produkter", action="store_true")
    parser.add_argument("--search", type=str, help="Søk i alle produkter")
    parser.add_argument("--id", help="Finn produkt for produktID")
    parser.add_argument(
        "--products",
        type=int,
        help="Bla gjennom produktkatalog (20 produkter om gangen)",
    )
    parser.add_argument(
        "--price",
        type=int,
        help="Finn produkt med prisintervall med å sende med min og max",
    )

    args = parser.parse_args()

    if args.search:
        arg_search(args)
    elif args.products:
        arg_products(args)
    elif args.price:
        print("MAX PRICE", args.price)
    elif args.id:
        arg_id(args)
    elif args.all:
        arg_all(args)
    else:
        print(get_logo())
        print("\nVelkommen til kolonials produktkatalog! \n")
        print(" > Jeg heter koliscrape og jeg er din hjelper!")
        print(" > Har du noen spørsmål ang produktkatalogen til Kolonial?")
        print("   (For å se hva jeg kan hjelpe deg med kan du sjekke ut --help) \n")


if __name__ == "__main__":
    main()
