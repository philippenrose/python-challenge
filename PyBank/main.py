import os
import csv

# csv_path = os.path("C:\Users\Home\WUSTL201907DATA2\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv")

csv_path = os.path.join('Resources', 'budget_data.csv')

output_path = os.path.join("..", "output", "output_for_PyBank.txt")


def PyBank(Budget):
    Month = 0
    Month_List = []
    Profit_Losses = []
    Change_List = []

    # Count the number of months
    for row in csv_reader:
        Month += 1

        # Add Profit/Losses to a list
        Profit_Losses.append(float(row[1]))

        # Add Changes of each month to a list
        # Ensure variable is defined
        try:
            Prev_Month
        except NameError:
            Prev_Month = None

        # Find List of monthly changes
        # Test whether variable is defined to be None
        if Prev_Month is None:
            change = 0
            Prev_Month = float(row[1])
        else:
            change = float(row[1]) - Prev_Month
            Change_List.append(change)
            Prev_Month = float(row[1])
            Month_List.append(row[0])

    # Count Total Profit/Losses
    # Average Change Each Month
    Total_Profit_Losses = sum(Profit_Losses)
    Average_Change = sum(Change_List) / (Month - 1)

    # Find Greatest Increase and Decrease
    Greatest_Increase = max(Change_List)
    Greatest_Decrease = min(Change_List)

    Monthly_Changes = dict(zip(Change_List, Month_List))
    Date_I = Monthly_Changes[Greatest_Increase]
    Date_D = Monthly_Changes[Greatest_Decrease]

    print(f'# ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## #')
    print(f'### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##')
    print(f'##################################################################')
    print(f'Financial Analysis')
    print(f'##################################################################')
    print(f'Total Months: {Month}')
    print(f'Total Profit/Losses: ${Total_Profit_Losses}')
    print(f'Average Change: ${Average_Change}')
    print(f'Greatest Increase: {Date_I} with ${Greatest_Increase}')
    print(f'Greatest Decrease: {Date_D} with ${Greatest_Decrease}')
    print(f'##################################################################')
    print(f'### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##')
    print(f'# ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## #')


with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    print(csv_file)

    next(csv_reader, None)

    PyBank(csv_reader)
