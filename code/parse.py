import json
import pandas as pd

with open ('json/files/jason_test.json') as f:
    data = json.load(f)
    
journeys = data['body']['data']['journeys']

trips = []

for journey in journeys:
    flight = (journey['flights'])
    for a in flight:
        trip = {
            'd_airport': a['airportDeparture']['code'],
            'a_airport': a['airportArrival']['code'],
            'd_date': a['dateDeparture'],
            'a_date': a['dateArrival'],
                }
        trips.append(trip)        
    trip['tax'] = journey['importTaxAdl']
    trip['id'] = journey['recommendationId'] #jei nereikia, išsitrink šitą
    
totals = []
for price in data['body']['data']['totalAvailabilities']:
    recommendation = {
        'id': price['recommendationId'],
        'totals': price['total']
        }
    totals.append(recommendation)

df_totals = pd.DataFrame(totals)
df_trips = pd.DataFrame(trips)

# sujungiu du df į vieną pagal ID
df= (pd.merge(df_totals, df_trips, on='id'))

#tik peržiūrėjimui, kad būtų patogiau
print (df)

#konvertuojam į csv 
df.to_csv('json/files/jason_test.csv', sep=',', index=False)