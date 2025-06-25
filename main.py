# Author: Karen M and Taufeeq P
# Date: 06/18/2025
# Description: EV Charging Session Analyzer


import json
from datetime import datetime, timedelta
import csv


# Phase 1
x = open('practice.json')
data = json.load(x)
print(data)

# Task 1 (load json file):
print("Task 1: Loading json file")
x = open("practice.json")
data = json.load(x)
x.close()
print()


# Task 2 (Print all message id):
print("Task 2: Printing All MessageID")
for i in data:
    print(i["messageID"])
print()


# Task 3 : Print User Authentication Methods (userID and authentication)
print("Task 3: Printing User Authentication Methods")
for i in data:
    print("UserID: ", i['userInfo']['userID'])
    print("Authetication Method: ", i['userInfo']['authentication']['method'])
    print()


# Task 4 : Total the Payment Amount
print("Task 4: Total Payment")
totalAmount = 0
for i in data:
    totalAmount += i['userInfo']['payment']['amount']
    # print("Total Payment: $", i['userInfo']['payment']['amount'])
    
print("Total Payment: $", totalAmount)
print()


# Task 5 : Filter Sessions by Payment Method
print("Task 5: Payment Methods")
for i in data:
    if (i['userInfo']['payment']['method'] == 'credit_card'):
        print(i['userInfo'])
print()


# Task 6 : Print Session Duration (YYYY-MM-DD)
print("Task 6: Session Duration")
for i in data:
    print("User: ", i['userInfo']['userID'])
    start_str = i['userInfo']['session']['startTimestamp']
    end_str = i['userInfo']['session']['endTimestamp']

    # turns string into format YYYY-MM-DD HH-MM-MS (Date, Time)
    start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ")
    end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

    #testing purposes
    # print(start_time)
    # print(end_time)

    duration = end_time - start_time
    duration_minutes = duration.total_seconds() / 60
    print(duration)
    print(duration_minutes, "minutes")
    print()
print()


# Task 7 : Count Sessions per User using list
print("Task 7: User Session Count using List")
my_list = []
same_list = []

# adds all userIDs into list for counting
for i in data:
    my_list.append(i['userInfo']['userID'])

for j in my_list:
    if (j not in same_list):
        print(j, "has", my_list.count(j), "sessions")
        same_list.append(j)
print()
# print(my_list)


# Task 7 : Count Sessions per User using dictionary (Taufeeq's Method)
print("Task 7: User Session Count using Dict")
session_count = {}
for session in data:
    if(session['userInfo']['userID'] in session_count):
        session_count[session['userInfo']['userID']] += 1
    else:
        session_count[session['userInfo']['userID']] = 1
for value in session_count.values():
    print(value)
print()


# Task 8 : Create Summary Dictionary
print("Task 8: Creating Summary Dictionary")
my_list = []
for i in data:
    # caculate duration
    start_str = i['userInfo']['session']['startTimestamp']
    end_str = i['userInfo']['session']['endTimestamp']

    # turns string into format YYYY-MM-DD HH-MM-MS (Date, Time)
    start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ")
    end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

    duration = end_time - start_time
    duration_minutes = duration.total_seconds() / 60

    session_summary = {
        'UserID' : i['userInfo']['userID'],
        'Amount' : i['userInfo']['payment']['amount'],
        'Duration' : duration_minutes
    }

    my_list.append(session_summary)

print(my_list)
print()


# Task 9 : Write Summary to a New JSON File
print("Task 9: Writing summary to new JSON file")
json_string = json.dumps(my_list, indent = 4)
w = open("summary.json", "w")
w.write(json_string)
w.close()


# Task 10 : Make Task 8 and 9 in function
def summarize_sessions(file_path):
    # task 1
    x = open(file_path)
    data = json.load(x)
    x.close()

    # Task 8
    my_list = []
    for i in data:
        # caculate duration
        start_str = i['userInfo']['session']['startTimestamp']
        end_str = i['userInfo']['session']['endTimestamp']

        # turns string into format YYYY-MM-DD HH-MM-MS (Date, Time)
        start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ")
        end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

        duration = end_time - start_time
        duration_minutes = duration.total_seconds() / 60

        session_summary = {
            'UserID' : i['userInfo']['userID'],
            'Amount' : i['userInfo']['payment']['amount'],
            'Duration' : duration_minutes
        }
        my_list.append(session_summary)


    # Task 9
        json_string = json.dumps(my_list, indent = 4)
        w = open("summary.json", "w")
        w.write(json_string)
        w.close()

