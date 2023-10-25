import csv
from datetime import datetime

PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
REQUEST_QUANTITY_INDEX = 1
PRODUCT_PRICE_INDEX = 2


def main():
    print("\n                                   🍉🥛REALLY-FRESH GROCERY STORE🥐🥕                               \n")
    try:
        products_dict = read_dict("products.csv", PRODUCT_KEY_INDEX)
    except FileNotFoundError as file_err:
        print()
        print(type(file_err).__name__, file_err, sep=": ")
        print(f"The file doesn't exist.")
    else:
        the_date = datetime.now()
        print(products_dict)
        num_of_items = 0
        sub_total = 0
        print("\nRequested Items")
        try:
            with open("request.csv") as data_file:
                data = csv.reader(data_file)
        except FileNotFoundError as file_err:
            print()
            print(type(file_err).__name__, file_err, sep=": ")
            print(f"The file doesn't exist.")

        except PermissionError as perm_err:
            print()
            print(type(perm_err).__name__, perm_err, sep=": ")
            print(f"The file doesn't exist.")

        else:
            with open("request.csv") as data_file:
                data = csv.reader(data_file)
                next(data)

                for unique_num in data:
                    key = unique_num[PRODUCT_KEY_INDEX]
                    try:
                        product_name = products_dict[key][PRODUCT_NAME_INDEX]
                        the_quantity = int(unique_num[REQUEST_QUANTITY_INDEX])
                        product_price = products_dict[key][PRODUCT_PRICE_INDEX]
                    except KeyError as key_err:
                        print()
                        print(type(key_err).__name__, key_err, sep=": ")
                        print(f"The {key_err} key doesn't exist.\n")
                    else:
                        print(f"{product_name}: {the_quantity} at ${product_price}")

                        num_of_items += the_quantity
                        sub_total += float(product_price) * the_quantity

                sale_tax = round(sub_total * 0.06, 2)
                total_price = sub_total + sale_tax

                print("                     Your Receipt            ")
                print(f"Number of Items: {num_of_items}     \t      Subtotal: {sale_tax:.2f}")
                print(f"Sales Tax: {sale_tax}      \t     Total: {total_price:.2f}\n")

                print(f"Thank you for shopping at 🍉🥛REALLY-FRESH GROCERY STORE🥐🥕 \n"
                      f"{the_date.strftime('%a %b %d')} \t {the_date.strftime('%I:%M:%S %p')}")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dict = {}

    with open(filename) as f:
        the_data = csv.reader(f)
        next(the_data)
        for rows in the_data:
            the_key = rows[key_column_index]
            product_dict[the_key] = rows

        return product_dict


if __name__ == '__main__':
    main()
