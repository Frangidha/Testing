import gspread
from google.oauth2.service_account import Credentials
import numpy as np
import plotext
import time
"""
the app is connected via API to google sheets for easy access to 
the old data. Secondly for a data control perspective to find back the data 
in case of an audit. it is split in 3 sheets to easily see 
each manipulation of the data.    
"""
# How to check if the values 
# Plot parameters - scatterplot
x_axes = "Wavenumbers (1/cm)"
y_axes = "Absorbance"
# Integration limit variable 
int_limit1 = 798.892
int_limit2 = 1688.416
int_limit3 = 1896.809
# how to set your limit variables to get the requested comments
high_limit = 10
low_limit = 0
high_value = 5
low_value = 1
medium_value = 3

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('data_treatment')


def launch_raw_data():
    """
    Get Raw figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the API in google sheets, which must be a string of x numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter raw data in the google drive form.")
        print("Data should be the same range as the other samples\n")
        print("Put the Data in the googe sheets using this file: ")
        print("https://docs.google.com/spreadsheets/d/1cEWBDHZ35fzQ320SUUwLCcgsBtijk0C3keXW9kgA0Uc/edit#gid=0\n")
        print("Example:")
        print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("A", "B", "C", "D", "..."))
        print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("Sample", 10, 20, 30, "...\n"))
        confirmation = input("have you put in your data please confirm by typing 'x': ")

        if validate_drive_data(confirmation):
            print("Data is valid!")
            break


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
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_drive_data(confirmation):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        # see loop_data function for explanation 
        old_data, new_data, range_data, loop = loop_data()
        if confirmation == 'x':
            raw_data = SHEET.worksheet("Raw_Data")
            # checks if new-data is added           
            if old_data < new_data:
                data_array = []
                lenght_data = []
                for ind in range(1, range_data):
                    column = raw_data.row_values(ind)
                    data_array.append(column[1:])
                    # checks if the data does not contain any strings
                    data_array = [[s.replace(',', '') for s in group]for group in data_array]
                    [[float(value) for value in group] for group in data_array]
                for x in data_array:
                    # add the lenght to the data_array
                    jls_extract_var = lenght_data
                    jls_extract_var.append(len(x))

                highest_value_input = max(lenght_data)
                lowest_value_input = min(lenght_data)
                if highest_value_input != lenght_data[0]:
                    raise ValueError(f"too many data points({highest_value_input})")
                elif lowest_value_input != lenght_data[0]:
                    raise ValueError(f"not enough data points({lowest_value_input})")
            else:
                raise ValueError("did you add new Data?\n")
                
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


def calculate_integration_area(sample, intLim1, intLim2, intLim3):
    """
    Calculates the area under the graph for entire region and calculations

    the numpy library uses the composite trapezoidal rule
    The composite trapezoidal rule is a method for 
    approximating a definite integral 
    by evaluating the integrand at n points.
    Let [a,b] be the interval of integration with a partition a=x0<x1<…<xn=b.
    more info: https://planetmath.org/compositetrapezoidalrule
    """
    
    print("Calculating integration data...\n")
    integration_data = SHEET.worksheet("Raw_Data").get_all_values()
    # convert into floats
    data_after = {e[0]: e[1:] for e in integration_data}
    xdata = data_after['Wavenumbers']
    xdata = [s.replace(',', '') for s in xdata]
   
    
    ydata = data_after[sample]
    ydata = [s.replace(',', '') for s in ydata]
    
    xdata = [float(i) for i in xdata]
    ydata = [float(i) for i in ydata]
    
    # search for the integration index of the selected values for partial integration.
    integration_border_One = xdata.index(intLim1)
    integration_border_Two = xdata.index(intLim2)
    integration_border_Three = xdata.index(intLim3)

    integration_row = []
    total_int = np.trapz(ydata, xdata)
    # integrate the entire data-set
    integration_row.append(total_int)
    # integrate the entire data-set
    xdata_int_1 = xdata[integration_border_Two:integration_border_Three]
    ydata_int_1 = ydata[integration_border_Two:integration_border_Three]
    partial_int = np.trapz(ydata_int_1, xdata_int_1)

    integration_row.append(partial_int)

    xdata_int_2 = xdata[integration_border_One:integration_border_Two]
    ydata_int_2 = ydata[integration_border_One:integration_border_Two]
    partial_int_2 = np.trapz(ydata_int_2, xdata_int_2)
    integration_row.append(partial_int_2)

    return integration_row


def calculate_ratio(Calculated_index, Sample):
    """
    Calculate the ratio index for each item type. 
    getting the integration values from google sheet 
    calculated by the previous function
    Use of division and addition
    """
    
    Calculated_index = []
    integration_data = SHEET.worksheet("Integrated_Data").get_all_values()   
    data = integration_data[-1]
    data = [s.replace(',', '') for s in data]

    int1 = float(data[0])
    int2 = float(data[1])
    int3 = float(data[2])

    Calculated_index.append(Sample)
    Ratio1 = int2/int1
    Calculated_index.append(Ratio1)
    Ratio2 = int3/int1
    Calculated_index.append(Ratio2)
    Ratio3 = (int2+int3)/int1
    Calculated_index.append(Ratio3)

    return Calculated_index


def ratio_evaluation(Sample, High_Limit, Low_Limit, High_index, Medium_index, Low_index):

    """
    it takes the calculated data afterwards it give 
    comments on this ratio and give recommendation or if 
    the Data is not possible repeats the programma
    """
    ratio_data = SHEET.worksheet("Calculation_index").get_all_values()
    headers = ratio_data[0]
    # get the headers for the table 
    header = headers[0]
    header1 = headers[1]
    header2 = headers[2]
    header3 = headers[3]  
    data = ratio_data[-1]

    for i in range(len(data)):
        data[i] = data[i].replace(",", ".")
    
    ratio1 = float(data[1])
    ratio2 = float(data[2])
    ratio3 = float(data[3])
    print("Calculated Data Table:\n")
    # the date table 
    print("{:<15} {:<15} {:<15} {:<15}".format(header, header1, header2, header3))
    print("{:<15} {:<15} {:<15} {:<15}".format(Sample, round(ratio1, 3), round(ratio2, 3), round(ratio3, 3)))
    
    print("")
    print("Data Interpretation:")
    # comments to each ratio regarding the set limits
    if ratio1 > High_Limit:
        print(f"{header1} seems to be outside the expected range\n")
    elif ratio1 > High_index:
        print(f"{header1} seems to be quite high\n")
    elif ratio1 > Medium_index:
        print(f"{header1} seems to be quite normal\n")
    elif ratio1 > Low_index:
        print(f"{header1} seems to be quite low\n")
    elif ratio1 < Low_index:
        print(f"{header1} seems to be Very low\n")
    elif ratio1 < Low_Limit: 
        print(f"{header1} is negative please remeasure\n")
        get_raw_data()
    else:
        print("oops something went wrong")
        get_raw_data()
    
    if ratio2 > High_Limit:
        print(f"{header2} seems to be outside the expected range\n")
    elif ratio2 > High_index:
        print(f"{header2} seems to be quite high\n")
    elif ratio2 > Medium_index:
        print(f"{header2} seems to be quite normal\n")
    elif ratio2 > Low_index:
        print(f"{header2} seems to be quite low\n")
    elif ratio2 < Low_index:
        print(f"{header2} seems to be Very low\n")
    elif ratio2 < Low_Limit: 
        print(f"{header2} is negative please remeasure\n")
        get_raw_data()
    else:
        print("oops something went wrong")
        get_raw_data()
    
    if ratio3 > High_Limit:
        print(f"{header3} seems to be outside the expected range\n")
    elif ratio3 > High_index:
        print(f"{header3} seems to be quite high\n")
    elif ratio3 > Medium_index:
        print(f"{header3} seems to be quite normal\n")
    elif ratio3 > Low_index:
        print(f"{header3} seems to be quite low\n")
    elif ratio3 < Low_index:
        print(f"{header3} seems to be Very low\n")
    elif ratio3 < Low_Limit: 
        print(f"{header3} is negative please remeasure")
        get_raw_data()
    else:
        print("oops something went wrong")
        get_raw_data()
    
    return header1, header2, header3
    

def raw_data_plot_generation(title, xlabel, ylabel):

    """
    This function will take the Raw Data values and plot them in graph to give a visual representation. 

    """

    print("The plot is generating, it will generate in a couple of seconds...\n")
    integration_data = SHEET.worksheet("Raw_Data").get_all_values()
    
    data_after = {e[0]: e[1:] for e in integration_data}
    # turn data form string to float
    xdata = data_after['Wavenumbers']
    xdata = [s.replace(',', '') for s in xdata]
    xdata = [float(i) for i in xdata]
    ydata = data_after[title]
    ydata = [s.replace(',', '') for s in ydata]
    ydata = [float(i) for i in ydata]
    # plot the raw spectrum
    plotext.scatter(xdata, ydata)
    plotext.title(f"Spectrum of {title}")
    plotext.xlabel(xlabel)
    plotext.ylabel(ylabel)
    plotext.show()
    plotext.clear_figure()


def get_sample_name(ind):
    """
    get the name of the sample taht is being calculated.
    """

    Sample_Name = SHEET.worksheet("Raw_Data")
    sample_column = Sample_Name.col_values(1)
    sample = sample_column[-abs(ind)]
    return sample


def get_last_5_entires_ratio_values():
    """
    Collect columns of data from calculation worksheet.
    Get the last 5 entries for each sample and return the data
    as a list of lists.
    """

    Ratio_data = SHEET.worksheet("Calculation_index")

    Ratio_data_array = []
    for ind in range(1, 5):
        column = Ratio_data.col_values(ind)
        Ratio_data_array.append(column[-5:])
    
    Data_list_1 = []
    for ind in range(0, 5):
        column = Ratio_data_array[0][ind]
        Data_list_1.append(column)
    Data_list_2 = []
    for ind in range(0, 5):
        column = Ratio_data_array[1][ind]
        Data_list_2.append(column)
    Data_list_3 = []
    for ind in range(0, 5):
        column = Ratio_data_array[2][ind]
        Data_list_3.append(column)
    Data_list_4 = []
    for ind in range(0, 5):
        column = Ratio_data_array[3][ind]
        Data_list_4.append(column)
    return Data_list_1, Data_list_2, Data_list_3, Data_list_4
    

def plot_barchart(samples, data, ratio):

    """
    take al the Data and combine them to make the plot of the last 
    5 entries to see the evolution of trends
    """
    print(f"{ratio} is being generated\n")
    data_replace = [s.replace(',', '.') for s in data]
    data_barchart = list(map(float, data_replace))
    plotext.plotsize(100, 30)
    plotext.bar(samples, data_barchart)
    plotext.title(ratio)
    plotext.show()
    plotext.clear_figure()


def Test_Data():
    """
        the Data was tested using https://www.integral-calculator.com/ and integration by hand. 
        this function is made to quickly check and compared the values using a set of know values using the trap integration from the numpy library.
    """
    # linear function Data
    xdata1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
    ydata1 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]
    # exponential function Data
    xdata2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
    ydata2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
    int_test1 = np.trapz(ydata1, xdata1)
    int_test2 = np.trapz(ydata2, xdata2)
    deviation = int_test2/151144859
    Low_Limit = 0.95
    High_Limit = 1.05
    if (int_test1 == 646000):
        # exponential function Data instead of a absolute value it is ratio that checks that the data doesn't deviate 5%. otherwise it will display a fault message.
        if (deviation > Low_Limit):
            print("the linear integration is the same as the calculated value")
            if (deviation < High_Limit):
                print("the exponential integration is within the range")
        else: 
            print("please check the programme and the integration values")
    else: 
        print("please check the programme")


def loop_data():
    """
    This code is used to check the Raw_Data sheet if the data input is correct. it checks if new data was added compared to the already existing data.
    Secondly it will check if the length of data input is correct of each row. this Data is also used for the value and Sample input value to know where to start. 
    """
    raw_data = SHEET.worksheet("Raw_Data").get_all_values()
    integration_data = SHEET.worksheet("Integrated_Data").get_all_values()
    new_data = len(raw_data)
    old_data_rows = len(integration_data)
    range_data = int(new_data) + 1 
    loop = new_data - old_data_rows
        
    return old_data_rows, new_data, range_data, loop


def main():
    """
    Run all program functions
    """
    launch_raw_data()
    old_data, new_data, range_data, loop = loop_data()
    x = loop
    # in case you want to change input method
    # activate the following 3 functions
    # data = get_raw_data()
    # raw_data = [num for num in data]
    # update_worksheet(raw_data, "Raw_Data")
    for ind in reversed(range(loop)):
        Sample = get_sample_name(x)
        
        raw_data_plot_generation(Sample, x_axes, y_axes)
    # Integration borders can be changed regarding your specifications 
        integrated_data = calculate_integration_area(Sample, int_limit1, int_limit2, int_limit3)
        update_worksheet(integrated_data, "Integrated_Data")
        ratio_data = calculate_ratio(integrated_data, Sample)
        update_worksheet(ratio_data, "Calculation_index")
    # High Limit, low Limit, high value, normal, value, low value
        header1, header2, header3 = ratio_evaluation(Sample, high_limit, low_limit, high_value, medium_value, low_value)
        x = x - 1 
    # timer has been put in place not to overload the API as often due to the quota problem
        time.sleep(4)
    # title
    # xlabel, ylabel
    barchart_data_sample, barchart_data_ratio1, barchart_data_ratio2, barchart_data_ratio3 = get_last_5_entires_ratio_values()
    # title, xlabel, ylabel
    plot_barchart(barchart_data_sample, barchart_data_ratio1, header1)
    plot_barchart(barchart_data_sample, barchart_data_ratio2, header2)
    plot_barchart(barchart_data_sample, barchart_data_ratio3, header3)
   
    
print("Welcome to Spectral Data Automation")

main()

# Test data of integration using the trapz numpy library 
# comparing to the classical method
# Test_Data()