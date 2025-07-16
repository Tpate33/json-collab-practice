# Phase 3A - Random Log Generator
# Task 1 - Set Up the Script
import json
import random
import uuid
import datetime


# Task 2 - Build a Template for One Session
randomDict = {}
vendorList = ["ChargeGrid", "GreenCharge", "VoltNet"]

# Generate random userID
randomInt = random.randint(10000, 99999)
intStr = str(randomInt)
randomDict['UserID'] = "user-" + intStr

# Random selects vendor
vendorIndex = random.randint(0, len(vendorList)-1)
randomDict['Vendor'] = vendorList[vendorIndex]


# Random generate cost and method
method = ["credit_card", "mobile_wallet"]
randomDict['Amount'] = round(random.uniform(5.00, 30.00), 2)
methodIndex = random.randint(0, len(method) - 1)
randomDict["Method"] = method[methodIndex]


# Random generate authentication method + token
methodAut = ["RFID", "app_login", "app_qr"]
randomDict["Authentication"] = methodAut[random.randint(0, len(methodAut) - 1)]

# Token
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
randToken = ""

while (len(randToken) != 8) :
    tokenNum = random.randint(0, 1)
    # 0 for alphabet
    if (tokenNum == 0):
        randToken = randToken + alpha[random.randint(0, len(alpha)-1)]
    # 1 for digits 0-9
    else:
        randToken = randToken + str(random.randint(0,9))

randToken = randToken[:4] + '-' + randToken[4:]
randomDict["Token"] = randToken

# Random messageID
msgID = random.randint(0, 999)
if (msgID < 100):
    if (msgID < 10):
        msgStrID = "00" + str(msgID)
    else:
        msgStrID = "0" + str(msgID)

else:
    msgStrID = str(msgID)
msgStr = "msg-20250605-" + msgStrID
randomDict["MessageID"] = msgStr

# print(randomDict)


# Task 3 - Generate N Random Sessions

session_list = []
for i in range(0,99):
    # everything below was copied from task 2
    randomDict = {}
    vendorList = ["ChargeGrid", "GreenCharge", "VoltNet"]

    # Generate random userID
    randomInt = random.randint(10000, 99999)
    intStr = str(randomInt)
    randomDict['UserID'] = "user-" + intStr

    # Random selects vendor
    vendorIndex = random.randint(0, len(vendorList)-1)
    randomDict['Vendor'] = vendorList[vendorIndex]

    # Random generate startTime and endTime
    start_date = ""
    weekDays = "UMTWRFS"
    year = random.randint(1907, 2025)
    month = random.randint(1,12)
    # military time
    start_hour = random.randint(1, 24)
    start_min = random.randint(1, 60)
    start_seconds = random.randint(1, 60) 

    end_hour = random.randint(1, 24)
    end_min = random.randint(1, 60)
    end_seconds = random.randint(1, 60)


    dayOfWeek = weekDays[random.randint(0, len(weekDays)-1)]
    # need to check leap year how many days in the month for days
    # January
    if (month == 1):
        day = random.randint(1,31)
    # leap years February
    elif ((month == 2) and ((year == 1908) or (year == 1912) or (year == 1916) or (year == 1920) or (year == 1924) or (year == 1928) or (year == 1932) or (year == 1936) or (year == 1940) or (year == 1944) or (year == 1948) or (year == 1952) or (year == 1956) or (year == 1960) or (year == 1964) or (year == 1968) or (year == 1972) or (year == 1976) or (year == 1980) or (year == 1984) or (year == 1988) or (year == 1992) or (year == 1996) or (year == 2000) or (year == 2004) or (year == 2008) or (year == 2012) or (year == 2016) or (year == 2020) or (year == 2024))):
        day = random.randint(1,29)
    # Non leap years February
    elif ((month == 2) and ((year != 1908) or (year != 1912) or (year != 1916) or (year != 1920) or (year != 1924) or (year != 1928) or (year != 1932) or (year != 1936) or (year != 1940) or (year != 1944) or (year != 1948) or (year != 1952) or (year != 1956) or (year != 1960) or (year != 1964) or (year != 1968) or (year != 1972) or (year != 1976) or (year != 1980) or (year != 1984) or (year != 1988) or (year != 1992) or (year != 1996) or (year != 2000) or (year != 2004) or (year != 2008) or (year != 2012) or (year != 2016) or (year != 2020) or (year != 2024))):
        day = random.randint(1,29)
    # March
    elif (month == 3):
        day = random.randint(1,31)
    # April
    elif (month == 4):
        day = random.randint(1,30)
    # May
    elif (month == 5):
        day = random.randint(1,31)
    # June
    elif (month == 6):
        day = random.randint(1,30)
    # July
    elif (month == 7):
        day = random.randint(1,31)
    # August
    elif (month == 8):
        day = random.randint(1,31)
    # September
    elif (month == 9):
        day = random.randint(1,30)
    # October
    elif (month == 10):
        day = random.randint(1,31)
    # November
    elif (month == 11):
        day = random.randint(1,30)
    # December
    elif (month == 12):
        day = random.randint(1,31)


