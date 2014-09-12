import urllib
import re
import json
import csv

exchange = raw_input('Enter nyse, nasdaq, amex or custom. ')
frequency = raw_input('Enter 1D for daily, 1M for monthly or 1Y for yearly. ')

with open('./tickers/' + exchange + '.csv', 'rb') as tickers:
	reader = csv.reader(tickers)
	for row in reader:
		ticker = row[0]
		myfile = open("./prices/" + exchange + "/" + ticker +".txt", "w+")
		myfile.close()
		
		try:
			htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/" + frequency + "/" + ticker + ":US")
			data = json.load(htmltext)
			datapoints = data["data_values"]
			myfile = open("./prices/" + exchange + "/" + ticker +".txt", "a")
			for point in datapoints:
				myfile.write(str(ticker + "," + str(point[0]) + "," + str(point[1]) + "\n"))
			myfile.close()
		except:
			print "exception: would not retrieve data"