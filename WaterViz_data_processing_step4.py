# -*- coding: utf-8 -*-
import csv, os, json
from pprint import pprint
from shutil import copyfile



'''
Cleaning data and put all building viz data into 4 buckets
according to the rate of completeness of water, gas and electricity data 
3_zeros: there are entries from this building with all three data absent in certain year
2_zeros: there are entries from this building with at most two data absent in certain year
1_zero: there are entries from this building with at most one data absent in certain year
0_zeros: here are no entries from this building with any data absent
'''

path0 = "/Users/darcy/Desktop/THESIS/3dWaterViz/bldg_data_viz2/"
path3 = "/Users/darcy/Desktop/THESIS/3dWaterViz/3_zeros/"
path2 = "/Users/darcy/Desktop/THESIS/3dWaterViz/2_zeros/"
path1 = "/Users/darcy/Desktop/THESIS/3dWaterViz/1_zero/"
path4 = "/Users/darcy/Desktop/THESIS/3dWaterViz/0_zero/"



#'bldgData', 'sqft', 'bldgId', 'bldgIndex'
#'water','index','elec','gas','time'
def readJson(filename):
	file = open(path0 + filename, 'r')
	#print file.readlines()
	j = json.load(file)
	#print j
	if (len(j['bldgData']) < 12 * 8):
		os.remove(path0+filename)
		return ("short", filename)

	#while (len())
	for i in range(len(j['bldgData'])):
		entry = j['bldgData'][i]
		if (entry['time'] < 201607):
			#if (entry['water'] == 0)

			if (entry['water'] == entry['gas'] == entry['elec'] == 0):
				copyfile(path0+filename, path3+filename)				
				os.remove(path0+filename)
				return ("3", filename)

			elif (entry['water'] == entry['gas'] == 0
				or entry['elec'] == entry['gas'] == 0
				or entry['water'] == entry['elec'] == 0):
				copyfile(path0+filename, path2+filename)
				os.remove(path0+filename)
				return ("2", filename)

			elif (entry['water']== 0
				or entry['elec'] == 0
				or entry['gas'] == 0):
				copyfile(path0+filename, path1+filename)
				os.remove(path0+filename)
				return ("1", filename)

			else:
				copyfile(path0+filename, path4+filename)
				os.remove(path0+filename)
				return ("0", filename)



	return




def readAll():
	nameList = os.listdir(path0);


	while (nameList != []):
		if (nameList[0] == ".DS_Store"):
			nameList.remove(nameList[0])

		if (nameList[0] != ".DS_Store"):
			message, filename = readJson(nameList[0])
			nameList.remove(filename)
			print filename, 'removed'


	return

	#print l

	# for i in range(len(nameList)):
	# 	name = nameList[i]
	# 	if (name != ".DS_Store"):
	# 		readJson(name)
	# 		print i, 'is done!'

	return



readAll()
#readJson('/AK0000AA_727340_viz.txt', path0, path3, path2, path1, path4)


def seperate3Zeros(path0, path3):





	return



def seperate2Zeros(path0, path2):





	return


def seperate1Zero(path0, path1, path4):





	return







def main ():
	seperate3Zeros(path0, path3)
	print("3...")
	seperate2Zeros(path0, path2)
	print("2...")
	seperate1Zero(path0, path1, path4)
	print("1...")



#main()






