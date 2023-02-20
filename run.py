import gspread
from google.oauth2.service_account import Credentials
import plotext as plt
import numpy as np

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('data_treatment')


def get_raw_data():
    """
    Get Raw figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of x numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter raw data from the last spectrum.")
        print("Data should be six numbers, separated by commas.")
        print("Example: Sample, 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        raw_data = data_str.split(",")

        if validate_data(raw_data):
            print("Data is valid!")
            break

    return raw_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        for value in values[1:]:
            int(value[1:])
            print(value)
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_integration_area(integration_row):
    """
    Calculates the area under the graph for entire region and calculations
    """
    print("Calculating integration data...\n")
    integration_data = SHEET.worksheet("Raw_Data").get_all_values()
    
    data_after = {e[0]: e[1:] for e in integration_data}
    
    xdata = data_after['Wavenumbers']
    
    ydata = data_after[list(data_after)[-1]]
    
    xdata = [int(i) for i in xdata]
    ydata = [int(i) for i in ydata]
    integration_row = []
    total_int = np.trapz(ydata, xdata)
    integration_row.append(total_int)

    xdata_int_1 = xdata[0:2]
    ydata_int_1 = ydata[0:2]

    partial_int = np.trapz(ydata_int_1, xdata_int_1)

    integration_row.append(partial_int)

    xdata_int_2 = xdata[2:5]
    ydata_int_2 = ydata[2:5]
    partial_int_2 = np.trapz(ydata_int_2, xdata_int_2)
    integration_row.append(partial_int_2)

    return integration_row


def calculate_ratio(Calculated_index):
    """
    Calculate the ratio index for each item type
    """
    print("Ratio index")
    Calculated_index = []
    integration_data = SHEET.worksheet("Integrated_Data").get_all_values()   
    data = integration_data[-1]
    int1 = int(data[0])
    int2 = int(data[1])
    int3 = int(data[2])
    
    Ratio1 = int2/int1
    Calculated_index.append(Ratio1)
    Ratio2 = int3/int1
    Calculated_index.append(Ratio2)
    Ratio3 = (int2+int3)/int1
    Calculated_index.append(Ratio3)

    return Calculated_index


def ratio_evaluation():
    ratio_data = SHEET.worksheet("Calculation_index").get_all_values()
    headers = ratio_data[0]
    
    header1 = headers[0]
    header2 = headers[1]
    header3 = headers[2]  
    data = ratio_data[-1]
    
    High_Limit = 10
    Low_Limit = 0
    High_index = 5
    Medium_index = 3
    Low_index = 1

    for i in range(len(data)):
        data[i] = data[i].replace(",", ".")
    
    ratio1 = float(data[0])
    ratio2 = float(data[1])
    ratio3 = float(data[2])
    

    if ratio1 > High_Limit:
        print("okay")
    elif ratio1 > High_index:
        print(f"{header1} seems to be quite high")
    elif ratio1 > Medium_index:
        print(f"{header1} seems to be quite normal")
    elif ratio1 > Low_index:
        print(f"{header1} seems to be quite low")
    elif ratio1 < Low_index:
        print(f"{header1} seems to be Very low")
    elif ratio1 < Low_Limit: 
        print(f"{header1} is negative please remeasure")
        get_raw_data()
    else:
        print("oops something went wrong")
        get_raw_data()
        
    data_evaluation = {}
    for header in headers:
        for value in data:
            data_evaluation[header] = value
            data.remove(value)
            break
    print("Resultant dictionary is : " + str(data_evaluation))
    return data_evaluation
    
def plot_generation():
    
    integration_data = SHEET.worksheet("Raw_Data").get_all_values()
    
    data_after = {e[0]: e[1:] for e in integration_data}
    
    xdata = data_after['Wavenumbers']
    
    ydata = data_after[list(data_after)[-1]]

    x = xdata
    y = ydata
    print(y)
    print(x)
    plt.plot(y)
    plt.title("Scatter Plot")
    plt.show()


def main():
    """
    Run all program functions
    """
    data = get_raw_data()
    raw_data = [num for num in data]
    update_worksheet(raw_data, "Raw_Data")
    integrated_data = calculate_integration_area(raw_data)
    update_worksheet(integrated_data, "Integrated_Data")
    ratio_data = calculate_ratio(integrated_data)
    update_worksheet(ratio_data, "Calculation_index")
    ratio_evaluation()
    #plot_generation()


print("Welcome to Spectral Data Automation")
main()

