import requests
import datetime

def waterLevel(date):
    payload = {'format':'json',
                'site':'385041075395602',
                'startDt':date,
                'endDT':date}
    r = requests.get('https://waterservices.usgs.gov/nwis/iv/', params=payload).json()['value']['timeSeries'][0]['values'][0]['value']
    avgLevel = 0
    for item in r:
        avgLevel += float(item['value'])
    avgLevel = avgLevel / len(r)
    avgLevel = format(avgLevel, '.2f')
    avgLevel = float(avgLevel)
    readingDate = r[0]['dateTime']
    print(f'The water table level is {avgLevel}ft below land and was read at {readingDate}')
    return [avgLevel, readingDate]

dates = []
for i in range(0, 52):
    newDate = datetime.date(2021, 1, 5) + datetime.timedelta(days=7*i)
    dates.append(newDate.isoformat())

levels = []
for date in dates:
    levels.append(waterLevel(date)[0])
print(levels)