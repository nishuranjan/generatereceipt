import csv
from datetime import datetime
from utils.utils import get_uuid, last_day_of_month

mapping = {
    'Timestamp': 'receiptdate',
    'Fee Status': 'status',
    'Payment Id': 'transactionid',
    'Payment Mode': 'mode',
    'Aug 2023': 'amount',
    'Name': 'name',
    'Email address': 'email',
    'Category': 'classcat',
}

def get_fee_details_without_csv_reader(file_path: str):
    """ retrive csv file data in form of dictionary using normal file operation, without using csv module

    Args:
        file_path (str): csv file path

    Returns:
        list : list of records of fee payment
    """
    fees_data = []
    # opening file
    with open(file_path, 'r', -1, "utf-8") as file:
        # headers = file.readline().strip().split(',')
        headers = next(file).strip().split(',')
        # Reading csv line by line
        for row in file:
            record = row.strip().split(',')
            
            # using dictionary comprehension
            record = {mapping[headers[i]] : value  for i, value in enumerate(record)}
            
            #Addition key value
            date_of_payment =  datetime.strptime('Aug 2023', '%b %Y')
            record = record | {
                'startdate': date_of_payment.strftime('%d/%m/%Y'),
                'enddate' : last_day_of_month(date_of_payment).date().strftime('%d/%m/%Y'),
                'accountid' : get_uuid(),
                'digitalsign' : 'digital sign',
                'phone' : '1234567',
            }
            fees_data.append(record)
            
        file.close()
    return fees_data


def get_fee_details_with_csv_reader(file_path: str):
    """ retrive csv file data in form of dictionary using csv module

    Args:
        file_path (str): csv file path

    Returns:
        list : list of records of fee payment
    """
    fees_data = []
    
    # opening file
    with open(file_path, 'r', -1, "utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
    
        # Reading csv line by line
        for row in reader:
            # with dictionary comprehension
            record = {mapping[headers[i]] : value  for i, value in enumerate(row)}
            
            #Addition key value
            date_of_payment =  datetime.strptime('Aug 2023', '%b %Y')
            record = record | {
                'startdate': date_of_payment.strftime('%d/%m/%Y'),
                'enddate' : last_day_of_month(date_of_payment).date().strftime('%d/%m/%Y'),
                'accountid' : get_uuid(),
                'digitalsign' : 'digital sign',
                'phone' : '1234567',
            }
            fees_data.append(record)
        file.close()
    return fees_data
   
def sendemail():
    return True

def audittrails():
    return True
