import pandas as pd

def data_extraction():
    daily = pd.read_csv("/home/ubuntu/Object_detection_FCOS/Drugsales/salesdaily.csv")
    weekly = pd.read_csv("/home/ubuntu/Object_detection_FCOS/Drugsales/salesweekly.csv")
    monthly = pd.read_csv("/home/ubuntu/Object_detection_FCOS/Drugsales/salesmonthly.csv")
    print("daily :",daily)
    print("weekly :",weekly)
    print("monthly :",monthly)
    
    #converting datatype of dates from object to Datetime
    monthly['datum'] = pd.to_datetime(monthly['datum'], format= '%Y-%m-%d')
    weekly['datum'] = pd.to_datetime(weekly['datum'], format= '%m/%d/%Y')
    daily['datum'] = pd.to_datetime(daily['datum'], format= '%m/%d/%Y')
    
    print("daily :",monthly['datum'])
    print("weekly :",weekly['datum'])
    print("monthly :",daily['datum'])
    
    monthly['year'] = monthly['datum'].dt.year
    monthly['month'] = monthly['datum'].dt.month
    monthly['day'] = monthly['datum'].dt.day
    
    print("daily :",monthly['datum'])
    print("weekly :",weekly['datum'])
    print("monthly :",daily['datum'])
    
    return daily, weekly, monthly
    
data_extraction()

