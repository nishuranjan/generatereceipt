import csv
from datetime import date, datetime, timedelta
from utils.feedetails import (sendemail,
                              get_first_date_of_current_month,
                              get_last_date_of_month)
from utils.feetemplate import feetemplate
from uuid import uuid4
# from pyhtml2pdf import converter
import pdfkit


def generate(source, year, month):
    """"
    author: learningdhara.com
    creation date: 27-Aug-2023
    modified by: n/a
    modified on: n/a

    purpose : Generating the receipt
    """

    # fetch the fee template to email
    template = feetemplate()

    startdate = get_first_date_of_current_month(year, month)
    enddate = get_last_date_of_month(year, month)
    digitalsign = "N/A"

    # fee details dictionary
    with open(source, mode='r') as srcfee:
        feedetails = csv.DictReader(srcfee)

        for row in feedetails:
            name = row["Name"]
            receiptdate = str(row["Timestamp"])
            email = row["Email address"]
            classcat = row["Category"]
            mode = row["Payment Mode"]
            transactionid = row["Payment Id"]
            status = row["Fee Status"]
            amount = row["Aug 2023"]
            accountid = uuid4()

            html_output = "target/{0}.html".format(email)
            pdf_output = "target/{0}.pdf".format(email)

            # print("receiptdate = ", receiptdate)
            # print(template)

            # replace the template variable
            rep_template = template.format(receiptdate, status, transactionid,
                                           amount, name, email, "no-phone",
                                           accountid, classcat,
                                           startdate, enddate, digitalsign,
                                           mode)

            # print(rep_template)
            # # store in target path
            f = open(html_output, "w")
            f.write(rep_template)
            f.close()
            print("Writing output file to: " + html_output)

            # Convert html into pdf
            pdfkit.from_file(html_output, pdf_output,
                             options={"enable-local-file-access": ""})

            # Send Email
            # sendemail(email, pdf_output)


# It Allows You to Execute Code When the File Runs as a Script,
#   but Not When It’s Imported as a Module
# Python sets the global __name__ of a module equal to "__main__"
#   if the Python interpreter runs your code in the top-level code environment:
# https://docs.python.org/3/library/__main__.html#what-is-the-top-level-code-environment
# “Top-level code” is the first user-specified Python module
# that starts running.
#   It’s “top-level” because it imports all other modules
#       that the program needs
if __name__ == "__main__":
    source = "source/feedetails.csv"
    month = datetime.now().month
    year = datetime.now().year

    generate(source, year, month)
