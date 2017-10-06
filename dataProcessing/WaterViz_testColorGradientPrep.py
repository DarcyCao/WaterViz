import csv, os
import collections




"""
This fuunction extracts the relevant data and sort according to key value.
Year month vs gallon/sqft, sorted according to timeline.
Output a csv file
"""
def dataPrep(path, name):
	sqft = float(name.split("_")[1].split(".")[0])
	print sqft
	with open(path + name, 'rb') as csvfile:
	    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
	    entry_dict = dict()
	    index = 0
	    for line in reader:
	    	#print line
	    	temp = line[0].split(',')
	    	key = int(temp[0]) + int(temp[1])*100
	    	#print key
	    	entry_dict[key] = round(int(temp[2])/sqft, 4)
	    	
	    #print entry_dict
	    od = collections.OrderedDict(sorted(entry_dict.items()))
	    print od
	    	
	    tsv_out = open("out" + ".tsv", "wb")
	    writer = csv.writer(tsv_out, delimiter='\t', lineterminator='\n')
	    writer.writerow(["index", "day", "hour", "value"])
	    #temp_row = [key, entry_dict[key]]
	    i = 0
	    for key in od:
	    	#print key%100, key/100
	    	writer.writerow([i, key/100, key%100, od.get(key)])
	    	i+=1





path = "/Users/darcy/Desktop/WaterViz/"
name = "ID0025ZZ_274412.csv"
dataPrep(path, name)