#calling function
summarize_sessions("practice.json")
print()
print()




# Phase 2
# Task 1 Add a New Session
print("Task 1: Adding new session to practice.json")
# done by tasks above
print()


# Task 2 Filteration (Remove All Sessions with Mobile Wallet Payments)
print("Task 2: Filtering out Mobile Wallet Payments (filtered_sessions.json)")
filtered_list = []
for i in data:
    if (i['userInfo']['payment']['method'] != "mobile_wallet"):
        filtered_list.append(i)
        
# print(filtered_list)
filtered_string = json.dumps(filtered_list, indent = 4)
w = open("filtered_sessions.json", "w")
w.write(filtered_string)
w.close()
print()


# Task 3: Group Sessions by Vendor Name
print("Task 3: Group Sessions by Vendor")
vendorName_list = []
my_dict = {}
for i in data:
    if (i['chargingStation']['vendor'] not in vendorName_list):
        vendorName_list.append(i['chargingStation']['vendor'])
        my_dict[i['chargingStation']['vendor']] = []

for k in vendorName_list:
    for p in data:
        if (p['chargingStation']['vendor'] == k):
            my_dict[k].append(p)

print(my_dict)
print()


# Task 4: Find the Longest Session
print("Task 4: Longest Session")
longest = 0.00
for i in data:
        # caculate duration
        start_str = i['userInfo']['session']['startTimestamp']
        end_str = i['userInfo']['session']['endTimestamp']

        # turns string into format YYYY-MM-DD HH-MM-MS (Date, Time)
        start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ")
        end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

        duration = end_time - start_time
        duration_minutes = duration.total_seconds() / 60
        
        if (duration_minutes > longest):
            longest = duration_minutes
            userID = i['userInfo']['userID']
            messageID = i['messageID']

print("The longest session is held by", userID, "with a duration of", longest, "minutes and a messageID of", messageID, "." )
print()


# Task 5: Anonymize User Info
print("Task 5: Anonymize User Info")
anonymized_list = []
for i in data:
    anonymized_list.append(i)
    #Tast 5 Pt. 2 Removing Token
    del i['userInfo']['authentication']['token']


for k in anonymized_list:
    k['userInfo']['userID'] = 'anonymous'

anonymized_string = json.dumps(anonymized_list, indent = 4)
w = open("anonymized_sessions.json", "w")
w.write(anonymized_string)
w.close()
print(anonymized_string)
print()


# Task 6 Currency Conversion
x = open('practice.json')
data = json.load(x)
x.close()
print("Task 6: Currency Conversion (USD > EUR)")
for i in data:
   # rounds to the second place value
   euro = round(i['userInfo']['payment']['amount'] * 0.93, 2)
   i["amountEUR"] =  euro
   print(i)
   print()
   


# Task 7
print("Task 7: Format and Export Summary CSV")
csv_list = []
for i in data:
    # caculate duration
    start_str = i['userInfo']['session']['startTimestamp']
    end_str = i['userInfo']['session']['endTimestamp']

    # turns string into format YYYY-MM-DD HH-MM-MS (Date, Time)
    start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ")
    end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

    duration = end_time - start_time
    duration_minutes = duration.total_seconds() / 60

    session_csv = {
        'UserID' : i['userInfo']['userID'],
        'Vendor' : i['chargingStation']['vendor'],
        'Amount' : i['userInfo']['payment']['amount'],
        'Duration' : duration_minutes
    }

    csv_list.append(session_csv)
    with open("summary_csv", 'w', newline='') as file:
        fieldnames = ['UserID', 'Vendor', 'Amount', 'Duration']
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(csv_list)

for i in csv_list:
    print(i)
print()




# Phase 3A
