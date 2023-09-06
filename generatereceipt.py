
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
    # retrieve fee details without using csv reader
    fee_details = get_fee_details_without_csv_reader(file_path)
    
    # retrieve fee details using csv reader
    # fee_details = get_fee_details_with_csv_reader(file_path)
    # pp(fee_details)
    
    # get absolute path of icon
    icon_path =  path.abspath("./images/2452184.png")
    for fee_data in fee_details:
        
        # get absolute path of file being created
        file_path = path.abspath(f"./receipts/html/{fee_data['email']}.html")
        
        # get the html template string by passing fee details and icon path of each file 
        content = feetemplate(fee_data, icon_path)
        
        # write html string to file
        write_html_receipt(file_path, content)

# ensure that file being executed from command line  
# can be imported as module also      
if __name__ == '__main__':
    # passing relative path of csv file
    generate('./source/feedetails.csv')
