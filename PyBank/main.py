import itertools
import csv
with open('budget_data.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    next(data)
    dates = []
    money = []
    for row in data:
        dates.append(row[0])
        money.append(int(row[1]))
    #money = [int(i) for i in money]
    TotalMonths = len(dates)
    TotalDollars = sum(money)
    AvChange = round((TotalDollars/TotalMonths),2)
    BigInc = max(money)
    BigDay = dates[money.index(BigInc)]
    SmlDec = min(money)
    SmlDay = dates[money.index(SmlDec)]
    print('Financial Analysis\n----------------------------')
    print(f'Total Months: {TotalMonths}\nTotal: ${TotalDollars}\nAverage Change: ${AvChange}')
    print(f'Greatest Increase in Profits: {BigDay} (${BigInc})')
    print(f'Greatest Decrease in Profits: {SmlDay} (${SmlDec})')
    with open('output.txt','w') as text:
        text.write('Financial Analysis\n----------------------------\n')
        text.write(f'Total Months: {TotalMonths}\nTotal: ${TotalDollars}\nAverage Change: ${AvChange}\n')
        text.write(f'Greatest Increase in Profits: {BigDay} (${BigInc})\n')
        text.write(f'Greatest Decrease in Profits: {SmlDay} (${SmlDec})')
'''
#Both the below codes correctly populates the dates list with only the dates
    data = csv.DictReader(csvfile)
    dates = [row['Date'] for row in data]
  
    money = [row['Profit/Losses'] for row in data]
    for row in data:
        print(row)
        # break
#Can't print row['Profits/Losses'], but can print other
'''
'''
    data = csv.reader(csvfile)
    dates = list(row[0] for row in data)
    money = list(row[1] for row in data)
    prints both with row[0] or 1 respectively
'''