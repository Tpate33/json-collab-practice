import json
from datetime import datetime, timedelta

# task 1 (load json file):
x = open("practice.json")
data = json.load(x)
x.close()

# task 2 (Print all message id):
print("Task 2:")
for i in data:
    print(i["messageID"])
print()

# task 3 : Print User Authentication Methods (userID and authentication)
print("Task 3:")
for i in data:
    print("UserID: ", i['userInfo']['userID'])
    print("Authetication Method: ", i['userInfo']['authentication']['method'])
    print()

#task 4: Task 4: Total the Payment Amount
payment_amount = 0
for sessions in data:
    payment_amount += sessions['userInfo']['payment']['amount']
print("This is the total payment amount across all sessions $" + str(payment_amount))
print('\n')

#Task 5: Filter Sessions by Payment Method
for sessions in data:
    if(sessions['userInfo']['payment']['method'] == 'credit_card'):
        print(sessions)
    print()

#Task 6: Print Session Duration
for session in data:
    start_str = session['userInfo']['session']['startTimestamp'] #Gets string for Start duration of current session
    end_str = session['userInfo']['session']['endTimestamp'] #Gets string for End duration of current session

    # Convert the timestamp strings to datetime objects
    start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ") 
    end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

    
    duration = end_time - start_time #Gives military time of EndTime - StartTime
    duration_minutes = duration.total_seconds() / 60 #Converts into an actual integer (Miuntes)

    print("Duration for this session ID: " + session['userInfo']['userID'] + ": " + str(duration_minutes) + " Minutes")
print()

#Task 7: Count Sessions per User
session_count = {}
for session in data:
    if(session['userInfo']['userID'] in session_count):
        session_count[session['userInfo']['userID']] += 1
    else:
        session_count[session['userInfo']['userID']] = 1

for value in session_count.values():
    print("This userID: " + session['userInfo']['userID'] + " has " + str(value) + " sessions")
print()

#Task 8: Create Summary Dictionary
summary_list = []
for session in data:
    start_str = session['userInfo']['session']['startTimestamp'] #Gets string for Start duration of current session
    end_str = session['userInfo']['session']['endTimestamp'] #Gets string for End duration of current session

    # Convert the timestamp strings to datetime objects
    start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ") 
    end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

    
    duration = end_time - start_time #Gives military time of EndTime - StartTime
    duration_minutes = duration.total_seconds() / 60 #Converts into an actual integer (Minutes)

    summary_dict = {
        'userID': session['userInfo']['userID'],
        'amount': session['userInfo']['payment']['amount'],
        'durationMinutes': duration_minutes
    }
    
    summary_list.append(summary_dict)

for summaries in summary_list:
    print(summaries)

#Task 9: Write Summary to a New JSON File
json_string = json.dumps(summary_list, indent=4)
f = open("summary_output.json", "w")
f.write(json_string)
f.close()


#Task 10: Make It a Function
def summarize_sessions(file_path):
    x = open(file_path)
    data = json.load(x)
    x.close()

    summary_list = []
    for session in data:
        start_str = session['userInfo']['session']['startTimestamp'] #Gets string for Start duration of current session
        end_str = session['userInfo']['session']['endTimestamp'] #Gets string for End duration of current session

        # Convert the timestamp strings to datetime objects
        start_time = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ") 
        end_time = datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")

    
        duration = end_time - start_time #Gives military time of EndTime - StartTime
        duration_minutes = duration.total_seconds() / 60 #Converts into an actual integer (Minutes)

        summary_dict = {
            'userID': session['userInfo']['userID'],
            'amount': session['userInfo']['payment']['amount'],
            'durationMinutes': duration_minutes
        }
    
        summary_list.append(summary_dict)

    for summaries in summary_list:
        print(summaries)

    #Task 9: Write Summary to a New JSON File
    json_string = json.dumps(summary_list, indent=4)
    f = open("summary_output.json", "w")
    f.write(json_string)
    f.close()

summarize_sessions("practice.json")