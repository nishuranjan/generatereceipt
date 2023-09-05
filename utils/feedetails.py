import csv
from datetime import datetime
from utils.utils import get_uuid, last_day_of_month

variable_mapping = {
    'Timestamp': 'receiptdate',
    'Fee Status': 'status',
    'Payment Id': 'transactionid',
    'Payment Mode': 'mode',
    'Aug 2023': 'amount',
    'Name': 'name',
    'Email address': 'email',
    'Category': 'classcat',
    # 'Aug 2023': 'startdate',
    #'Aug 2023': 'enddate',
    # 'sign': 'digitalsign',
      # 'Phone': 'phone',
    # 'uuid': 'accountid',
}

def get_fee_details_without_csv_reader(file_path: str):
    """_summary_
    Args:
        file_name (str): _description_
    """
    fees_data = []
    # opening file
    with open(file_path, 'r', -1, "utf-8") as file:
        headers = []
        row_count = 0
        # Reading csv line by line
        for row in file:
            record = {}
            row_count += 1
            row = row.strip()
            if row_count == 1:
                headers = row.split(',')
                print(headers)
                continue
            details = row.split(',')
            print(details)
            for i, value in enumerate(details):
                record[variable_mapping[headers[i]]] = value
            
            date_of_payment =  datetime.strptime('Aug 2023', '%b %Y')
            record['startdate'] = date_of_payment.strftime('%d/%m/%Y')
            record['enddate'] = last_day_of_month(date_of_payment).date().strftime('%d/%m/%Y')
            record['accountid'] = get_uuid()
            record['digitalsign'] = 'digital sign'
            record['phone'] = '1234567'
            fees_data.append(record)
            
        file.close()
    return fees_data


def get_fee_details_with_csv_reader(file_path: str):
    """_summary_
    Args:
        file_name (str): _description_
    """
    fees_data = []
    
    # opening file
    with open(file_path, 'r', -1, "utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
    
        # Reading csv line by line
        for row in reader:
            record = {}
            for i, value in enumerate(row):
                record[variable_mapping[headers[i]]] = value   
            date_of_payment =  datetime.strptime('Aug 2023', '%b %Y')
            record['startdate'] = date_of_payment.strftime('%d/%m/%Y')
            record['enddate'] = last_day_of_month(date_of_payment).date().strftime('%d/%m/%Y')
            record['accountid'] = get_uuid()
            record['digitalsign'] = 'digital sign'
            record['phone'] = '1234567'
            fees_data.append(record)
            
        file.close()
    return fees_data
   
def sendemail():
    return True

def audittrails():
    return True
