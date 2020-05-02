import csv

counties = ["Los Angeles", "Snohomish", "Harris"]
states = ["California", "Washington", "Texas"]
with open('us-counties.csv','r') as countiesCSV:
	csvReader = csv.reader(countiesCSV)
	with open('corona-data.csv', 'w') as coronaDataCSV:
		csvWriter = csv.writer(coronaDataCSV)
		for row in csvReader:
			if row[1] in counties and row[2] in states:
				csvWriter.writerow(row)
