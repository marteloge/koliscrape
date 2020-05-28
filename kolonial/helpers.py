import datetime


def get_logo():
    return (
        " _  __     _             _       _ \n"
        + "| |/ /___ | | ___  _ __ (_) __ _| |\n"
        + "| ' // _ \| |/ _ \| '_ \| |/ _` | |\n"
        + "| . \ (_) | | (_) | | | | | (_| | |\n"
        + "|_|\_\___/|_|\___/|_| |_|_|\__,_|_|\n"
    )


def get_file_name():
    date = datetime.datetime.now()
    return (
        str(date.year)
        + "-"
        + str(date.month)
        + "-"
        + str(date.day)
        + "_all_products.json"
    )


def print_product(product):
    print(" - ", product["title"], " - ", product["price"], product["currency"])
