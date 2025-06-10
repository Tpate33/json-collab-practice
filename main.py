import json
from datetime import datetime, timedelta

x = open('practice.json')
data = json.load(x)
print(data)

# Task 1 (load json file):
x = open("practice.json")
data = json.load(x)
x.close()

# Task 2 (Print all message id):
print("Task 2:")
for i in data:
    print(i["messageID"])
print()

# Task 3 : Print User Authentication Methods (userID and authentication)
print("Task 3:")
for i in data:
    print("UserID: ", i['userInfo']['userID'])
    print("Authetication Method: ", i['userInfo']['authentication']['method'])
    print()


# Task 4 : Total the Payment Amount
print("Task 4:")
totalAmount = 0
for i in data:
    totalAmount += i['userInfo']['payment']['amount']
    # print("Total Payment: $", i['userInfo']['payment']['amount'])
    
print("Total Payment: $", totalAmount)
print()


# Task 5 : Filter Sessions by Payment Method
print("Task 5: ")
for i in data:
    if (i['userInfo']['payment']['method'] == 'credit_card'):
        print(i['userInfo'])
print()


# Task 6 : Print Session Duration (YYYY-MM-DD)
print("Task 6: ")
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
print("Task 7: ")
my_list = []
same_list = []

# adds all userIDs into list for counting
for i in data:
    my_list.append(i['userInfo']['userID'])


for k in my_list:
    if (k not in same_list):
        print(k, "has", my_list.count(k), "sessions")
        same_list.append(k)
    
# print(my_list)


# Task 7 : Count Sessions per User using dictionary
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
print("Task 8: ")
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
print("Task 9:")
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

summarize_sessions("practice.json")

