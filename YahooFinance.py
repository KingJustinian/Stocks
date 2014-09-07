import urllib2

print("Welcome to the Yahoo Finance Stock Program!")
print("Downloading 2 year historical records")

# Retrieve the webpage as a string
f = urllib2.urlopen("http://ichart.yahoo.com/table.csv?s=GIS&a=7&b=6&c=2014&d=8&e=6&f=2014&g=d")	
s = f.read()

outputTable = []
outputTable.append(['Quarter', 'Date', 'Close', 'Return'])

lines = s.split('\n')
headers = lines[0].split(',')
index = 0
for line in lines:
	stock = line.split(',')
	# The last row only contains a couple of columns
	if (len(stock) > 4):
		outputRow = [None] * 4
		outputRow[1] = stock[0]
		outputRow[2] = stock[4]
		# First row is headers, 2nd you can't calculate
		if (index >= 2):
			outputRow[3] = (float(outputRow[2]) - float(outputTable[index][2]))/float(outputTable[index][2])
		outputTable.append(outputRow)
	index += 1

tableSize = len(outputTable)
quarterDelimiter = tableSize / 8
index = 0
curQuarter = 1
for outputRow in outputTable:
	outputRow[0] = curQuarter
	index += 1
	if (index >= quarterDelimiter):
		index = 0
		curQuarter += 1

for outputRow in outputTable:
	print("##############")
	for outputCol in outputRow:
		print(outputCol)
