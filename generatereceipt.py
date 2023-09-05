import datetime
from utils.feedetails import (get_fee_details_with_csv_reader, get_fee_details_without_csv_reader)
from utils.feetemplate import feetemplate
from utils.utils import write_html_receipt
from pprint import pprint as pp
from os import path

def generate(file_path: str):
    """"
    author: learningdhara.com

    creation date: 27-Aug-2023
    modified by: n/a
    modified on: n/a

    purpose : Generating the receipt
    """
    # fee details dictionary
    fee_details = get_fee_details_without_csv_reader(file_path)
    # fee_details = get_fee_details_with_csv_reader(file_path)
    #pp(fee_details)
    
    # replace the template variable
    icon_path =  path.abspath(f"./images/2452184.png")
    for fee_data in fee_details:
        file_path = path.abspath(f"./receipts/html/{fee_data['email']}.html")
        content = feetemplate(fee_data, icon_path)
        write_html_receipt(file_path, content)
           
if __name__ == '__main__':
    generate('./source/feedetails.csv')
