import json

f = open('miles.json', 'w+')
try:
    data = json.load(f);
    last_mile = data['last_mile']
    total_miles = data['total_miles']
except Exception, e:
    data = {
        'last_mile': 0,
        'total_miles': 45000
    }

    last_mile = data['last_mile']

    total_miles = data['total_miles']

miles = int(raw_input('Miles? \n'))

theStr = "You've driven: " + str(total_miles - last_mile + miles) + " total \n"
theStr += "Since you last drove you've driven " + str(last_mile + miles) + "\n"
theStr += "You have " + str(total_miles - miles) + " left \n"

print theStr
