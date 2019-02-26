import csv
import datetime
#import time
#Only import time if you need to time something

def states(statename):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    try:
        return us_state_abbrev[statename]
    except:
        print('A U.S. state name was not recognized')


with open('employee_data.csv', newline='') as csvfile:
    given = csv.reader(csvfile)
    record = list(zip(*zip(given)))[0]
    #This takes 0.001001119613647461 seconds to run
    record[0][1] = 'First Name'
    record[0].insert(2,'Last Name')
    for i in range(1,(len(record)-1)):
        record[i].insert(2,record[i][1].split(' ')[1])
        record[i][1] = record[i][1].split(' ')[0]
        date = datetime.datetime.strptime(record[i][3], '%Y-%m-%d')
        record[i][3] = datetime.datetime.strftime(date, '%m/%d/%Y')
        record[i][5] = states(record[i][5])
        record[i][4] = '***-**-'+record[i][4][7:]

    with open('employee_data_modified.csv', 'w', newline = '') as fcsv:
        write = csv.writer(fcsv)
        write.writerows(record)
    '''
    given = csv.reader(csvfile)
    record = []
    for row in given:
        record.append(row)
    #This takes 0.0010023117065429688 seconds to run
    record[0][1] = 'First Name'
    record[0].insert(2,'Last Name')
    for i in range(1,(len(record)-1)):
        record[i].insert(2,record[i][1].split(' ')[1])
        record[i][1] = record[i][1].split(' ')[0]
        date = datetime.datetime.strptime(record[i][3], '%Y-%m-%d')
        record[i][3] = datetime.datetime.strftime(date, '%m/%d/%Y')
        record[i][5] = states(record[i][5])
        record[i][4] = '***-**-'+record[i][4][7:]

    with open('employee_data_modified.csv', 'w', newline = '') as fcsv:
        write = csv.writer(fcsv)
        write.writerows(record)
    #print(record[1]) This is the first list for a person
    #print(record[1][1].split(' ')[0]) This is te first name
    '''