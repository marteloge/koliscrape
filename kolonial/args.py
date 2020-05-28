import math

from time import sleep

from products import get_products
from helpers import get_file_name, print_product


def arg_search(args):
    print(
        f"\n > Vi skal se om vi kan finne produkt som matcher søkeordet ditt '{args.search}'..."
    )
    search = args.search
    products = get_products()

    result = [
        product
        for product in products
        if str(search).lower() in product["title"].lower()
        or str(search).lower() in product["description"].lower()
    ]

    if len(result) > 0:
        amount = len(result)

        print(
            "\n > YAY! Jeg fikk "
            + (" et treff " if amount == 1 else f"{amount} treff ")
            + "med ditt søkeord '"
            + search
            + "'\n"
        )

        for product in result:
            print_product(product)

        print("\n > (Søk tok utgangspunkt produktets beskrivelse og tittel) \n")

    else:
        print("\n > Beklager, jeg fant ikke noe produkt med å søke på {args.search} :(")


def arg_products(args):
    print(
        f"\n > La oss se om vi kan finne produktene på side {args.products} i produktkatalogen..."
    )

    page = args.products
    products = get_products()
    start = (page - 1) * 20

    if page < 1 or type(page) is not int:
        print("\n > Beklager, sidetall starter fra 1 og må være et heltall")
    elif start > len(products):
        print(
            f"\n Beklager, vi har bare { math.floor(len(products) / 20)} produktsider!"
        )
    else:
        print(f"\n > Her er produktene på side {page}:\n")
        for product in products[start : start + 20]:
            print_product(product)

        if (page * 20 + 20) < len(products):
            print(
                "\n > Se flere produkter? Gå til neste produktside --products"
                + f" { page + 1 } (totalt { math.floor(len(products) / 20)} sider) \n"
            )
        else:
            print(f"\n > Dette var siste produktside! \n")


def arg_id(args):
    print(
        f"\n > La oss se om vi kan finne produkt med id {args.id} i produktkatalogen..."
    )
    products = get_products()

    results = [
        product
        for product in products
        if product["url"] is not None and str(args.id) in product["url"]
    ]

    if len(results) > 0:
        print(f"\n > Yay - vi fant produkt med id {args.id}\n")
        for product in results:
            print_product(product)
        print("\n")
    else:
        print(f"\n > Beklager - fant ikke produkt med id {args.id}.\n")


def arg_all(args):
    products = get_products()

    print("\n > Jeg skal finne frem alle produktene for deg :)")
    sleep(1)

    print(f"\nHer er alle produkter ({len(products)}):")

    for product in products:
        print_product(product)

    print("\n > Det var alt! \n")
