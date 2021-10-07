import requests
from datetime import datetime, timedelta

def CoCoRaHs(date):
    payload = {'ReportType':'Daily',
               'Format':'JSON',
               'State':'DE',
               'StartDate':str(date - timedelta(days=7)),
               'EndDate':str(date),
               'Station':'DE-KN-24'}
    #DE-KN-03 Smyrna
    #DE-KN-24 Felton
    #DE-KN-28 Magnolia
    #DE-KN-12 Camden
    #DE-KN-31 Dover
    #DE-KN-32 Dover
    #DE-SS-30 Milford
    #DE-KN-13 Milford
    #DE-KN-20 Clayton
    r = requests.get('https://data.cocorahs.org/export/exportreports.aspx', params=payload).json()['data']
    totalPercip = 0
    for row in r['reports']:
        totalPercip += row['totalpcpn']
    print(totalPercip)

date = input('Enter date of reading (XX/XX/XXXX): ')
weekLong = input('Was it a long week? (Y/N): ')
weekShort = input('Was it a short week? (Y/N): ')

dateObj = datetime.strptime(date, '%m/%d/%Y')

CoCoRaHs(dateObj)
