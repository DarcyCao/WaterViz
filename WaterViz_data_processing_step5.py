#!/usr/bin/python
# -*- encoding: utf-8 -*-
import csv, os, json
from pprint import pprint
from shutil import copyfile

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

'''
Using the data from the best two buckets and format them so that 
they can be loaded into the visualization


o_zero:4 
1_zero:632
Make the connection between data and states / geolocation

'''



# path0 = "/Users/darcy/Desktop/THESIS/3dWaterViz/bldg_data_viz2/"
# path3 = "/Users/darcy/Desktop/THESIS/3dWaterViz/3_zeros/"
# path2 = "/Users/darcy/Desktop/THESIS/3dWaterViz/2_zeros/"
# path1 = "/Users/darcy/Desktop/THESIS/3dWaterViz/1_zero/"
# path4 = "/Users/darcy/Desktop/THESIS/3dWaterViz/0_zero/"
pathin = "/Users/darcy/Desktop/THESIS/3dWaterViz/GeoPairing/"
pathout = "/Users/darcy/Desktop/THESIS/3dWaterViz/GeoPairing/GeoPaired/"
path = "/Users/darcy/Desktop/THESIS/3dWaterViz/"

states = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL","GA","HI","IL",
"ID","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE",
"NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN",
"TX","UT","VT","VA","WA","WV","WI","WY"];




#'bldgData', 'sqft', 'bldgId', 'bldgIndex'
#'water','index','elec','gas','time'

def geoPairing():
	nameList = os.listdir(pathin);
	for i in range(len(nameList)):
		if (nameList[i] == ".DS_Store" or nameList[i] == 'GeoPaired'):
			continue
		else: 
			json_filein = pathin + nameList[i]
			# #print file.readlines()
			# j = json.load(file)
			# print j
			print json_filein
			with open(json_filein) as json_file:
				json_decoded = json.load(json_file)
				#print json_decoded
				state = json_decoded['bldgId'][:2]
				if (state == 'DC'):
					state = 'MD'
					json_decoded['DC'] = True

				stateIndex = states.index(state)
				
				json_decoded['state'] = state
				json_decoded['stateIndex'] = stateIndex
				print state, stateIndex


				#save updated json file into the new folder Geopaired
				json_fileout = pathout + nameList[i]
				with io.open(json_fileout, 'w', encoding='utf8') as outfile:
				    str_ = json.dumps(json_decoded,
				                      indent=4, sort_keys=True,
				                      separators=(',', ': '), ensure_ascii=False)
				    outfile.write(to_unicode(str_))

				# Read JSON file
				with open(json_fileout) as data_file:
				    data_loaded = json.load(data_file)

				print(json_decoded == data_loaded)

	return


def getFileNames():
	tempList = []
	for fn in os.listdir(pathout):
		if (fn != ".DS_Store"):
			file_name = fn
			print file_name+","
			tempList.append(file_name+",")
	with open('path + "viz_file_names.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
    				quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(tempList)
		csvfile.close()
			

	return





#geoPairing()
getFileNames()




















