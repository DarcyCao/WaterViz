'''
Creates data for a single building (or a certain building)
	from the yearly data csv files got from step 1.
Rename file based on building id, State located and other bldg properties.
Discards redundant columns leaving only the consumption and cost of
	gas, electricity and water for future referance.


Data input columns:
	"Region No.",
	"State",[1]
	"Service Center",
	"Fiscal Month",[3]
	"Fiscal Year",[4]
	"Building Number",[5]
	"Area Field Office",
	"Cat",
	"Building Designation",
	"Gross Sq.Ft",[9]
	"Electricity (KWH)",[10]
	"Electricity (Cost)",[11]
	"Demand (KW)",
	"Demand (Cost)",
	"Steam (Thou. lbs)",
	"Steam (Cost)",
	"Gas (Cubic Ft)",[16]
	"Gas (Cost)",[17]
	"Oil (Gallon)",
	"Oil (Cost)",
	"Chilled Water (Ton Hr)",
	"Chilled Water (Cost)",
	"Renewable Electricity (KWH)",
	"Renewable Electricity (Cost)",
	"Renewable Gas (Cubic Ft)",
	"Renewable Gas (Cost)",
	"Other (mmBTU)",
	"Other (Cost)",
	"Water (Gallon)",[28]
	"Water (Cost)"[29]



Data output columns:
	in titie:
		("State",)
		"Building Number",
		"Gross Sq.Ft",
	in file:	
		"Fiscal Month",
		"Fiscal Year",
		"Electricity (KWH)",
		"Electricity (Cost)",
		"Gas (Cubic Ft)",
		"Gas (Cost)",
		"Water (Gallon)",
		"Water (Cost)"

'''



import os, csv

# creates empty files of unique bldg id in new folder
def createBldgCsvs(set_of_ids):
	os.chdir('./BldgCsvs/')
	temp_file_names = set_of_ids.copy()
	while len(temp_file_names) != 0:
		temp_file_name = temp_file_names.pop()
		# found new building. Create new file
		if temp_file_name not in os.listdir('.'):
			csv_file_temp = open(temp_file_name.strip('\"') + ".csv", 'a').close()
	return




def getYearlyData(year, path):
	os.chdir(path)
	for fn in os.listdir('.'):
		if (os.path.isfile(fn) & (fn != ".DS_Store") 
			& (str(year) in fn)):
			file_name = fn
			break
	print file_name + " found!"
	with open(path + file_name, 'rb') as csvfile:
	    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
	    entry_dict = dict()
	    index = 0
	    for line in reader:
			entry_dict[index] = line[0].split(',')
			index += 1

	print len(entry_dict)


	set_of_ids = set()
	for i in xrange(len(entry_dict)):
		bldg_id = entry_dict[i][5]
		if (len(bldg_id) == 10 and bldg_id not in set_of_ids):
			set_of_ids.add(bldg_id)
			#print "new building " + bldg_id + " added to the set."
	print "------------------------------"+str(len(set_of_ids)) + " bldg IDs found."


	createBldgCsvs(set_of_ids)
	print "All new files created."
	getBldgCsv(entry_dict)

	return






#   "State",[1]
# 	"Fiscal Month",[3]
# 	"Fiscal Year",[4]
# 	"Building Number",[5]
# 	"Gross Sq.Ft",[9]
# 	"Electricity (KWH)",[10]
# 	"Electricity (Cost)",[11]
# 	"Gas (Cubic Ft)",[16]
# 	"Gas (Cost)",[17]
# 	"Water (Gallon)",[28]
# 	"Water (Cost)"[29]


def getBldgCsv(entry_dict):
	print "Getting Bldg data..."
	#for i in xrange(10):

	for i in xrange(len(entry_dict)):
		temp_month = entry_dict[i][3]
		temp_year = entry_dict[i][4]
		temp_id = entry_dict[i][5]
		temp_Sqft = entry_dict[i][9]
		temp_ElecKWH = entry_dict[i][10]
		temp_ElecCost = entry_dict[i][11]
		temp_GasCubic = entry_dict[i][16]
		temp_GasCost = entry_dict[i][17]
		temp_WaterGallon = entry_dict[i][28]
		temp_WaterCost = entry_dict[i][29]
		if (temp_id+".csv") in os.listdir('.'):
			csv_file = open(temp_id + ".csv", 'a')
			writer = csv.writer(csv_file)
			temp_row = [temp_month.strip('\"'), temp_year.strip('\"'), temp_Sqft.strip('\"'), 
				temp_ElecKWH.strip('\"'), temp_ElecCost.strip('\"'), temp_GasCubic.strip('\"'), 
				temp_GasCost.strip('\"'), temp_WaterGallon.strip('\"'), temp_WaterCost.strip('\"')]
			writer.writerow(temp_row)
			print temp_row
			#entry_dict.pop(i) ??????why after delete this line it appends??

			csv_file.close()
	# search for bldg in all yearly files
	# rename and save

	return


# calls getBldgCsv() function while keeping track of all building ids
def main():
	path = "/Users/darcy/Desktop/WaterViz/EUAS/YearlyData/"
	for year in xrange(2003, 2016+1):
		getYearlyData(year, path)
		print "-------------------------------------------year ", year, " is entered into bldg data."

	return


main()