# Formatting

    if (month < 10):
        month = '0' + str(month)
    else:
        month = str(month)

    if (day < 10):
        day = '0' + str(day)
    else:
        day = str(day)

    if (start_hour < 10):
        start_hour = '0' + str(start_hour)
    elif (start_hour == 24):
        start_hour = '00'
    else:
        start_hour = str(start_hour)

    if (start_min < 10):
        start_min = '0' + str(start_min)
    else:
        start_min = str(start_min)

    if (start_seconds < 10):
        start_seconds = '0' + str(start_seconds)
    else:
        start_seconds = str(start_seconds)

    if (end_hour < 10):
        end_hour = '0' + str(end_hour)
    else:
        end_hour = str(end_hour)

    if (end_min < 10):
        end_min = '0' + str(end_min)
    else:
        end_min = str(end_min)

    if (end_seconds < 10):
        end_seconds = '0' + str(end_seconds)
    else:
        end_seconds = str(end_seconds)

    year = str(year)


    randomDict['startTimestamp'] = year + '-' + month + '-' + day + dayOfWeek + start_hour + ':' + start_min + ':' + start_seconds + 'Z'
    randomDict['endTimestamp'] = year + '-' + month + '-' + day + dayOfWeek + end_hour + ':' + end_min + ':' + end_seconds + 'Z'

    # Random generate cost and method
    method = ["credit_card", "mobile_wallet"]
    randomDict['Amount'] = round(random.uniform(5.00, 30.00), 2)
    methodIndex = random.randint(0, len(method) - 1)
    randomDict["Method"] = method[methodIndex]


    # Random generate authentication method + token
    methodAut = ["RFID", "app_login", "app_qr"]
    randomDict["Authentication"] = methodAut[random.randint(0, len(methodAut) - 1)]

    # Token
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
    randToken = ""

    while (len(randToken) != 8) :
        tokenNum = random.randint(0, 1)
        # 0 for alphabet
        if (tokenNum == 0):
            randToken = randToken + alpha[random.randint(0, len(alpha)-1)]
        # 1 for digits 0-9
        else:
            randToken = randToken + str(random.randint(0,9))

    randToken = randToken[:4] + '-' + randToken[4:]
    randomDict["Token"] = randToken

    # Random messageID
    msgID = random.randint(0, 999)
    if (msgID < 100):
        if (msgID < 10):
            msgStrID = "00" + str(msgID)
        else:
            msgStrID = "0" + str(msgID)

    else:
        msgStrID = str(msgID)
    msgStr = "msg-20250605-" + msgStrID
    randomDict["MessageID"] = msgStr
    session_list.append(randomDict)

print(session_list)


# Task 4 - Export to random_sessions.json
random_session = json.dumps(session_list, indent = 4)
w = open("random_sessions.json", "w")
w.write(random_session)
w.close()
print()