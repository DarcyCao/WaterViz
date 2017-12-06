import csv, os, json
import collections


def changeNameOfFiles(path):
	os.chdir(path)
	for fn in os.listdir('.'):
		if (os.path.isfile(fn) & (fn != ".DS_Store")):
			#next(reader)print fn
			file_name1 = fn
			with open(path +file_name1, 'rb') as csvfile:
				reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
				file_name2 = next(reader)[2]
				file_name3 = next(reader)[2]
				#print file_name3, file_name2
				if (file_name2 == file_name3): #check if it's sqft
					newName = fn.split(".tsv")[0] + "_" + file_name2.split(".0")[0] + ".tsv"
					print newName
					os.rename(fn, newName)
	print "changed name format into id + sqft."
	return




"""
This function extracts the relevant data and sort according to key value.
Output a tsv file with index, Year + month, gallon/sqft, sorted according to timeline.

"""
def dataPrep(path, name, path2, count):
	hostDict = dict()
	sqft = float(name.split("_")[1].split(".")[0])
	bldgId = name.split("_")[0].split(".")[0]
	hostDict["sqft"] = sqft
	hostDict['bldgId'] = bldgId
	hostDict['bldgIndex'] = count
	print sqft, bldgId
	if (sqft != 0):
		with open(path + name, 'rb') as csvfile:
		    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		    entry_dict = dict()
		    index = 0
		    for line in reader:
		    	#print line
		    	temp = line[0].split('\t')
		    	key = int(float(temp[0]) + float(temp[1])*100)
		    	#print key
		    	entry_dict[key] = [round(float((temp[-2]))/sqft, 4), 
		    	round(float((temp[-4]))/sqft, 4), round(float((temp[-6]))/sqft, 4)]
		    	#print temp
		    	#print entry_dict[key]

		    #print entry_dict
		    od = collections.OrderedDict(sorted(entry_dict.items()))
		    #print od


		    json_out = open(path2 + name.split(".tsv")[0] + "_viz" + ".txt", "wb")

		    hostDict["bldgData"] = []
		    i = 0
		    for key in od:
		    	tempDict = dict()
		    	tempDict["index"] = i
		    	tempDict["time"] = key
		    	tempDict["elec"] = od.get(key)[0]
		    	tempDict["gas"] = od.get(key)[1]
		    	tempDict["water"] = od.get(key)[2]
		    	hostDict["bldgData"].append(tempDict)
		    	i+=1

		    print hostDict["bldgData"]
		    with json_out as outfile:
		    	json.dump(hostDict, outfile)
		    	
		    # tsv_out = open(path2 + name.split(".tsv")[0] + "_viz" + ".tsv", "wb")
		    # writer = csv.writer(tsv_out, delimiter='\t', lineterminator='\n')
		    # writer.writerow(["index", "day", "hour", "value"])
		    # #temp_row = [key, entry_dict[key]]
		    # i = 0
		    # for key in od:
		    # 	#print key%100, key/100
		    # 	writer.writerow([i, key/100, key%100, od.get(key)])
		    # 	i+=1




path = "/Users/darcy/Desktop/THESIS/dataProcessing/EUAS/YearlyData/BldgTsvs/"
#[1]
#changeNameOfFiles(path)

path2 = "/Users/darcy/Desktop/THESIS/WaterViz/VIZZ/bldg_data_viz2/"
def preps(path, path2):
	os.chdir(path)
	#look for yearly data files
	count = 0
	name_arr = []
	for fn in os.listdir('.'):
		if (os.path.isfile(fn) & (fn != ".DS_Store")):
			file_name = fn
			
			
			temp = "bldg_data_viz2/" +file_name.split(".tsv")[0] + "_viz" + ".csv"
			sqft = file_name.split(".tsv")[0].split('_')[1]
			if (sqft != 0):
				name_arr.append(temp)
				print temp
			#dataPrep(path, file_name, path2, count)
			count += 1



	return name_arr

#dataPrep(path, 'AK0000AA_727340.tsv', path2, 1)

print preps(path, path2)

# path0 = "/Users/darcy/Desktop/WaterViz/"
# name = "ID0025ZZ_274412.csv"

#dataPrep(path, name)






