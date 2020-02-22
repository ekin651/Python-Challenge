import os
import csv
with open('budget_data.csv') as filecsv:
    csv_reader = csv.reader(filecsv)
 
    csv_header = next(filecsv)
    total_months = 0
    for row in csv_reader:
          total_months = total_months + 1         
    Results = (
        f"Total Months: {total_months} "
    )
    print  (Results)
with open('budget_data.csv') as filecsv:
    csv_reader = csv.reader(filecsv)
 
    csv_header = next(filecsv)
    profit_losses_total= 0
    for row in csv_reader:
        profit_losses_total = profit_losses_total + int(row[0])
    Results = (
        f"Total : ${profit_losses_total} "
    )
    print(Results)
with open('budget_data.csv') as filecsv:
    csv_reader = csv.reader(filecsv)
    
    csv_header = next(filecsv)
    
    past_profit_losses = 867884
    
    total_months = 0
    
    profit_change = []
    
    for row in csv_reader:
        
        total_months = total_months + 1  
        
        monthly_profit_dif = int(row[0]) - past_profit_losses
        
        past_profit_losses = int(row[0])
        
        profit_change.append(monthly_profit_dif)
        
        dif_profit_change = round(sum(profit_change)/total_months)
    Results = (
        f"Average Change : ${dif_profit_change} "
    )
    print(Results)
with open('budget_data.csv') as filecsv:
    csv_reader = csv.reader(filecsv)
    
    csv_header = next(filecsv)
    
    past_profit_losses = 867884
    greatest_increase=0
    lowest_decrease=10000000
      
    profit_change = []
    
    
    
    for row in csv_reader:
        
                
        monthly_profit_dif = int(row[0]) - past_profit_losses
        
        past_profit_losses = int(row[0])
        
        profit_change.append(monthly_profit_dif)
        
        dif_profit_change = round(sum(profit_change)/total_months)
        
        if (monthly_profit_dif  > greatest_increase):
            greatest_increase_month = row[1]
            greatest_increase =  monthly_profit_dif
       
        if (monthly_profit_dif < lowest_decrease):
            lowest_decrease_month = row[1]
            lowest_decrease = monthly_profit_dif
    
        
             
        
    Results = (
        f"Greatest Increase in Profit: {greatest_increase_month} ${greatest_increase} \n"
        f"Greates Decrease in Profit: {lowest_decrease_month} ${lowest_decrease} "
    )
    print( Results )
    