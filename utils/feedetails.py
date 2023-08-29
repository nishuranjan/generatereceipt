import csv


def readfeedetails(source: str):
    """
    reading the fee details csv file
    parameter: source
    """

    with open(source, mode='r') as srcfee:
        csv_reader = csv.DictReader(srcfee)

        return csv_reader


def storefeedetails(target: str):
    """
    writing the fee details pdf in target folder
    parameter: pdf
    """

    return True


def sentemail():

    return True
