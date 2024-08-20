from data_extraction import data_extraction

def data_analysis():
    daily, weekly, monthly=data_extraction()
#    print("daily :",daily)
#    print("weekly :",weekly)
#    print("monthly :",monthly)
    merged_data = daily.merge(weekly, how='outer', left_index=True, right_index=True, suffixes=('_daily', '_weekly'))
    merged_data = merged_data.merge(monthly, how='outer', left_index=True, right_index=True, suffixes=('', '_monthly'))
    merged_data.fillna(method='ffill', inplace=True)
    print(merged_data.head())
    print(merged_data.tail())
    print(merged_data.describe())
    print ("Missing values\n\n",merged_data.isnull().any(),sep='')
    print (merged_data.info())
    return merged_data

data_analysis() 