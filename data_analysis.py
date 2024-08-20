from data_extraction import data_extraction

def data_analysis():
    monthly=data_extraction()
    print("monthly :",monthly)
    print(monthly.head())
    print(monthly.tail())
    print(monthly.describe())
    print ("Missing values\n\n",monthly.isnull().any(),sep='')
    print (monthly.info())
    return monthly

data_analysis() 
