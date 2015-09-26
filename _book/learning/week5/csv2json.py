import csv
csvfile =  open('birdstrikes.csv', 'rb') 
birdstrikes = csv.reader(csvfile, delimiter=' ', quotechar='|')
for rom in birdstrikes:
	print rom[1]
