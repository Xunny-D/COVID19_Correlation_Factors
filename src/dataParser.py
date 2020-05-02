import csv

counties = ["Los Angeles", "Snohomish", "New York City", "Harris"]
states = ["California", "Washington", "New York", "Texas"]

countiesCoronaCSV = open('us-counties.csv', 'r')
CaliTempsCSV = open('CaliTemps.csv', 'r')
WashingtonTempsCSV = open('WashingtonTemps.csv', 'r')
newYorkTempsCSV = open('newYorkTemps.csv', 'r')

NYCCSV = open('NYCTemps.csv', 'w', newline='')
snohomishCSV = open('snohomishTemps.csv', 'w', newline='')
LATempsCSV = open('LATemps.csv', 'w', newline='')
DataCSV = open('DATA.csv', 'w', newline='')

coronaReader = csv.reader(countiesCoronaCSV)
caliReader = csv.reader(CaliTempsCSV)
washingtonReader = csv.reader(WashingtonTempsCSV)
NYReader = csv.reader(newYorkTempsCSV)

NYCTempsWriter = csv.writer(NYCCSV)
snohomishTempsWriter = csv.writer(snohomishCSV)
LATempsWriter = csv.writer(LATempsCSV)
dataWriter = csv.writer(DataCSV)

for row in caliReader:
	if row[1] == "LOS ANGELES INTERNATIONAL AIRPORT, CA US":
		LATempsWriter.writerow(["Los Angeles", row[5], row[20]])

for row in washingtonReader:
	if row[1] == "ALPINE MEADOWS, WA US":
		snohomishTempsWriter.writerow(["Snohomish", row[5], row[20]])

for row in NYReader:
	if row[1] == "LAGUARDIA AIRPORT, NY US":
		NYCTempsWriter.writerow(["New York City", row[2], row[17]])

LATempsCSV.close()
snohomishCSV.close()
NYCCSV.close()

LATempsCSV = open('LATemps.csv', 'r')
snohomishCSV = open('snohomishTemps.csv', 'r')
NYCCSV = open('NYCTemps.csv', 'r')

LATempsReader = csv.reader(LATempsCSV)
snohomishReader = csv.reader(snohomishCSV)
NYCReader = csv.reader(NYCCSV)

dataWriter.writerow(["date", "county", "state", "fips", "cases", "deaths", "avg temp"])
for row1 in coronaReader:
	if row1[1] == "Los Angeles":
		for row2 in LATempsReader:
			if row1[0] == row2[1]:
				dataWriter.writerow([row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row2[2]])
				break
	elif row1[1] == "Snohomish":
		for row2 in snohomishReader:
			if row1[0] == row2[1]:
				dataWriter.writerow([row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row2[2]])
				break
	elif row1[1] == "New York City":
		for row2 in NYCReader:
			if row1[0] == row2[1]:
				dataWriter.writerow([row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row2[2]])
				break
