# Modules & file path
import os
import csv
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv.csv')

# Open and read CSV 
with open(csvpath) as csvfile:
    
    #  CSV Reader delimiter and variable 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header 
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Variables
    total_months = 0
    net_amount = 0
    monthly_change = []
    month_count = []
    greatest_increase = 0
    greatest_increase_month = 0
    greatest_decrease = 0
    greatest_decrease_month = 0

    # Calculate total number of months, net amount of "profit/losses", & set variables for rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Reach each row of data 
    for row in csvreader:
        
        # Calculate total number of months 
        total_months += 1
        # Calculate net amount of "profit/losses" 
        net_amount += int(row[1])

        # Calculate change from current month to previous 
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate greatest increase 
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate greatest decrease 
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate average and date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print 
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")

# Write output and open 
output_file = os.path.join('.', 'PyBank', 'analysis', 'budget_data_revised.text')
with open(output_file, 'w',) as txtfile:

# Write the new data 
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")