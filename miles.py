import json
import time

try:
    f = open('miles.json', 'r+')
except Exception, e:
    f = open('miles.json', 'a+')

try:
    text = f.read()
    data = json.loads(text);

except Exception, e:
    data = [{
        "last_mile": 0,
        "total_miles": 45000,
        "datetime": time.strftime('%c')
    }]

print data

datum = data[-1]

last_mile = datum['last_mile']

total_miles = datum['total_miles']

datetime = datum['datetime']

try:
    miles = int(raw_input('Miles? \n'))
except Exception, e:
    print "That is not a number! \n"
    exit()

if int(miles) <= int(last_mile):
    print "The last recorded milage was: " + str(last_mile) + "\n"
    print "Please enter a value greater than that"
    exit()

theStr = "The last time you drove was: " + datetime + "\n"
theStr += "You've driven: " + str(last_mile + miles) + " total \n"
theStr += "Since you last drove you've driven " + str(miles - last_mile) + "\n"
theStr += "You have " + str(total_miles - miles) + " left \n"

print theStr

data.append({
    "last_mile": miles,
    "total_miles": 45000,
    "datetime": time.strftime('%c')
})
f.seek(0)
f.write(unicode(json.dumps(data, ensure_ascii=False)))
f.truncate()
f.close()