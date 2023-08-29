from utils.feedetails import readfeedetails
from utils.feetemplate import createtemplate


def generate():
    """"
    author: learningdhara.com
    creation date: 27-Aug-2023
    modified by: n/a
    modified on: n/a

    purpose : Generating the receipt
    """

    # fee details dictionary
    feedetails = readfeedetails("source/feedetails.csv")

    # replace the template variable
    output = createtemplate()
