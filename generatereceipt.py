import datetime
from utils.feedetails import (readfeedetails,
                              storefeedetails,
                              sendemail,
                              audittrails)
from utils.feetemplate import feetemplate


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
    template = feetemplate()
