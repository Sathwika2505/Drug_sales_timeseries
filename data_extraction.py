import pandas as pd

def data_extraction():
    monthly = pd.read_csv("/home/ubuntu/Object_detection_FCOS/Drugsales/salesmonthly.csv")
    print("monthly :",monthly)
    monthly['datum'] = pd.to_datetime(monthly['datum'], format= '%Y-%m-%d')
    
    print("daily :",monthly['datum'])
    monthly['month'] = monthly['datum'].dt.month
    
    print("daily :",monthly['datum'])
    
    return monthly
    
data_extraction()

